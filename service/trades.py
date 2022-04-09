from .gemini_client import GeminiClient
from .external_trades import ExternalTradesService
from .binance_client import BinanceClient
import os
import json
from tabulate import tabulate

import datetime

USE_CACHE = True

class TradeHistoryService():
    def __init__(self):
        self._cache = {}
        self._gemini_client = GeminiClient()
        self._binance_client = BinanceClient()
        self._external_trades_service = ExternalTradesService("/Users/julio/Development/gemini-cli/external_orders")

    def get_past_trades(self, symbol):
        if USE_CACHE and symbol in self._cache:
            return self._cache[symbol]
        gemini_past_trades = self._gemini_client.get_past_trades(symbol)

        external_trades = self._external_trades_service.get_orders(symbol)
        self._cache[symbol] = gemini_past_trades + external_trades
        return self._cache[symbol]
        
    def calculate_total_crypto_investment(self, symbol):
        past_trades = self.get_past_trades(symbol)
        total_investment = 0.0
        for trade in past_trades:
            total_investment += float(trade['amount'])
        return total_investment

    def calculate_total_fiat_investment(self, symbol):
        past_trades = self.get_past_trades(symbol)
        total_investment = 0
        for trade in past_trades:
            trade_date = self._gemini_client.timestamp_to_datetime(trade['timestamp'])
            amount = float(trade['amount'])
            price = float(trade['price'])
            fee_amount = float(trade['fee_amount'])
            total_investment += (amount * price) + fee_amount
        return total_investment
        

    def calculate_avg_price(self, symbol):
        past_trades = self.get_past_trades(symbol)
        nominator = 0
        denominator = 0
        for trade in past_trades:
            trade_date = self._gemini_client.timestamp_to_datetime(trade['timestamp'])
            amount = float(trade['amount'])
            price = float(trade['price'])

            nominator += (amount * price)
            denominator += amount

        avg_price = (nominator / denominator) if denominator != 0 else 0

        return avg_price

    def get_base_pair(self, symbol):
        return symbol[:3]

    def get_last_price(self, symbol):
        return self._gemini_client.get_last_price(symbol)

    def print_investment_summary(self, symbols, subtract_alts=False):
        table = []
        table.append(["SYMBOL","PRINCIPAL","AMOUNT", "AVG PRICE","LAST PRICE", "CUR VALUE", "GAIN/LOSS", "BRK EVEN"])
        total_investment_principal = 0.0
        total_investment_value = 0.0
        portfolio_percents = {}
        for symbol in symbols:
            avg_price = self.calculate_avg_price(symbol)
            investment_principal = self.calculate_total_fiat_investment(symbol)
            total_crypto_investment = self.calculate_total_crypto_investment(symbol)
            last_price = self.get_last_price(symbol)

            if subtract_alts:
                # Get alts bought with crypto investment
                alts_purchased_total = self._binance_client.get_base_pair_total(symbol[:3])
                print("Total {symbol} used to purchase alts: {amount}".format(symbol=symbol[:3], amount=alts_purchased_total))
                # Subtract alts from crypt investment
                total_crypto_investment -= alts_purchased_total

            # print ("{symbol} investment = {inv} * {price}".format(symbol=symbol, inv=total_crypto_investment, price=last_price))
            investment_value = total_crypto_investment * last_price
            gain = investment_value - investment_principal

            break_even = investment_principal / total_crypto_investment if total_crypto_investment != 0 else 0
            
            total_investment_principal += investment_principal
            total_investment_value += investment_value

            portfolio_percents[symbol] = {
                'principal': investment_principal,
                'gain': gain
            }
            

            table.append([symbol, investment_principal, total_crypto_investment, avg_price, last_price, investment_value, gain, break_even])
        
        total_gain = total_investment_value - total_investment_principal
        table.append(['TOTAL', total_investment_principal, 0.0, 0.0, 0.0, total_investment_value, total_gain, 0.0])
        
        print (tabulate(table, headers="firstrow"))
        print ("")
        date = datetime.datetime.now()
        print ("Prices as of %s" % (date.isoformat()))

        if total_investment_value > 1000000:
            print("\nCongrats, you are a crypto millionaire!")

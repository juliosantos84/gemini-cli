from .gemini_client import GeminiClient
import os

class TradeHistoryService(GeminiClient):
    def __init__(self):
        super().__init__(
            api_key     = os.getenv("AUDITOR_API_KEY"), 
            api_secret  = os.getenv("AUDITOR_API_SECRET"), 
            sandbox     = False
        )

    def calculate_total_crypto_investment(self, symbol):
        past_trades = self.private_client.get_past_trades(symbol)
        total_investment = 0.0
        for trade in past_trades:
            total_investment += float(trade['amount'])
        return total_investment

    def calculate_total_fiat_investment(self, symbol):
        past_trades = self.private_client.get_past_trades(symbol)
        total_investment = 0
        for trade in past_trades:
            trade_date = self.timestamp_to_datetime(trade['timestamp'])
            amount = float(trade['amount'])
            price = float(trade['price'])
            fee_amount = float(trade['fee_amount'])
            total_investment += (amount * price) + fee_amount
        return total_investment
        

    def calculate_avg_price(self, symbol):
        past_trades = self.private_client.get_past_trades(symbol)
        nominator = 0
        denominator = 0
        for trade in past_trades:
            trade_date = self.timestamp_to_datetime(trade['timestamp'])
            amount = float(trade['amount'])
            price = float(trade['price'])

            nominator += (amount * price)
            denominator += amount

        avg_price = nominator / denominator
        return avg_price

    def print_investment_summary(self, symbols):
        print ("SYMBOL\t\PRINCIPAL\tAVG PRICE\tCUR VALUE\tGAIN/LOSS\tBRK EVEN")
        total_investment_principal = 0.0
        total_investment_value = 0.0
        for symbol in symbols:
            avg_price = self.calculate_avg_price(symbol)
            investment_principal = self.calculate_total_fiat_investment(symbol)
            total_crypto_investment = self.calculate_total_crypto_investment(symbol)
            ticker = self.public_client.get_ticker(symbol)
            last_price = self.get_last_price(symbol)

            investment_value = total_crypto_investment * last_price
            gain = investment_value - investment_principal

            break_even = investment_principal / total_crypto_investment

            total_investment_principal += investment_principal
            total_investment_value += investment_value

            print ("%s\t%08.2f\t$%08.2f\t%08.2f\t%08.2f\t%08.2f" % (symbol, investment_principal, avg_price, investment_value, gain, break_even))
        
        total_gain = total_investment_value - total_investment_principal
        total_break_even = total_investment_value - total_investment_principal
        print ("%s\t%08.2f\t$%08.2f\t%08.2f\t%08.2f\t%08.2f" % ('TOTAL', total_investment_principal, 0.0, total_investment_value, total_gain, total_break_even))

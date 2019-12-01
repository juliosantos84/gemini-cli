import gemini
import json
import logging as log
import os
from datetime import datetime

auditor_api_key = os.getenv("AUDITOR_API_KEY")
auditor_api_secret = os.getenv("AUDITOR_API_SECRET")

public_client = gemini.PublicClient()

private_client = gemini.PrivateClient(auditor_api_key, auditor_api_secret)

def calculate_total_investment(symbol):
    past_trades = private_client.get_past_trades(symbol)
    total_investment = 0
    for trade in past_trades:
        trade_date = datetime.fromtimestamp(trade['timestamp'])
        amount = float(trade['amount'])
        price = float(trade['price'])
        fee_amount = float(trade['fee_amount'])
        total_investment += (amount * price) + fee_amount
    return total_investment
    

def calculate_avg_price(symbol):
    past_trades = private_client.get_past_trades(symbol)
    nominator = 0
    denominator = 0
    for trade in past_trades:
        trade_date = datetime.fromtimestamp(trade['timestamp'])
        amount = float(trade['amount'])
        price = float(trade['price'])

        nominator += (amount * price)
        denominator += amount

    avg_price = nominator / denominator
    return avg_price

def print_investment_summary(symbols):
    print ("Investment Summary")
    for symbol in symbols:
        avg_price = calculate_avg_price(symbol)
        total_investment = calculate_total_investment(symbol)
        print ("%s: %f @ $%f" % (symbol, total_investment, avg_price))

print_investment_summary(['BTCUSD','ETHUSD', 'ZECUSD', 'LTCUSD'])

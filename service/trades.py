from .gemini_client import GeminiClient
import os

class TradeHistoryService(GeminiClient):
    def __init__(self):
        super().__init__(
            api_key     = os.getenv("AUDITOR_API_KEY"), 
            api_secret  = os.getenv("AUDITOR_API_SECRET"), 
            sandbox     = False
        )

    def calculate_total_investment(self, symbol):
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
        print ("Investment Summary")
        for symbol in symbols:
            avg_price = self.calculate_avg_price(symbol)
            total_investment = self.calculate_total_investment(symbol)
            print ("%s: %f @ $%f" % (symbol, total_investment, avg_price))


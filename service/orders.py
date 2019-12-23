from .gemini_client import GeminiClient
import os

class OrderService(GeminiClient):
    def __init__(self):
        super().__init__(
            api_key     = os.getenv("TRADER_API_KEY"), 
            api_secret  = os.getenv("TRADER_API_SECRET"), 
            sandbox     = False
        )

    def buy(self, symbol, amount, price):
        return self.private_client.new_order(symbol, amount=str(amount), price=str(price), side='buy')
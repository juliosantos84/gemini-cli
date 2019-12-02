from .gemini_client import GeminiClient
import os

class OrderService(GeminiClient):
    def __init__(self):
        super().__init__(
            api_key     = os.getenv("TRADER_API_KEY"), 
            api_secret  = os.getenv("TRADER_API_SECRET"), 
            sandbox     = False
        )
    
    def list_prices(self, symbols=['BTCUSD', 'ETHUSD', 'LTCUSD', 'ZECUSD']):
        for s in symbols:
            ticker = self.public_client.get_ticker(s)
            bid = ticker['bid']
            ask = ticker['ask']
            last = ticker['last']
            print ("%s: %s < %s < %s" % (s, bid, last, ask))

    def buy(self, symbol, amount, price):
        return self.private_client.new_order(symbol, amount=amount, price=price, side='buy')
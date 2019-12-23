import gemini
import os
from datetime import datetime

class GeminiClient:
    def __init__(self, api_key, api_secret, sandbox=False):
        self._auditor_api_key = api_key
        self._auditor_api_secret = api_secret
        self.public_client = gemini.PublicClient()
        self.private_client = gemini.PrivateClient(self._auditor_api_key, self._auditor_api_secret)
    
    def get_last_price(self, symbol):
        ticker = self.public_client.get_ticker(symbol)
        return float(ticker['last'])

    def list_prices(self, symbols=['BTCUSD', 'ETHUSD', 'LTCUSD', 'ZECUSD']):
        for s in symbols:
            ticker = self.public_client.get_ticker(s)
            bid = ticker['bid']
            ask = ticker['ask']
            last = ticker['last']
            print ("%s: %s < %s < %s" % (s, bid, last, ask))

    def timestamp_to_datetime(self, timestamp):
        datetime.fromtimestamp(timestamp)
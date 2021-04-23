import gemini
import os
from datetime import datetime
import json

class GeminiClient:
    def __init__(
        self, 
        api_key = os.getenv("GEMINI_AUDITOR_API_KEY"), 
        api_secret = os.getenv("GEMINI_AUDITOR_API_SECRET"), 
        sandbox=False):
        self._auditor_api_key = api_key
        self._auditor_api_secret = api_secret
        self.public_client = gemini.PublicClient()
        self.private_client = gemini.PrivateClient(self._auditor_api_key, self._auditor_api_secret)
    
    def iserror(self, response):
        # {"result": "error", "reason": "Maintenance", "message": "The Gemini Exchange is currently undergoing maintenance."}
        return isinstance(response, dict) and response['result'] == 'error'

    def get_last_price(self, symbol):
        ticker = self.public_client.get_ticker(symbol)
        last = float(ticker['last'])
        return last

    def list_prices(
        self, 
        symbols=[
            'BTCUSD', 'ETHUSD', 'LTCUSD', 'ZECUSD', 
            'FILUSD', 'LINKUSD', 'BATUSD', 'MKRUSD', 'AAVEUSD', 'YFIUSD', '1INCHUSD'
        ]
        ):
        for s in symbols:
            ticker = self.public_client.get_ticker(s)
            bid = ticker['bid']
            ask = ticker['ask']
            last = ticker['last']
            print ("%s: %s < %s < %s" % (s, bid, last, ask))

    def timestamp_to_datetime(self, timestamp):
        datetime.fromtimestamp(timestamp)

    def get_past_trades(self, symbol):
            past_trades = self.private_client.get_past_trades(symbol)

            if self.iserror(past_trades):
                raise Exception("Unable to get past trades, reason: %s\n\t%s"%(past_trades['reason'], past_trades['message']))

            return past_trades
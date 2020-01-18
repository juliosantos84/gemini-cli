import os
import json

class ExternalTradesService():
    def __init__(self,inputDir="external_orders"):
        self._inputDir = inputDir
        self._cache = {}

    def get_orders(self, symbol = None):
        
        if symbol is None:
            return []
        
        inputFile = os.path.join(self._inputDir, "%s.json" % (symbol))

        if not os.path.exists(inputFile):
            return []
        else:
            with open(inputFile, "r") as external_trades:
                data = external_trades.read()
                orders = json.loads(data)
                return orders
                    


# ets = ExternalTradesService(inputDir="/Users/julio/Development/gemini-cli/external_orders")

# orders = ets.get_orders(symbol="ETH")

# print (json.dumps(orders))


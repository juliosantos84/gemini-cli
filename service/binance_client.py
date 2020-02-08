from binance.client import Client
import os
import json

ALT_PAIRS = {
    'ETH': ['XRPETH','XLMETH','BATETH'],
    'BTC': ['XRPBTC','XLMBTC','BATBTC']
}

class BinanceClient():
    def __init__(
        self, 
        api_key=os.getenv("BINANCE_API_KEY"),
        api_secret=os.getenv("BINANCE_API_SECRET")):
        self._client = Client(api_key, api_secret)

    def get_orders(self, symbol):
        all_orders = self._client.get_all_orders(symbol=symbol)
        orders = []
        for order in all_orders:
            if order['status'] == "FILLED":
                orders.append(order)
        return orders

    def get_base_pair(self, symbol):
        return symbol[:3]

    def get_base_pair_total(self, base_pair):
        alt_pairs = ALT_PAIRS[base_pair] if base_pair in ALT_PAIRS else None
        # print (alt_pairs)
        total = 0.0
        if alt_pairs is not None:
            for pair in alt_pairs:
                orders = self.get_orders(pair)
                for order in orders:
                    total += float(order['origQty']) * float(order['price'])
        return total




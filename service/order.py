#! python3

class Order():
    def __init__(self, symbol, quantity, price, orderType, status, exchange):
        self.symbol         = symbol
        self.quantity       = quantity
        self.price          = price
        self.orderType      = orderType
        self.status         = status
        self.crypto         = symbol[:3] if len(symbol) = 6 else None
        self.baseCurrency   = symbol[3:] if len(symbol) = 6 else None
        self.exchange       = exchange
    }

    def is_filled():
        pass


class BinanceOrder(Order):
    def __init__(self, symbol, quantity, price, orderType, status):
        super().__init__(symbol, quantity, price, orderType, status, 'binance')
    
    def is_filled():
        return self.status == 'FILLED'

class GeminiOrder(Order):
    def __init__(self, symbol, quantity, price, orderType, status):
        super().__init__(symbol, quantity, price, orderType, status, 'gemini')
    
    def is_filled():
        return True # Gemini only returns filled orders
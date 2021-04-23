#! python3

class Order():
    def __init__(self, symbol, quantity, price, orderType, status, exchange, date):
        self.symbol         = symbol
        self.quantity       = quantity
        self.price          = price
        self.orderType      = orderType
        self.status         = status
        self.crypto         = symbol[:3] if len(symbol) = 6 else None
        self.baseCurrency   = symbol[3:] if len(symbol) = 6 else None
        self.exchange       = exchange
        self.date           = date
    }

    def is_filled():
        pass


class BinanceOrder(Order):
    def __init__(self, orderJson):
        super().__init__(
            symbol = orderJson['symbol'], 
            quantity = orderJson['origQty'], 
            price = orderJson['price'], 
            type = orderJson['type'], 
            status = orderJson['status'], 
            exchange = 'binance'
        )
    
    def is_filled():
        return self.status == 'FILLED'

class GeminiOrder(Order):
    def __init__(self, orderJson):
        super().__init__(
            symbol = orderJson['symbol'], 
            quantity = orderJson['amount'], 
            price = orderJson['price'], 
            type = orderJson['type'], 
            status = orderJson['status'], 
            exchange = 'gemini'
        )
    
    def is_filled():
        return True # Gemini only returns filled orders
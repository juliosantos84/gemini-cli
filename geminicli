# Run using `python geminicli [option]`

from service import TradeHistoryService
from service import OrderService
import sys
import argparse
import json

SYMBOLS = [
    'BTCUSD', 
    'ETHUSD', 
    'LTCUSD', 
    'ZECUSD', 
    'FILUSD', 
    'LINKUSD', 
    'BATUSD', 
    'MKRUSD', 
    'AAVEUSD', 
    'YFIUSD', 
    '1INCHUSD',
    'COMPUSD',
    'MATICUSD',
    # Added 1/29/2022
    'MANAUSD',
    'UNIUSD',
    'LUNAUSD',
    'AXSUSD',
    'AMPUSD',
    'LRCUSD',
    'ENSUSD',


]

parser = argparse.ArgumentParser(
    prog        = 'geminicli',
    description = 'Connects to gemini and binance to print investment info.\n'
                  'Configure:\n\n'
                  'GEMINI_AUDITOR_API_KEY\n\n'
                  'GEMINI_AUDITOR_API_SECRET,\n\n'
                  'BINANCE_API_KEY\n\n'
                  'BINANCE_API_SECRET\n\n')
parser.add_argument('command', type=str, default="summary", choices=['summary','buy', 'list'])
parser.add_argument('-s', '--symbol', type=str, default='BTCUSD')
parser.add_argument('-l', '--symbol-list', dest='symbol_list', nargs='+', type=str, default=SYMBOLS)
parser.add_argument('-a', '--amount', type=float, default=5.00)
parser.add_argument('-p', '--price', type=float, default=7400)
parser.add_argument('-r', '--subtract-alts', action="store_true")
args = parser.parse_args()


if args.command == 'summary':
    th = TradeHistoryService()
    th.print_investment_summary(symbols=args.symbol_list, subtract_alts=args.subtract_alts)
elif args.command == 'buy':
    o = OrderService()
    print ("Buying $%f of %s @ %f " % (args.amount, args.symbol, args.price))
    order = o.buy(symbol=args.symbol, amount=args.amount, price=args.price)
    json.dumps(order)
    
elif args.command == 'list':
    o = OrderService()
    o.list_prices()

from service import TradeHistoryService
from service import OrderService
import sys
import argparse
import json

parser = argparse.ArgumentParser(
    prog        = 'gemini-cli',
    description = '')
parser.add_argument('command', type=str, default="summary", choices=['summary','buy', 'list'])
parser.add_argument('-s', '--symbol', type=str, default='BTCUSD')
parser.add_argument('-a', '--amount', type=float, default=5.00)
parser.add_argument('-p', '--price', type=float, default=7400)
args = parser.parse_args()

th = TradeHistoryService()
o = OrderService()

if args.command == 'summary':
    th.print_investment_summary(['BTCUSD','ETHUSD', 'ZECUSD', 'LTCUSD'])
elif args.command == 'buy':
    print ("Buying $%f of %s @ %f " % (args.amount, args.symbol, args.price))
    order = o.buy(symbol=args.symbol, amount=str(args.amount), price=str(args.price))
    json.dumps(order)
    
elif args.command == 'list':
    o.list_prices()
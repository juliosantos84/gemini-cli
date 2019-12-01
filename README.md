# gemini-cli

## setup
- Configure API secrets
```bash
export AUDITOR_API_KEY="GEMINI_API_KEY"
export AUDITOR_API_SECRET="GEMINI_API_SECRET"
```

## operations

### trade_history

Use `print_investment_summary(['BTCUSD','ETHUSD', 'ZECUSD', 'LTCUSD'])` to retrieve an investment summary:
```bash
BTCUSD: 318.438659 @ $6226.876005
ETHUSD: 578.725639 @ $231.782748
ZECUSD: 404.994400 @ $103.395255
LTCUSD: 526.968916 @ $93.806625
```


```json
{
   "price":"7557.00",
   "amount":"0.02644552",
   "timestamp":1575154596,
   "timestampms":1575154596795,
   "type":"Buy",
   "aggressor":false,
   "fee_currency":"USD",
   "fee_amount":"0.4996219866",
   "tid":8983847321,
   "order_id":"8983511810",
   "exchange":"gemini",
   "is_auction_fill":false
}
```
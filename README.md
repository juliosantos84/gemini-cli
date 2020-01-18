# gemini-cli

## setup
1. create a virtual environment
```bash
virtualenv -p <PATH_TO_PYTHON3> .gemini-cli && source .gemini-cli/bin/activate
```
1. install requirements
```bash
pip3 install -r requirements.txt
```
- Configure API secrets
```bash
export AUDITOR_API_KEY="GEMINI_API_KEY"
export AUDITOR_API_SECRET="GEMINI_API_SECRET"
```
1. Update geminicli to use the python3 installed by virtualenv:
```bash
#! /Users/julio/Development/gemini-cli/.gemini/bin/python3
```
1. Add gemini-cli project folder to your path, i.e.
```bash
export PATH="/Users/julio/Development/gemini-cli:$PATH"
```

## usage

### trade summary

Use `geminicli summary` to retrieve an investment summary:
```bash
SYMBOL      PRINCIPAL    AMOUNT    AVG PRICE    LAST PRICE    CUR VALUE    GAIN/LOSS    BRK EVEN
--------  -----------  --------  -----------  ------------  -----------  -----------  ----------
BTCUSD        4704.1     0.5658    9039.92         8915.23     4247.5          0.4     1076.08
ETHUSD        1404.8    16.9855     223.029         176.22     3090.8       -706.06     224.743
ZECUSD        1404.99   13.4705     103.395          53.39      719.192     -685.803    104.301
LTCUSD        1526.97   16.1739      93.8066         60.02      970.755     -556.214     94.4097
TOTAL         8432.9     0            0               0        5028.3        595.34       0
```

## reference
### trade
```json
# trade
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
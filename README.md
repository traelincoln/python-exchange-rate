# Description  
Get foreign currency exchange rates on the command line

# Usage   
```bash
$ python3 rate.py currency_from currency_to exchange_amount
```

# Example
## Input
``` bash
$ python3 rate.py zar usd 1000000
```
## Output
```bash
$ From            To              Amount          Cash  
  ZAR     1       USD     0.05    1,000,000.00    52,763.43
```
# TOD0 
- Get the correct ZWL rate from www.rbz.co.zw  
- Allow for multiple input exchange rates and amounts  
- Write tests

# Data sources
Credit: [fawazahmed0/currency-api on Github](https://github.com/fawazahmed0/currency-api)

## CDN links
- <https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd.min.json>  
- <https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd.json>

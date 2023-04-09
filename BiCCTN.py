import ccxt

binance = ccxt.binance({
    'timeout': 30000, 
    'rateLimit': 1000,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future',
        'urls': {
            'api': 'https://fapi.binance.com',
        },
    },
    'apiKey': 'rMzlGI5cA9o2KibCF6nNHxeiaXwuofdMXnP9s7I6IQqokKga3Kl9P138pszzEieU',
    'secret': 'lfXmYuHoogld6fD32OkXabQsOAjrugmwvKGtUuFBVnNBCdl79L68cwNSMlZ4mk2d',
    
    })


# ticker = binance.fetch_ticker('BTC/USDT')
# print(ticker)    
# print(binance.fetch_balance()) 

balance = binance.fetch_balance()

print(balance['total'])

# for asset in balance['total']:
#     amount = balance['total'][asset]
#     if amount > 0:
#         print(f"{asset}: {amount}")








##### kraken api #####

# import ccxt

# exchange = ccxt.kraken()
# symbol = 'BTC/USD'

# ticker = exchange.fetch_ticker(symbol)
# price = ticker['last']

# print(f"Current {symbol} price on {exchange.name} is: {price}")

### end kraken api ###
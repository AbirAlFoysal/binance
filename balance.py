import ccxt

#### tesnet
# api_key = 'xTW1tLVDOQb96mnvmUflQLJAowwuQxtXAb58pXUbFibwB7TIk7RdgspfHlXsnSgv'
# secret_key = 'SFb19A2nXaCNTSHJNhGfqMKa6iUXEaqolOAVZpHRLoqOodfpwhWkSeXdf6hpwNQa'

#### second:
# apiKey: 'xTW1tLVDOQb96mnvmUflQLJAowwuQxtXAb58pXUbFibwB7TIk7RdgspfHlXsnSgv'
# secret: 'SFb19A2nXaCNTSHJNhGfqMKa6iUXEaqolOAVZpHRLoqOodfpwhWkSeXdf6hpwNQa'
   
#### first
api_key = 'rMzlGI5cA9o2KibCF6nNHxeiaXwuofdMXnP9s7I6IQqokKga3Kl9P138pszzEieU'
secret_key = 'lfXmYuHoogld6fD32OkXabQsOAjrugmwvKGtUuFBVnNBCdl79L68cwNSMlZ4mk2d'

exchange = ccxt.binance({
    'apiKey': api_key,
    'secret': secret_key,
    # 'enableRateLimit': True,
    # 'test': True,
    # 'timeout': 3000,
    # 'spot': True,
    # 'options': {
    #     'defaultType': 'future',
    # },
})

# fetch account balance
balance = exchange.fetch_balance()

usdt_balance = balance['total']['USDT']
print(f"Your testnet account balance is: {usdt_balance} USDT")



# api_key = 'rMzlGI5cA9o2KibCF6nNHxeiaXwuofdMXnP9s7I6IQqokKga3Kl9P138pszzEieU'
# secret_key = 'lfXmYuHoogld6fD32OkXabQsOAjrugmwvKGtUuFBVnNBCdl79L68cwNSMlZ4mk2d'
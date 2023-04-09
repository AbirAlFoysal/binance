import ccxt
import time
import pandas as pd

binance = ccxt.binance({
    'apiKey': 'rMzlGI5cA9o2KibCF6nNHxeiaXwuofdMXnP9s7I6IQqokKga3Kl9P138pszzEieU',
    'secret': 'lfXmYuHoogld6fD32OkXabQsOAjrugmwvKGtUuFBVnNBCdl79L68cwNSMlZ4mk2d',
})

def trading_strategy():
    ohlcv = binance.fetch_ohlcv('BTC/USDT', '1h')
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)

    short_ma = df['close'].rolling(window=20).mean()
    long_ma = df['close'].rolling(window=50).mean()
    
    # Determine buy/sell signals
    if short_ma.iloc[-1] > long_ma.iloc[-1] and short_ma.iloc[-2] <= long_ma.iloc[-2]:
        # Buy signal
        order = binance.create_order('BTC/USDT', 'market', 'buy', 0.001)
        print(f"Bought BTC at {order['price']}")
    elif short_ma.iloc[-1] < long_ma.iloc[-1] and short_ma.iloc[-2] >= long_ma.iloc[-2]:
        # Sell signal
        order = binance.create_order('BTC/USDT', 'market', 'sell', 0.001)
        print(f"Sold BTC at {order['price']}")



# Fetch market data
ohlcv = binance.fetch_ohlcv('BTC/USDT', '1h')
df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')


# Place orders
order = binance.create_order('BTC/USDT', 'limit', 'buy', 0.001, 60000)

# Check account balance
balance = binance.fetch_balance()['USDT']['free']
print(f"Current balance: {balance}")

while True:

    trading_strategy()
    time.sleep(1)

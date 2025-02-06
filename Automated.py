import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ticker = "AAPL" # Apple stock
start_date = "2010-01-01"
end_date = "2024-01-01"

# gather stock data
data = yf.download(ticker, start=start_date, end=end_date)
# this downloads their range from the stock data

# display few rows
print(data.head())

short_window = 50 # Short-term SMA = simple moving average
long_window = 200 # long term SMA

data['SMA50'] = data['Close'].rolling(window=short_window).mean()
data['SMA200'] = data['Close'].rolling(window=long_window).mean()
# this will compute the averages

data['Signal'] = 0
# Buy
data.loc[data['SMA50'] > data['SMA200'], 'Signal'] = 1
# Sell
data.loc[data['SMA50'] < data['SMA200'], 'Signal'] = -1
# It will update with 1 buy and -1 for sell

# Simulating trades
data['Position'] = data['Signal'].shift(1)
# Under this comment the code will calculate the % change daily
data['Daily Return'] = data['Close'].pct_change()
# Calculate the returns now through strategy
data['Strategy Return'] = data['Position'] * data['Daily Return']
# Calculate cumulative returns
data['Cumulative Market Return'] = (1 + data['Daily Return']).cumprod()
data['Cumulative Strategy Return'] = (1 + data['Strategy Return']).cumprod()

# GRAPH VISUALIZER
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price', alpha=0.5)
plt.plot(data['SMA50'], label='SMA50', alpha=0.75)
plt.plot(data['SMA200'], label='SMA200', alpha=0.75)
plt.title(f"{ticker} Price and Moving Averages")
plt.legend()
plt.show()
# this helps identify buy/sell zones when SMA50 crosses above or below SMA200
# this will compare how the strategy performs against holding the stock without any activity trading strategy

total_start_return = data['Cumulative Strategy Return'].iloc[-1] - 1
total_market_return = data['Cumulative Market Return'].iloc[-1] - 1
# This is going to measure the profitability of trading strategy against buy-and-hold
# it helps evaluate how well it performs historically
print(f"Total Strategy Return: {total_start_return:.2%}")
print(f"Total Market Return: {total_market_return:.2%}")


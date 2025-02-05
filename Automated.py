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

data['SMA50'] =
data['Close']

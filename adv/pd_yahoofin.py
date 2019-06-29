#Stock Prices
#-----------------------------
#%
#pip install pandas_datareader
pip install pandas.io.data
#restart kernel
from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd

#
# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
tickers = ['AAPL', 'MSFT', '^GSPC']

# We would like all available data from startdate until enddate
start_date = '2019-06-01'
end_date = '2019-06-30'

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
panel_data = data.DataReader('INPX', 'google', start_date, end_date)

panel_data.to_frame().head(9)

import pandas_datareader as pdr
from datetime import datetime

ibm = pdr.get_data_yahoo(symbols='IBM', start=datetime(2000, 1, 1), end=datetime(2012, 1, 1))
print(ibm['Adj Close'])



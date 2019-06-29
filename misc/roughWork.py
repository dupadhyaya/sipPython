#Rough Work
#-----------------------------
#%

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

#%%
#https://pypi.org/project/yahoo-finance/
pip install yahoo-finance
import yahoo-finance

from yahoo_finance import Share
yahoo = Share('YHOO')
yahoo.get_price()
>>> print yahoo.get_open()
yahoo_finance.Share("SBI.NSE")
symbol = yahoo_finance.Share("GOOG")
google_data = symbol.get_historical("2019-06-01", "2019-06-30")
google_df = pd.DataFrame(google_data)

# Output data into CSV
google_df.to_csv("/home/username/google_stock_data.csv")

#
pip install yahoofinancials
from yahoofinancials import YahooFinancials

tech_stocks = ['AAPL', 'MSFT', 'INTC']
bank_stocks = ['WFC', 'BAC', 'C']
yahoo_financials_tech = YahooFinancials(tech_stocks)
yahoo_financials_banks = YahooFinancials(bank_stocks)
yahoo_financials_tech
ech_cash_flow_data_an = yahoo_financials_tech.get_financial_stmts('annual', 'cash')
bank_cash_flow_data_an = yahoo_financials_banks.get_financial_stmts('annual', 'cash')
banks_net_ebit = yahoo_financials_banks.get_ebit()
tech_stock_price_data = yahoo_financials_tech.get_stock_price_data()
daily_bank_stock_prices = yahoo_financials_banks.get_historical_price_data('2008-09-15', '2018-09-15', 'daily')
daily_bank_stock_prices
#https://pypi.org/project/yahoofinancials/

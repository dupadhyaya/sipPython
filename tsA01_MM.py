#Date Time - MM
#-----------------------------
#%

#datetime
from datetime import datetime
datetime(year=2019, month=1, day=31)

# Parser
from dateutil import parser
parser.parse('14th July 2019 0730 pm')

#Numpy
import numpy as np
date1 = np.array('2019-07-01', dtype=np.datetime64)
#note 07 and 01
date1 + 1
date1 + [1,2,3]
date1 + np.array([5,10,11])
date1 + np.arange(12)
#another way
np.datetime64('2019-07-10')
np.datetime64('2019-07-10 13:00')

#%%%
#Pandas Date Time
import pandas as pd
date2 = pd.to_datetime('11th July 2019')
date2
#vectorised ops
date2 + 1  #will not work
date2 + np.arange(12) #this will also not work
date2 + pd.to_timedelta(np.arange(12))  #not correct
date2 + pd.to_timedelta(np.arange(12), 'D') # daily interval
date2 + pd.to_timedelta(np.arange(12), 'M') # month interval

#
#index by time
np.random.seed(1234)
attendance = np.random.randint(25,50, size=180)
np.mean(attendance) #37.63
startDate = pd.to_datetime('01 Aug 2019')
startDate
indexvalues = startDate + pd.to_timedelta(np.arange(180), 'D')
indexvalues
data1 = pd.Series(attendance, index=indexvalues)
data1
data1.head()
data1.head(2).append(data1.tail(3))  #heads-2, tails-3
#
data1['2020']  #filter
data1['2019-10'] 
data1['2019-10-01':'2019-12-25']  #between certain dates
data1[data1.index.dayofweek == 2] #2nd day of week


#----------
#Parsing a series of Dates with different dates 
dates3 = pd.to_datetime([ datetime(2019,7,10), '11th July 2019','2019-7-15', '2019-07-20', '18-07-2019']) 
dates3

#convert to periods index : not much use here
dates3.to_period('D')
dates3.to_period('M')
dates3.to_period('Y')

#difference in dates
datetime.today() - dates3[0]
datetime.today() - dates3[3]


#pandas sequence
pd.date_range('2019-07-01', '2019-10-30')

pd.date_range('2019-07-01', periods=45)
pd.date_range('2019-07-01', periods=3, freq='M')
pd.date_range('2019-07-01', periods=5, freq='H')

#%%%
#

#%%%
pd.timedelta_range(0, periods=9, freq='2H20T')

#business day offser
from pandas.tseries.offsets import BDay
pd.date_range('2019-07-01', periods=9, freq=BDay())
#see the gap in days - Sat & SUn

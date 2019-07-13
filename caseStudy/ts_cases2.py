#Time Series - SIP
#-----------------------------
#%
#program started for Business Days from 15 Jun to 28 Jul

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

classDate = pd.date_range('2019-06-15', '2019-07-28', freq='B')
type(classDate)
len(classDate)
classDate.strftime('%a')  #day of class
#all are between Mon to Fri
random.seed(1234)
attendance1 = np.random.randint(low=25,high=50, size=30)
np.mean(attendance1)
#%%%
workshop1 = pd.DataFrame({'attendance1':attendance1, 'days' : classDate.strftime( '%a') }, index=classDate)
workshop1.head(3).append(workshop1.tail(2))
workshop1.describe()
workshop1.dtypes
#make days as categories
workshop1.days = workshop1.days.astype('category', ordered=True)
#depreciated - days should be in order
workshop1.days

#New in version 0.23.0
from pandas.api.types import CategoricalDtype
dayCat_type = CategoricalDtype(categories=['Mon', 'Tue', 'Wed', 'Thu','Fri'], ordered=True)
workshop1.days = workshop1.days.astype(dayCat_type)
workshop1.days
#now it is better
#%%%
#lets plot first
workshop1.attendance1.plot(figsize=(10,5)) 
#only on those days where attendance was taken
#Sat and Sun was off
workshop1.asfreq('D').plot(figsize=(10,5))
#with gaps - blanks 
#fill these gaps : only 1,2 ahead ffill
workshop1.asfreq('D').attendance1.fillna(method='ffill', limit=1)
workshop1.asfreq('D').attendance1.fillna(method='ffill', limit=2)
#fill only 1 value or 2 next 

#original data - group by Days 
#average attendance on Mondays, Tues, 
workshop1.head()
from pandas import Grouper
workshop1.groupby(['days', pd.Grouper(freq='M')])['attendance1' ].mean()
#all mondays on month; find their mean day wise
workshop1.groupby(['days', pd.Grouper(freq='W')])['attendance1'].mean()
#all mondays on week; find their mean day wise
workshop1.groupby(['days', pd.Grouper(freq='D')])['attendance1'].mean()

#same as original data - full year
workshop1.groupby(['days', pd.Grouper(freq='A')])['attendance1'].mean()
workshop1.groupby('days').mean()
workshop1

#Moving average
workshop1.head(5)
workshop1.attendance1[0:3].sum()/3
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rolling.html    
(40+49+37)/3, (49+37+39)/3
workshop1['attendance1'].rolling(3).mean().head(5)
ma1 = workshop1.rolling(5, win_type='triang').mean()
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.rolling.html
ma1  #moving average over 5 day period
#plot it
ma1.plot(color='black', linewidth=1.5, marker='', figsize=(8, 4), label='Moving Average Attenance 5 Day Period')

#using MPL 
fig, ax = plt.subplots(figsize=(8,4))
ma1.plot(ax=ax)
workshop1.attendance1.plot(ax=ax)
xs = workshop1.index
ys = workshop1.attendance1
y1s = ma1.attendance1
for x,y in zip(xs,ys):
    label = "{:d}".format(y)
    plt.annotate(label, (x,y), textcoords="offset points",          xytext =(3,2),  ha='center', color ='red', size=12) #
for x,y in zip(xs,y1s):
    plt.annotate("{:.0f}".format(y), (x,y), color='blue', size=10) 
fig.text(0.7, 0.8, r'Attendance Rolling Plot', ha="center", va="bottom", size="medium",color="blue")
ax.set_title("Time Series Plot")
plt.show();
    
#https://www.programiz.com/python-programming/methods/built-in/format
#%%
#attendance of multiple classes
random.seed(1234)
attend2 = np.random.randint(low=25,high=40, size=(100,3))
attend2
dates2 = pd.date_range('2019-06-15', periods=100, freq='B')
random.seed(1234)
import random
classType = random.choices(['Theory','Tutorial', 'Practical'], k=100)
classType
workshop2 = pd.DataFrame(attend2, index=dates2)
#not able to add another column classType
workshop2
workshop2['classType'] = classType
workshop2.columns=(["BBA", "MBA", "BTECH",'classType'])
workshop2.head()
#categories no order
workshop2.classType = workshop2.classType.astype('category')
workshop2.describe(include='all')
workshop2.dtypes

#%%%

#plot
workshop2.plot(figsize=(10,5))
workshop2[['BBA','MBA','BTECH']].plot(figsize=(10,5))
workshop2.plot.scatter(x='MBA', y='BBA', c='DarkBlue')

workshop2['BBA'].plot()
workshop2['MBA'].plot()

#different plots from different columns
cols_plot = ['BBA', 'MBA', 'BTECH']
axes = workshop2[cols_plot].plot(marker='.', alpha=0.8, linestyle='None', figsize=(11, 9), subplots=True)
for ax in axes:    ax.set_ylabel('Daily Attendance')
# Line
axes = workshop2[cols_plot].plot(marker='.', alpha=0.8, figsize=(11, 9), subplots=True, linestyle='-')
for ax in axes:    ax.set_ylabel('Daily Attendance')
#ax.text('2019-09-1', 30, "New Year's Day")
ax.text('2019-09-1', 30, "New Year's Day")


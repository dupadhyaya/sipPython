#Date Time - Operations & Arithmetic
#-----------------------------
#%

from datetime import datetime as dt

#to date from integer values
new_date = dt(2019,7,4)
new_date

equinoxDate = dt(2019,6,23)
equinoxDate

#%%

d1 = dt(2019,6,15)
d2 = dt(2019,7,28)
d2 + d1 #error
d2 - d1  #number of days


#%%
d3 = dt(2019, 7, 4, 15, 30, 59, 10)
d3
d3.hour   #hour
d3.minute #minute
d3.second  #second
d3.microsecond #microsecond
d3.tzinfo  #no info store in environment


#time instance
datetime.time.min
datetime.time.max
datetime.time.resolution

#Date parts
today = datetime.date.today()
today
today.ctime()
today.timetuple()
today.toordinal()
today.year
today.month
today.day


#time
import time
time.time()
time.localtime()

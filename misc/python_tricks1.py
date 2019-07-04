#Panda Tricks
#-----------------------------
#%
#https://realpython.com/python-pandas-tricks/
import pandas.util.testing as tm
tm.N, tm.K = 15, 3  # Module-level default rows/columns

dir(tm)

import numpy as np
np.random.seed(444)

t1 = tm.makeTimeDataFrame(freq='M')
t1.head()

t2 =tm.makeDataFrame()
t2


#date time
from itertools import product
datecols = ['year', 'month', 'day']

df = pd.DataFrame(list(product([2017, 2016], [1, 2], [1, 2, 3])),  columns=datecols)
df['data'] = np.random.randn(len(df))
df

df.index = pd.to_datetime(df[datecols])
df.head()
df = df.drop(datecols, axis=1).squeeze()
df.head

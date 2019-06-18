# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 06:28:03 2017 by Dhiraj Upadhyaya
"""
#Student Data 
import pandas as pd
from datetime import datetime
from dateutil.parser import parse

df = pd.read_csv('dsstudents.csv')
df
df.columns
df.dob
df['dob'].describe()
df['course'].describe()



#Date Column - Calculate Age
today = datetime.date.today() 
today
dob1 = datetime.datetime.strptime(df.dob, "%d-%b-%y").date()



dob1 = pd.to_datetime(df.dob)
type(dob1)
dob1
dob2 = [datetime.datetime.strptime(x, '%d-%b-%y') for x in df.dob]
type(dob2)
dob2
dob3 = [parse(x) for x in df.dob]
type(dob3)
dob3

#Diff
diffdays = (today - dob1)
age = diffdays/365
age
age.dt.days
import numpy as np
(age / np.timedelta64(1, 'D')).astype(int)
pd.to_timedelta(age)
#Age
df['age'] = age.dt.days
df
df.columns

df.describe()
df.drop(df.index[2], inplace=True)
df
#df = df.drop([5]).reset_index(drop=True)
df.index = range(len(df))
df

df.to_csv('dsstudents2.csv')
df.count()
#CSV file formated and saved

df2 = pd.read_csv('dsstudents2.csv')
df2
pd.Factors

# -*- coding: utf-8 -*-
#index ing python pandas

#single index
import pandas as pd
import numpy as np


#data 
df7 = pd.read_csv('data/mtcars.csv')
df7.head()
df7.columns
df7.describe
df7.dtypes
#convert selected columns to category
df7.columns
catcolumns1 = ['cyl', 'vs', 'am', 'gear', 'carb']
catcolumns1

#%%
#create index with carname ; first keep a column with names also
df7['car'] = df.carname
df7 = df.set_index('carname')
df7

df7[catcolumns1] = df7[catcolumns1].astype('category')
df7.dtypes

df7.describe()
df7[catcolumns1].describe()
df7.columns

df7.describe(include='all')


df7.index

#multiple index
df7b = pd.read_csv('data/mtcars.csv')
df7b.head()
df7b.columns
df7b.dtypes
df7b.index # 0 to 31 with gap of 1

#access with index number
df7b.loc[1]
df7b.loc[0:2]

df7c = df7b.set_index('cyl')
df7c

df7d = df7b.set_index(['cyl','gear','am'])
df7d

#grouping using Index
df7d.groupby(['cyl','am'])['wt'].mean()

df7d.unstack()  #error duplicate entries

df7d.index

#Missing Values
#-----------------------------
#%

#handling missing values
#find, row, col, total, 
#import, 
#handle, replace (techniques)

# import the pandas library
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(40,100, size=(5, 3)), index=['Rahul', 'Tanisha', 'Vijay', 'Hitesh', 'Priyanka'],columns=['HR', 'MM', 'Stats'])
df
#add blank rows by adding indexes - b, d, g
df = df.reindex(['Saksham','Rahul', 'Pooja','Tanisha','Arunabh', 'Vijay','Rakhi', 'Hitesh', 'Priyanka','Yash'])
df
#Using reindexing, we have created a DataFrame with missing values. In the output, NaN means Not a Number.

#o make detecting missing values easier (and across different array dtypes), Pandas provides the isnull() and notnull() functions, which are also methods on Series and DataFrame objects 
df.isnull()  #cell wise 
df.notnull()

df.isna() 
df.isna() == df.isnull()

#
df
df.HR.isnull()
df.MM.isnull().sum()  #how many missing
df.isnull().sum() 

#filling missing values
df.HR.fillna(0, inplace=True)
df  #set column one

df.fillna(99)  #only show not replaced
df.fillna(99).isnull().sum()  #no missing values now


#filling missing values fwd / reverse left / right
#Fill NA Forward and Backward
#pad/fill- Fill methods Forward
#bfill/backfill- Fill methods Backward
df
df.fillna(method='pad') #same column, fill fwd (first row is not filled)
df.fillna(method='backfill')  #yash is left out

#drop missing values
df.dropna()
df.dropna(axis=0)  #keep only complete rows
df
df.dropna(axis=1) #col which is complete

df
#replace generic values
df2 = pd.DataFrame({'subject1':[10,20,30,40,50,2000], 'subject2':[1000,0,30,40,50,60]})
df2 #these values of 1000 and 2000 are not correct

df2.replace({1000:10,2000:60})

assert pd.isnull(df2).all().all()

#%%
df
df.describe()
df.info()
#%%
df['MM']
df['MM'].replace(np.nan, 0)  #replace missing values with 0
#or vice versa
df['MM'].replace(np.nan, 0, inplace=True)
df
df['MM'].replace(0, np.nan, inplace=True)  #0 may mean missing
df

#%%%
#arithmetic on missing values
df.HR.mean()
df.MM.mean()  #R does not allow this. na.rm=T required
df
meanMM = df.MM.mean()
meanMM
df['MM'] = df.MM.fillna(10,inplace=True)
df['MM'] = df['MM'].fillna(meanMM, inplace=True)
df
data_name[‘column_name’].replace(0, np.nan, inplace= True)
#%%%

import numpy
dataset = read_csv('pima-indians-diabetes.csv', header=None)
# mark zero values as missing or NaN
dataset[[1,2,3,4,5]] = dataset[[1,2,3,4,5]].replace(0, numpy.NaN)
# count the number of NaN values in each column
print(dataset.isnull().sum())










#https://machinelearningmastery.com/handle-missing-data-python/
#https://www.tutorialspoint.com/python_pandas/python_pandas_missing_data.htm




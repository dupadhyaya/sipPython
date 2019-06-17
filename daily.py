# -*- coding: utf-8 -*-
"Daily Practise File
#-----------------------------
#Data Structures

#List - ordered collection of items, mutable
list1 = [1,2,3,4,5]
list1
type(list1)



list2 = ['a','c','d','e']

#%%
#tuple - multiple type of objects, immutable
tuple1 = (1,2, 'a', 'b')
tuple1
type(tuple1)

#%%
#Dictionary - key-value pairs
dict1 = {1:'Ramesh', 2:'Suresh', 3:'Priyanka'}
dict1
type(dict1)

#%%
#Set - ordered collection of simple items, immutable
set1 = set(['india', 'pakistan', 'england', 'australia','india'])
set1
type(set1)



#%%
#Strings

str1 = 'Python Programming'
type(str1)


#%%
#sequence - tuple and list are used
list1
for i in list1:
    print(i)
tuple1
for i in tuple1:
    print(i)
for i in range(1, 10, 2):
    print(i, end=' ')
    
#%%
#frozen set- accepts iterable object as input parameter.
tupleFZ1 = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
type(tupleFZ1)  

# converting tuple to frozenset 
frozenset1 = frozenset(tupleFZ1) 
frozenset1
type(frozenset1)

dict1
frozenset2 = frozenset(dict1)
type(frozenset2)
frozenset2
#keys of dictionary made as frozen set

#%%
#zip - map the similar index of multiple containers 
# initializing lists 
name = [ "Dhiraj", "Kounal", "Akhil", "Pooja" ] 
rollno = [ 4, 1, 3, 2 ] 
marks = [ 90, 50, 60, 70 ] 
# using zip() to map values 
mapped = zip(name, rollno, marks) 
# converting values to print as set 
mapped = set(mapped) 
mapped
namez, rollnoz, marksz = zip(*mapped)
namez


#%%
#numpy - array - same data type
import numpy as np
np1 = np.arange(1,10)
np1
type(np1)
np?
np2 = np.array([ 90, 50, 60, 70 ])
np2
np.sort(np2)

np3 = np.array([[1,4],[3,1]])
np3
np3.shape

#%%
#pandas - dataframe, excel like
#https://mode.com/python-tutorial/pandas-dataframe/
import pandas as pd
pd?
df1 = pd.DataFrame({'rollno':[1,2,3,4], 'name': [ "Dhiraj", "Kounal", "Akhil", "Pooja" ], 'marks':[ 40, 50, 60, 70 ], 'gender':['M','M','M','F']})
df1
type(df1) 

df1.columns
df1.describe
df1.dtypes
df1.shape
df1.groupby('gender').size()
df1.groupby('gender')['marks'].mean()
df1.groupby('gender').aggregate({'marks': [np.mean, 'max']})

#%%
#Graphs https://python-graph-gallery.com/
import matplotlib.pyplot as plt
#https://matplotlib.org/
df1.groupby('gender').size().plot(kind='bar')

#https://seaborn.pydata.org/index.html
import seaborn as sns
# sns.set(style="ticks", color_codes=True)
iris = sns.load_dataset("iris")
sns.pairplot(iris)


#%%
#Load Inbuilt Datasets
import statsmodels.api as sm
#https://vincentarelbundock.github.io/Rdatasets/datasets.html
mtcars = sm.datasets.get_rdataset(dataname='mtcars', package='datasets')
mtcars.data.head()

#%%
#Load from Excel/ CSV and export to
data = mtcars.data
data.head()

data.to_csv('exportcsv1.csv')
data.to_excel('exportexcel1.xlsx','sheet1', header=False)

#load from CSV and Excel
data2a = pd.read_csv('exportcsv1.csv')
data2a.head()

data2b = pd.read_excel('exportexcel1.xlsx','sheet1')
data2b.head()

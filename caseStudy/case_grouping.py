#Practise in Class
#-----------------------------
#%
#Groupby, Pivot Table, Cross Tab, 
#Time Series, TS Plot, Moving Average, Stock Market Data Download
#ARIMA forecasting

#Groupings and Total
#create a dataframe with 3 category columns and two numeric, one rollno
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from collections import Counter
import seaborn as sns

#DF
rollno = np.arange(1, 101)
rollno

gender = random.choices(['M','F'], weights=(.7,.3), k=100)
gender.count('M')
Counter(gender)
len(gender)

course = random.choices(['BBA','MBA','BTECH'], weights=(.4,.3,.3), k=100)
Counter(course)

grade = random.choices(['A-','A+','A'], weights=(.4,.3,.3), k=100)
Counter(grade)

catscore = np.random.randint(60,99, size=100)
catscore

classXII = np.trunc(np.random.normal(loc=60, scale=10, size=100))
classXII

#join them
students = pd.DataFrame({'rollno':rollno, 'gender':gender,'course':course, 'grade':grade, 'catscore':catscore, 'classXII':classXII})
students
students.dtypes
#convert gender, course, grade to category
from pandas.api.types import CategoricalDtype
gradeCatType = CategoricalDtype(categories=["A+", "A", "A-"],ordered=True)
students['grade'] = students['grade'].astype(gradeCatType)
students[['course', 'gender']] = students[['course', 'gender']].astype('category') 
students.dtypes

#ready for analysis
students.groupby('gender').size()
students.gender.value_counts()
students.groupby(['gender','course']).size()
students.groupby(['gender','course']).aggregate({'rollno':'count'})
students.groupby(['gender','course']).aggregate({'rollno':'count', 'catscore':[np.mean,np.max], 'classXII':[np.max,np.min]})

students.groupby(['gender','course']).aggregate({'rollno':'count', 'catscore': {'MEANcat':np.mean,'MAXcat': np.max}, 'classXII': {'MAXxii': np.max, 'MINxii': np.min}})
#not {}, [] combinations ; dictionary type

students.groupby(['gender','course']).aggregate({'rollno':'count', 'catscore':np.mean, 'classXII':np.max}).unstack()

mapping = {'classXII': 'mean', 'catscore': 'max'}
students.groupby(['gender','course']).aggregate(mapping)

students[['classXII','catscore','gender','course']].groupby(['gender','course']).aggregate ( ['mean', np.median, np.max])
students.groupby(['gender','course']).agg({'rollno':'count'}).add_prefix('Count_')


#lets to similar things from pivot table 
#pivot_table, index, columns, values
students.pivot_table(index='gender', columns='course', values='rollno', aggfunc='count')
students.groupby(['gender','course']).size().unstack()

students.pivot_table(index='course', columns='gender', values='classXII', aggfunc=np.mean)

students.pivot_table(index=['course','grade'], columns='gender', values='classXII', aggfunc=np.mean, fill.value=0)
#see the order of grades : A+,A,A-; if no value, fill it with 0

aggfunc1 ={'classXII': np.mean, 'catscore': [min, max, np.mean]}
students.pivot_table(index=['course','grade'], columns='gender', values=['classXII','catscore'], aggfunc = aggfunc1)
#read more at https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot_table.html
#pandas.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All')
#%%%
#crosstab - used for factors
#pandas.crosstab(index, columns, values=None, rownames=None, colnames=None, aggfunc=None, margins=False, margins_name='All', dropna=True, normalize=False)
#https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.crosstab.html
#use columns
pd.crosstab(index=students['course'], columns=students['gender'])
students.groupby(['gender','course']).size().unstack()
students.pivot_table(index='gender', columns='course', values='rollno', aggfunc='count')
#------- more Xtab
pd.crosstab(index=students['course'], columns=students['gender'], margins=True)
pd.crosstab(index=students['course'], columns=students['gender'], margins=True, margins_name='Total Students')

#numeric summ also possible
pd.crosstab(index=students['course'], columns=students['gender'], values=students['classXII'], aggfunc='mean').round(0)


pd.crosstab(df.make, df.body_style, values=df.curb_weight, aggfunc='mean').round(0)
pd.crosstab(students.course, students.gender)
pd.crosstab(students.course, students.gender, normalize='columns')
#proportion in columns
pd.crosstab(students.course, students.gender, normalize='index')
#proportion in rows : .32 + .68 = 1.0

pd.crosstab(students.course, [students.gender, students.grade])
#count course-gender-grade - how many students
pd.crosstab(students.course, [students.gender, students.grade], rownames=['Course Type :'], colnames=['Gender Type :', "Grade Type :"],  dropna=False)


sns.heatmap(pd.crosstab(students.course, [students.gender, students.grade]),  cmap="YlGnBu", annot=True, cbar=False)
#more from here : https://pbpython.com/pandas-crosstab.html
#https://pbpython.com/images/crosstab_cheatsheet.png

students.columns
pd.crosstab(a, [b, c], rownames=['a'], colnames=['b', 'c'])


#groupby agg, pivot, xtab over
#lets reshape the data
students.head()
#melt-Unpivots” a DataFrame from wide format to long format, optionally leaving identifier variables set.
#pandas.melt(frame, id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None)
pd.melt(students, id_vars='rollno', value_vars=['catscore','classXII'], var_name='MarksCategory', value_name='marks')
#we don't want all columns
melt1 = pd.melt(students[['rollno', 'gender', 'catscore','classXII']], id_vars=['rollno', 'gender'], value_vars=['catscore','classXII'], var_name='MarksCategory', value_name='marks')
#another way
students.melt(id_vars=['rollno', 'gender'], value_vars=['catscore', 'classXII'], var_name='MarksCategory', value_name='marks')

melt1.groupby(['MarksCategory']).agg({'marks':np.mean})

#unmelt - index-col no change, columns- which should be transposed
#DataFrame.pivot(index=None, columns=None, values=None)[source]
#https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html
melt1.head()
melt1.pivot(index=['rollno','gender'], columns=['MarksCategory'], values='marks')
melt1.pivot(index='rollno', columns='MarksCategory', values='marks').head()
#get gender also
melt1.pivot_table(index=['rollno','gender'], columns='MarksCategory', values='marks').reset_index()


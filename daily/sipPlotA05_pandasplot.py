# -*- coding: utf-8 -*-
#Simple Plot
#-----------------------------
#%

import pandas as pd
import numpy as np



#numpy does not have plot; pandas has
studentcount = pd.Series([30, 25, 37])
studentcount.plot(kind='barh')

#Load Inbuilt Datasets
import statsmodels.api as sm
#https://vincentarelbundock.github.io/Rdatasets/datasets.html
mtcars = sm.datasets.get_rdataset(dataname='mtcars', package='datasets')
mtcars.data.head()
df = mtcars.data
#convert relevant columns to categories
catCols = ['cyl','gear', 'am','vs']
df['catCols'] = df['catCols'].astype('Category')
#use plot in pandas
df.mpg.plot()  #line
df.cyl.plot()  #line
df.cyl.value_counts().plot(kind='bar')

#here plot is method in pandas : no matplotlib used here
df.mpg.plot(kind='hist')

#other plots
#‘line’ : line plot (default)
#‘bar’ : vertical bar plot
#‘barh’ : horizontal bar plot
#‘hist’ : histogram
#‘box’ : boxplot
#‘kde’ : Kernel Density Estimation plot
#‘density’ : same as ‘kde’
#‘area’ : area plot
#‘pie’ : pie plot
#‘scatter’ : scatter plot
#‘hexbin’ : hexbin plot

df.cyl.value_counts().plot(kind='pie')
df.mpg.plot(kind='hist')
df[['mpg','cyl']].groupby('cyl').mean()
df[['mpg','cyl']].groupby('cyl').mean().plot(kind='barh')  #not correct
df[['mpg','cyl']].groupby('cyl').groups
#df[['mpg','cyl']].groupby('cyl').level(0)
df.groupby('cyl')['mpg'].plot(kind='hist' , legend=True)  # correct

df.mpg.plot(kind='box')
df.groupby('cyl')['mpg'].plot(kind='box')
df.groupby('cyl').size().plot(kind='area')

#scatter
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.scatter.html
df[['mpg', 'wt', 'cyl']].plot(kind='scatter', x='mpg', y='wt', c='cyl', legend=True)
pd.plotting?


#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html
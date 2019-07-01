#Panda Introduction and Topics
#-----------------------------
#%library
import pandas as pd
print(dir(pd), end =', ')
len(dir(pd))
#initial
#help
pd.read_csv?

#read from dataset
from pydataset import data
mtcars = data('mtcars')
mtcars.head()

#write to csv
mtcars.to_csv('data/mtcarsCSV.csv')

#read a csv/ excel
df = pd.read_csv('data/mtcarsCSV.csv')
df.shape
#should be able to read from CSV/ only data table

#create Panda Series


#create Pandas DF

#Groupy


#pandas plots

#Multi Index - Columns and Row
#-----------------------------
#%
import numpy as np
import pandas as pd

semester = ['Semester1'] * 3 + ['Semester2'] + ['Semester3'] * 3
semester
subjects = ['S11','S12','S21','S31','S32','S33','S33']
subjects
students = ['Student1','Student2','Student3','Student4']
colDF = pd.DataFrame({'SEMESTER':semester, 'SUBJECTS':subjects})
colDF
pd.MultiIndex.from_frame(dfcol)
colIndex = pd.MultiIndex.from_frame(colDF)
colIndex
data = np.random.randint(60,90, size=(4,7))

result1 = pd.DataFrame(data=data,columns= colDF)
result1
result2 = pd.DataFrame(data=data, columns= pd.MultiIndex.from_frame(colDF), index=students)
result2
result3 = pd.DataFrame(columns= pd.MultiIndex.from_frame(colDF), index=students)
result3

#------
result3a = result3.copy()
result3a.columns = result3a.columns.droplevel(0)
result3a

result3b = result3.copy()
result3b.columns = result3b.columns.droplevel(0)
result3b

#-------------------

result2a = result2.copy()
result2a.columns = result2a.columns.droplevel(0)
result2a

result2b = result2.copy()
result2b.columns = result2b.columns.droplevel(1)
result2b

result2c = result2.copy()
result2c

#remove a row with Student1
result2c.drop('Student1', axis=0)
result2c.drop(86, axis=1)
result2c.drop([('Semester1','S11')], axis = 1) 
#Remove one subject



#Remove unused levels
i = pd.MultiIndex.from_product([range(2), list('ab')])
i

#MultiIndex(levels=[[0,1],['a','b']],codes=[[0,0,1,1],[0,1,0,1]])
i[2:]
#MultiIndex(levels=[[0,1], ['a','b']], codes=[[1, 1], [0, 1]])
#The 0 from the first level is not represented and can be removed
#[0,0]
i[2:].remove_unused_levels()

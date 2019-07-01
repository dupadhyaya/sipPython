# -*- coding: utf-8 -*-
#
#-----------------------------
#%https://jakevdp.github.io/PythonDataScienceHandbook/03.05-hierarchical-indexing.html


midx = pd.MultiIndex(levels=[['Delhi', 'Chandigarh'], ['AIIT', 'ABS', 'ALS']],codes=[[0,0,1,1,1], [0, 1, 0, 1, 2]])
midx
d = [[100,120],[75,70],[120,105],[90,65],[80,55]]
d
df = pd.DataFrame(index=midx, columns=['Male', 'Female'], data=d)
df
df.index
df.drop(index='ABS')
df.drop(columns=['Male'], axis=1)
df.drop(index=['Delhi'], axis=0)
df.drop(index='ABS',level=1,axis=0)
df.drop(index='Delhi',level=0,axis=0)
df.drop(index=['Delhi','Chandigarh'],level=1,axis=0)  #no effect
df.drop(index=['Delhi','Chandigarh'],level=0,axis=0)  #no data
df.drop(index=['AIIT'],level=1,axis=0)  #no data



df.drop(index=['AIIT'], axis=0)

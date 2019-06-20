# -*- coding: utf-8 -*-
#-----------------------------
#%
#Cross Tab
#%

import pandas as pd
import seaborn as sns

# Read in the CSV file and convert "?" to NaN
df1 = pd.read_csv('data\mtcars.csv')
df1.head()
df1.columns

pd.crosstab(df1.cyl, df1.gear)

#df1.pivot_table(index='cyl', columns='gear')

pd.crosstab(df1.cyl, df1.gear, margins=True, margins_name="Total")

pd.crosstab(df1.cyl, [df1.gear, df1.am])

pd.crosstab([df1.cyl, df1.vs], [df1.gear, df1.am], rownames=['Cylinder', "Engine Type"], colnames=['Gear', "Transmission Type"],  dropna=False)

xtab1 = pd.crosstab([df1.cyl, df1.vs], [df1.gear, df1.am], rownames=['Cylinder', "Engine Type"], colnames=['Gear', "Transmission Type"],  dropna=False)


sns.heatmap(xtab1,  cmap="YlGnBu", annot=True, cbar=False)

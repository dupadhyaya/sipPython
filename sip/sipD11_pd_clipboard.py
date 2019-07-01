#Pandas - read / write to clipboard
#-----------------------------
#%
import pandas as pd
dfread = pd.read_clipboard()
dfread
#pandas.read_clipboard(sep='\\s+', **kwargs)[source]
dfread.to_clipboard()
dfread.iloc[2:4,1:3]
#now paste it in excel or csv
dfread.loc[2:4,['sub11','sub12']]

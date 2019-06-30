#Pandas - read / write to clipboard
#-----------------------------
#%

import pandas as pd

dfread = pd.read_clipboard()
dfread
#pandas.read_clipboard(sep='\\s+', **kwargs)[source]

dfread.to_clipboard()
#now paste it in excel or csv

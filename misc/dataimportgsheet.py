# -*- coding: utf-8 -*-
#
#-----------------------------
#%
#go to this URL
#https://docs.google.com/spreadsheets/d/1CyRWdMMpZN0eHK86MzTDDMhk6u_7jU88GhT3l4yS6nE/edit#gid=1231355909
#importing data from google sheets
#open the online sheet. convert to web : PUblish to web : full documents
#see the individual sheetIDs

import pandas as pd

file_id="1231355909"
link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS3HvsiRUiSyKNCWIGIHnexiupwmR_pzDwDbH0_ypRt5VdM5sIbSZtL5Q2K4u2jLHoNv6wc56kZ61hE/pub?gid={FILE_ID}&single=true&output=csv"
link
csv_url=link.format(FILE_ID=file_id)
csv_url
df = pd.read_csv(csv_url)
df

file_id2 = "1413672922"
csv_url2=link.format(FILE_ID=file_id2)
csv_url2
df2 = pd.read_csv(csv_url2)
df2.head()

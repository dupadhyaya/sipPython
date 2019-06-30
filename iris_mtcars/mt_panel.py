#Pandas Panel Data - mtcars
#-----------------------------
#%


from pydataset import data
mtcars = data('mtcars')
mtcars.head()

mtcars.values
mtcars.index
mtcars.columns
data = mtcars.values
data
mtindexDF1 = pd.DataFrame({'TYPE':['NUMERIC','NUMERIC', 'CATEGORY', 'NUMERIC', 'NUMERIC', 'NUMERIC', 'NUMERIC', 'CATGEGORY','CATGEGORY', 'CATGEGORY', 'CATGEGORY' ], 'COLNAME': ['mpg', 'cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear','carb']}) 
mtindexDF1
mtindex1 = pd.MultiIndex.from_frame(mtindexDF1)
mtindex1
pdMTCARS1 = pd.DataFrame(data, columns=mtindex1)
pdMTCARS1
pdMTCARS1(['TYPE', 'COLNAME']).sort_index
.sort_values(['TYPE', 'COLNAME'], ascending=True, inplace=True)

#Plots Plots   
#-----------------------------
#%

from pydataset import data
mtcars = data('mtcars')
mtcars.head()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#
print(mtcars.columns, end=' , ')
catCols = ['cyl', 'vs', 'am', 'gear', 'carb']
mtcars[catCols] = mtcars[catCols].astype('category')
mtcars.dtypes

#%%
plt.plot([1,2,3], [1,2,3], 'go-', label='line 1', linewidth=2)
plt.hist(x=mtcars.mpg)
plt.scatter(x='wt', y='mpg', data=mtcars)
mtcars.groupby('gear').size().plot(kind='bar')
#factor plot for categories

#multiple plots
#Grid of plots
fig, ax = plt.subplots(figsize=(6,3))
#Two blank panels
ax.plot([1, 3, 5])
ax.set_title('Dhiraj')
ax.grid(True)
plt.show()
fig.tight_layout()

#%%
x1= np.random.randint(30, 100, 1000)
x2= np.random.standard_normal(100)
np.mean(x1); np.mean(x2)
fig1, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
ax1.hist(x1, bins=10)  # row1, col1
ax2.hist(x2, bins=5)   # row1, col2
plt.show()
#
(fig1.axes[0] is ax1, fig1.axes[1] is ax2)
#
fig1, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
fig1.axes[0].hist(x1, bins=10)  # row1, col1
fig1.axes[1].hist(x2, bins=5)   # row1, col2
plt.show()
#------------

gridsize = (3, 2)
fig = plt.figure(figsize=(12, 8))
ax1 = plt.subplot2grid(gridsize, (0, 0), colspan=2, rowspan=2)
ax2 = plt.subplot2grid(gridsize, (2, 0))
ax3 = plt.subplot2grid(gridsize, (2, 1))
#not plot
ax1.hist(x2, bins=5, color='r')
ax2.hist(x2, bins=5, color='g')
ax3.hist(x2, bins=5, color='y')
#plt.close('all') #closes all the figure windows:
#--------------------



ax[0].plot([1, 3, 5])
ax[0].set_title('Dhiraj')
ax[0].grid(True)
ax[1].plot([2, 4, 6])
ax[1].set_title('Upadhyaya')
ax[1].grid(False)
plt.show()
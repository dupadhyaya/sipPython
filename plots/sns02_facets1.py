# -*- coding: utf-8 -*-
#Created on Mon Jun 24 17:47:13 2019 : dhiraj@sony

#mtcars
from pydataset import data
mtcars = data('mtcars')
mtcars.head()

import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

#Part-1 : nothing to show 
g = sb.FacetGrid(mtcars, col='am')
plt.show()  #2 am types

g = sb.FacetGrid(mtcars, col='gear')
plt.show()  #3 gear types

#Part 2 : 
g = sb.FacetGrid(mtcars, col='am')
g.map(plt.hist, 'mpg')  #histogram of mpg
plt.show()

g = sb.FacetGrid(mtcars, col='gear')
g.map(plt.hist, 'mpg')  #histogram of mpg
plt.show()

g = sb.FacetGrid(mtcars, col='gear')
g.map(plt.bar, 'cyl')  #histogram of mpg
plt.show() #not working...

#now it is working
g = sb.FacetGrid(mtcars, col='gear')
g.map(plt.scatter, 'wt', 'mpg')  #
plt.show() #now working...
#not quite right

#mtcars.groupby(['gear','cyl']).size().unstack()


#
g = sb.FacetGrid(mtcars, col='gear')
g.map(plt.scatter, 'wt', 'mpg')  #scatter
plt.show()

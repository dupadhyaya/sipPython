#
#-----------------------------
#%

#https://towardsdatascience.com/the-tale-of-missing-values-in-python-c96beb0e8a9d

from sklearn.preprocessing import Imputer
In [2]: imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
In [3]: imp.fit(train)
In [4]: train= imp.transform(train)
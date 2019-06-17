# -*- coding: utf-8 -*-
#-----------------------------
#%Count Plot

#https://vincentarelbundock.github.io/Rdatasets/datasets.html
import statsmodels.api as sm
dataset_mtcars = sm.datasets.get_rdataset(dataname='mtcars', package='datasets')
dataset_mtcars.data.head()
df = dataset_mtcars.data

plt.figure(figsize=(12,6))
sns.countplot(x='cyl',data=df, hue='gear')
plt.xticks(rotation=45);

#https://python-data-science.readthedocs.io/en/latest/exploratory.html
#Multiple Plots
df.cyl.value_counts()
fig, axes = plt.subplots(ncols=3, nrows=1, figsize=(15, 5)) # note only for 1 row or 1 col, else need to flatten nested list in axes
gear = [4,6,8]
axes
for gear, ax in enumerate(axes):
    sns.countplot(x=gear[cnt], data=df, ax=ax, order= df[gear[cnt]].value_counts().index)

for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=90)
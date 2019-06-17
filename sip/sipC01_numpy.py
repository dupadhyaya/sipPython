# -*- coding: utf-8 -*-
#Numpy
import numpy as np

np.arange(10)
np.arange(0,10)
x=np.arange(10,20)
x
x[0], x[5], x[-1]
x[0:5]
x[0:8:2]
x[10:0:-1]
x[1::3]



np.random.random(size=10)
np.random.randint(10, size=6)
x=np.random.randint(10, size=(3,4))
x[1,1]
x[:2,]
x[:1,:2]
x[::2,::1]
x[::-1,::-1]



x=np.random.randint(10, size=(3,4,5))
x
np.ndim(x), np.shape(x), np.size(x)

np.random.randint(1, 10, size=10)
np.random.randint(10,20, size=(3,5))
np.random.normal(0,1,(3,3))
np.linspace(10,15,9)
np.empty(10)
np.eye(4)
np.zeros([10])
np.ones([12])
np.full((3,4),[3.14])

np.array([1,2,3,4])
np.array([1,2,3,4,5,6]).reshape(2,3)
x=np.array([1,2,3,4,5,6]).reshape(2,3)
x
x[:,np.newaxis]
x[np.newaxis,:]

#%%
x=np.array([1,2,3])
y=np.array([4,5,6])
x,y
np.concatenate([x,y])
x=np.arange(6).reshape(2,3)
x
y=np.arange(10,16).reshape(2,3)
y
np.concatenate([x,y], axis=0)
np.concatenate([x,y], axis=1)

np.vstack([x,y])
np.hstack([x,y])

#split
x=np.arange(10,19)
x1,x2,x3 = np.split(x,[3,5])
x1,x2,x3
y=x.reshape([3,3])
y
upper, lower = np.vsplit(y,[2])
upper
lower
left, right = np.hsplit(y,[1])
left
right

#%%
#Ufuncs
x=np.arange(5)
x
np.add(x,5)
np.multiply(x,10)
y=np.empty(5)
np.multiply(x,5, out=y )
y


#%%
x=np.random.randint(10,100, size=(3,6))
np.size(x)
x.sum()
x.mean()
x.sum(axis=0)
x.sum(axis=1)
x.min()
x.min(axis=1)
x.max(axis=0)
x
np.median(x)
np.max(x)
np.min(x)

#%%
x=np.random.randint(10,100, size=20)
x

np.equal(x, 49)
np.greater(x, 40)
np.less(x, 50)
np.greater_equal(x, 40)
x < 40
np.sum(x < 40)

#np.sum(x < 40, axis=0)
x=np.random.randint(10, size=(3,4))
x
np.all(x > 4)
np.any(x > 4)
np.sum(x > 1)
np.sum(x > 3, axis=1)
np.sum(x > 3, axis=0)
np.sum( (x> 3) & (x < 7), axis=0)
np.sum( ~((x> 3) & (x < 7)), axis=0)


#sort
#%%
x = np.random.randint(100,size=50)
x
np.sort(x)
np.argsort(x)

x = np.random.randint(10,size=10)
x
np.partition(x, 3)  #sort
np.partition(x, 4)  #sort


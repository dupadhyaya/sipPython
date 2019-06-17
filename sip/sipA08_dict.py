# -*- coding: utf-8 -*-
#Data Stuctures - Dictionaries
#Dictionary - collection, unordered, changeable/ mutable, indexed, curly bracket with key:value pairs

car = { 'brand':'Honda', 'model': 'Jazz', 'year' : 2017}
car

#access
car['brand']
car.get('brand')

#change
car['year'] = 2018
car.get('year')

#list all Keys
for i in car: print(i)

#list all values
for i in car: print(car[i])

for i in car.values() : print(i)

#key - value
for i, j in car.items() : print(i, j)

#check if key exist
if 'model' in car: print('Model key exists')

#length
len(car)

#add items
car['color']= 'black'
car

#remove items
car.pop('model')
car

#removes last inserted item ie color here
car.popitem()
car

#remove item with specified key name
del car['brand']
car

#delete dictionary
del car
car

#empty dictionary
car = { 'brand':'Honda', 'model': 'Jazz', 'year' : 2017}
car
car.clear()
car
car['brand'] ='hyundia'
car

#copy dictionary
car = { 'brand':'Honda', 'model': 'Jazz', 'year' : 2017}
car
yourcar = car.copy()
yourcar
#method2
hiscar = dict(car)
hiscar

#new dictionary
newcar = dict(brand ='Honda', model ='Jazz', year=2017)
newcar
#round bracket, no quotes in keys, equal to symbol


#methods 
#clear, copy, fromkeys, get, items, pop, popitem, setdefault, update, values


car(['brand','year'])

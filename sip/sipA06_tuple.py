# -*- coding: utf-8 -*-
#Tuples - collection, ordered, unchangeable/ unmutatble, like list, round bracket

tuple1 = (1,2, 'SIP', 'Dhiraj', True)
tuple1

#everying like list except changes
tuple1[0] = 99

#access
tuple1[0]

for i in tuple1 : print(i)

if 'Dhiraj' in tuple1 : print('Dhiraj is present in tuple')
if 'Kounal' in tuple1 : print('Kounal is present in tuple')

tuple1.append('kounal')  #error, cannot add
len(tuple1)

#methods in tuple
#count, index, ...
tuple1
tuple1.remove()  #cannot remove also

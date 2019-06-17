# -*- coding: utf-8 -*-
#list comprehension

even1 = [ 2*i for i in range(1,11)]
even1

for i in even1:
    print(i, "\t", round(i/3,1), "\t", i%3 == 0 , end = "\n")

even2 = [ 2*i for i in range(1,11) if i%3 ==0]
even2

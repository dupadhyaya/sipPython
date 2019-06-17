# -*- coding: utf-8 -*-
#lambda function
# small anonymous function
#take any number of arguments but can have one expression

#lamda arguments : expression

x1 = lambda a : a + 10
x1(5)

x2 = lambda a, b, c : a + b + c
x2(1,2,3)

#used within other functions

def func1(n):   return lambda a : a + n
func2 = func1(2)
func2(11)

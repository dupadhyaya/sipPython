# -*- coding: utf-8 -*-
#if-else condition
#logical operations


x=1
#short methods
if x == 1 : print("x = 1")
#
y=2
print(x) if x > y else print(y)
x=1
print("This is X", x) if x==1 else print("x not equal to 1")
#3 conditions
x=3; y=3
print("X") if x > y else print("=") if x == y else print("Y")
#longer way
if x > y:
    print("X")
elif x == y:
    print("=")
else :
    print("Y")



#other logical operations
#==, !=, <, > , <=, >= 

#with else 


if x == 1: 
    print(" x=1")
else:
    print("x not equal to 1")
x=2

if x == 1: 
    print(" x=1")
else:
    print("x not equal to 1")

#no bracket, use of indentation with colon operator
#elif

if x == 1: 
    print(" x=1")
elif x == 2:
    print(" x=2")
else :
    print("x not equal to 1 or 2")

x=3
if x == 1: 
    print(" x=1")
elif x == 2:
    print(" x=2")
else :
    print("x not equal to 1 or 2")


#shorthand if


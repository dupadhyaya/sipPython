# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 18:57:25 2017 by Dhiraj Upadhyaya
Chp-13 : Functions
"""
"""
def print_hello():
    print('Hello')

print_hello()
print('Dhiraj', end=' ')
print_hello()

def draw_square():
    print('*' * 15)
    print('*', ' ' * 11, '*')
    print('*', ' ' * 11, '*')
    print('*' * 15)
draw_square()


def print_hello(n):
    print('Hello ' * n, end='\n')

print_hello(3)
print_hello(5)

def print_hello(m, n):
    print(m, 'Hello '* n, end='\n')

print_hello('Dhiraj',3)

# return values
def convert(t):
    return(t * 9 / 5 + 32)
x=100
print(x, ' Celcius into Fah is ', convert(100))

from math import pi, sin
def deg_sin(x):
    return sin(pi * x/180)
x=90
print(x, ' in radian is degrees ', deg_sin(x))
#sin 90 =1

# return multiple values
def solve(a,b,c,d,e,f):
    x = (d + e - b + f) / (a + d - b + c)
    y = (a + f - c + e) / (a + d - b + c)
    return[x,y]
xsol, ysol = solve(2,3,4,1,2,5)
print(' The solution is x = ', xsol , ' and y is ', ysol)

# return to end function call
bad_words = ['ugly', 'bad']
def multiple_print(string, n, bad_words):
    if string in bad_words:
        print(' Return from here')
        return
    print(string * n)
    print()

multiple_print('bad',3,bad_words)

#default values in function
def multiple_print(string, n=1):
    print(string * n)
    print()

multiple_print('Dhiraj')
multiple_print('Upadhyaya',3)



#13.5 Local Variables
def func1():
    for i in range(5):
        print(i, sep=' ', end='\t')

def func2():
    i = 100 
    print()
    func1()  # i's of func1 are used
    print(i, sep=' ', end='\t') # this i is 100
func1()
func2()
print()
"""

def reset():
    global time_left
    #time_left = 30
    print('Print in Reset ', time_left)

def print_time():
    print('Print inside print time ', time_left)
    
time_left=40  # can be changed from anywhere
print('Print outside Function - 1 ',time_left)
reset()
print_time()
print('Print outside Function - 2 ',time_left)



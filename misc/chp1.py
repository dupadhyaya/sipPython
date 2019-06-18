"""
Created on Mon Sep 25 06:58:44 2017 by Dhiraj Upadhyaya
"""
#Ch- 1 PIPY
# Eg 1.3

# --- Bookmark 1

temp = eval(input("Enter the Temp in C- "))
print('Temp in F is ', 9/5 * temp + 32)


num1 = eval(input('Enter the first no- '))
num2 = eval(input('Enter the 2nd No - '))
print('Sum of two nos ' , num1, ' and ', num2, 'is ', num1+num2, ' and average is ' , (num1+num2)/2)

# ---   Bookmark 2 
#1.5 Getting Input
# --- Input from the user
name = input(' Enter your name ')
print(" Hello ", name)

# Basic Structure : variable_name = input(message to user)
# For numeric values variable_name = eval(input('Enter a number')
num = eval(input('Enter a number: '))
print('You no square : ', num * num)
# --- Bookmark 3
print(2 * 4 + 5)

## Printing
print('Hi There') # prints as it appears
print('3+4')
print(3+4)
# several items
print('Hi There', '3+4', 3+4)
print('Hi There \t', '3+4 \n', 3+4)   # with next line & tab



print('Dhiraj ',' Upadhyaya',' with sep ', sep='-')
print('Dean DS')

print('Dhiraj ',' Upadhyaya',' with sep & end ', sep='-', end='') # same line
print('Dean DS')
# different way to use end
print('Dhiraj ',' Upadhyaya',' with sep and different option of end',  sep='-', end=':::')
print('Dean DS')

#--- 1.7 Variables
temp = eval(input('Enter a temperatur in C '))
print(' In F it is ', 9/5* temp +32)
f_temp = 9/5 * temp+ 32
print(f_temp)
if f_temp >  212:
    print(' Temp is above boiling point')
if f_temp < 32:
    print('Temp is below frezzing point')
    
"""

# Example
x=3; y=4; z = x+y ; z=z+1; x=y; y=5
print(x, y,z)

# Variable Names

# 1.8 Exercises
# Print Box

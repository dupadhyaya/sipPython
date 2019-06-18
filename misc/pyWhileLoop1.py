# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 06:37:23 2017 by Dhiraj Upadhyaya
Chp-9 : while loops
"""
"""
temp = 0
while temp != -1000:
    temp = eval(input('Enter the temp in C (-1000 to quit) ')) 
    print('In F, the temp is ', 9/5 * temp + 32)

for i in range(10):
    print(i, end =' ')
print()
i=0
while i < 10:
    print(i, end=' ')
    i=i+1
# infinite loop - when exit condition is not reached
# while True:
#break



for i in range(10):
    num = eval(input(' Enter the no: '))
    if num < 0 :
        print('No entered is < 0 ,.. exiting ')
        break
#9.4 Else
for i in range(5):
    num = eval(input("Enter the no "))
    if num < 0:
        print('Stopped Early ')
        break
    else:
        print('No is ', num)
else:       # placement of else below for
        print('user entered all 5 values')
"""
        
# Prime Nos - 2 methods
num=4 ; i=2
while i<num and num%i != 0:
    i = i+1
print(i, num)
if i == num:
    print('Prime')
else:
    print('Not prime')
print('*** 2nd method ****' )
for i in range(2, num):
    if num%i == 0:
        print('Not a prime ')
        break
    else:
        print(' Prime ')

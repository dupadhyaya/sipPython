# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 05:36:21 2017 by Dhiraj Upadhyaya
Chp-6 Strings
"""

#m = """ is a long string that is 
#spread across two lines """


#Basics
s = ' Hello'
t = "Hello"

print(s, t, m, sep='\n')

num = eval(input(' Enter a no  '))
string = input('Enter a string  ')
print(num, string)

#length of string
fname = 'Dhiraj'
age = 50
lname = ' Upadhyaya'
city =''  # empty string
print(len(fname), len(lname), len(city), sep='\t')
#print(len(age), sep='\t')  # len of numeric value- involid

# concatenation
print('AB' + 'cd') # ABcd
print('A', '7', 'B')  # A7B
print('Hi' *4) # 4 times Hi
#print('Hi' + 4) # this will not work

print('-' *75)  # long dashes
s=''
for i in range(10):
    t = input('Enter a letter : ')
    if t =='a' or t =='e' or t =='i' or t =='o' or t =='u' :
        s = s + t
print(s)  # aeou



# in operator

name = 'Dhiraj Upadhyaya'
if 'a' in name:
    print('a is in the string')

if 'x' not in name:
    print('x is not in the string')

s=''
for i in range(5):
    t = input('Enter a letter : ')
    if t in 'aeiou':
        s = s + t
print(s)
#6.4 Indexing
s='Python'
print(s[0], s[1], s[-1], s[-2])
for i in range(len(s)):
    print(i, ' element is ', s[i])
print('\n')
for i in range(1,len(s)+1):
    print(len(s)-i, ' element is ', s[-i])



#6.5 Slice
s ='abcdefghij'
print(s, len(s))
print(s[0], s[1], s[len(s)-1], s[9])
print(s[2:5])  # (2-1)=1 to (5-1)=4 characters
print('upto 5th character ', s[:5])  # upto 5th character 0-4
print('5th to last character ', s[5:])  # from 5th character to last
print('Last 2 characters ', s[-2])  # 2nd last characters
print('All Characters ', s[:])  # all characters
print('1st to 7th ',s[1:7:2])  # from 1st to 7 with step 2
print(' Rev String ', s[ : : -1])  # reverses the string
x3 = numpy.arange(1, 9, 2)
print(x3)
#print(s[numpy.array([1,2,3])])  # does not work

#6.6 Changing Individual Characters
s ='abcdefghij'
print(s)
#s[4] = 'X'  # this will not work 
#python string are imutable, cannot modify
s = s[:4] + 'X' + s[5:]
print(s)

#6.7 Looping
for i in range(len(s)):
    print(s[i], sep='\t', end=' ')
print('\n')
for c in s:
    print(c, sep='', end='\t')


#String Functions
# lower, upper, replace, count, index, isalpha
s ='abcdefghij'
print(s.lower())
print(s.upper())
s1 = 'Hi Dhiraj'
print(s1)
print(s1.replace('Hi', 'Hello'))
print(s.index('a'))
print(s1.index('D'))  # excl space

s3 = 'u'
print(s3.isalpha())
n1 = '1' # n1=1 is wrong, since it will be numeric
print(n1.isalpha())
print(s1.isalpha())  # String will be False if any character is not
print(s.isalpha())  # this is true does not have space

x ='d'
for x in s1:
    location = s1.index(x)
    print(location, end=' ')
print()
s1 = 'Hi Dhiraj'
print(s1)
print(s1.index('D'))


print('\n' * 3) # 3 blank lines

s = input('Enter some text : ')
for i in range(len(s)):
    if s[i] == 'a':
        print(i, end='\t')

s = input('Enter some text : ')
doubled_s = ''
for c in s:
    doubled_s = doubled_s + c * 2
print(doubled_s)  
#Hello -> HHeelllloo

name = input('Enter your name : ')
for i in range(len(name)):
    print(name[:i+1], end='\t')
#D       Dh      Dhi     Dhir    Dhira   Dhiraj  


#Remove Punctuation Marks
s="Dhiraj ( * d , ; b "
s = s.lower()
print(s)
for c in ',.;:-?() \' \"':
    s = s.replace(c, '')
print(s)

# Print decimal part
s= '34.5673'  # as text float does not have index function
print(s[s.index('.')+1:])

from math import floor
num = 34.5673
print(num - floor(num))

import string
print(string.ascii_lowercase[:26])
alphabet = string.ascii_lowercase[:26]
#alphabet = 'abcde'
print(alphabet)
key = string.ascii_lowercase[20:26] + string.ascii_lowercase[0:20]
print(key)
secret_message = 'Dhiraj 2017 & * Upadhyaya'
secret_message = secret_message.lower()
for c in secret_message:
    if c.isalpha():
        print(key[alphabet.index(c)], end ='')
    else:
        print(c, end='')

    
import string
print(list(string.ascii_lowercase))  
for i in range(0, 10, 2):
    print(i, end='')

print("hello{0}, world!".format('z'))

for one in range(97,110):
    print(chr(one), end=' ')
    
    
small_letters = map(chr, range(ord('a'), ord('z')+1))
big_letters = map(chr, range(ord('A'), ord('Z')+1))
digits = map(chr, range(ord('0'), ord('9')+1))
print(small_letters, '\n', big_letters, '\n', digits)
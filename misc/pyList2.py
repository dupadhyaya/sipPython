# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 11:18:34 2017 by Dhiraj Upadhyaya
Chp 8 - More with Lists
"""

# choice(L), sample(L,n), shuffle(L) 

from random import choice, sample
"""
names = ['ritwik', 'sadiva', 'devansh', 'nikhil', 'himanshu', 'dummy']
current_player = choice(names)  # only 1 item from the list
print(current_player)

team = sample(names, 2)  # more than 1 item
print(team)

s = 'thequickbrownfoxjumpsoverthelazylittledog1234567890!@#$%^&*()'
for i in range(100):
    print(choice(s), end =' ')
print('\n')
from random import shuffle
print(names)
shuffle(names)
print(names)
for p in names:
    print(p, ' : it is your turn')

# in 2 teams
shuffle(names)
teams=[]
for i in range(0, len(names),3):
    teams.append([names[i], names[i+1], names[i+2]])
print(teams)


#8.2 Split
s ='Hi ! this is a test '
print(s.split())  # list of words sep by space etc..

from string import punctuation
for c in punctuation:
    s = s.replace(c, '') # ! with space
print(s)

# count of words
from string import punctuation
#s = input('Enter the word ')
s =' the a the above below the '
for c in punctuation:
    s = s.replace(c, '')
s = s.lower()  # first convert to lowercase
L = s.split() # then split it
print(s, L, sep='\n')

word = 'the'
print(word, ' appears ', L.count(word), ' times ')

s = '1-800-271-8281'
print(s.split('-'))


#8.3 Join - opposite to split
L = ['A','B','C']
print(' '.join(L))
print(''.join(L))
print(','.join(L))
print('*&*'.join(L))

from random import shuffle
#word = input('Enter a word :' )
word = 'Dhiraj Upadhyaya'
letter_list = list(word)
print(letter_list)
shuffle(letter_list)
print(letter_list)
anagram = ' '.join(letter_list)
print(anagram)   # characters of name in different order


#8.4 LIst comprehensions - create list
string = 'Hello'
L=[1,14,5,9,12]
M=['one', 'two', 'three', 'four', 'five', 'six']


L = [ i for i in range(5)]
print(L)

L = [ 0 for i in range(5)]
print(L)

L = [ i**2 for i in range(5)]
print(L)

L = [ i*10 for i in range(5)]
print(L)

L = [ c*2 for c in string]
print(L)

[m[0] for m in M ]
print(M)
print([m[0] for m in M ])  # first char of each word


L=[1,2,4,11]
x=[i for i in L if i < 10]
print(x)

y=[m[0] for m in M if len(m) == 3]
print(y)

# longer way
L=[]
for m in M:
    if len(m) == 3:
        L.append(m)
print('2nd way', L)



#Multipe fors
L = [[i,j] for i in range(2) for j in range(2)]
print(L)
print('\n')
L = [[i,j,k] for i in range(2) for j in range(2) for k in range(3)]
print(L)
print('\n')

L = [[i,j] for i in range(4) for j in range(i)]
print(L)


#8.5 List Comprehensions
# 50 random nos betw 1 and 100
L = [randint(1,100) for i in range(50)]
print(L)
# replace each with its square
L = [ i**2 for i in L]
print(L)
#how many greater than 50
print('\n')
print(len(L))
print(len([ i for i in L if i>50]))

# nos betw 1 & 100, how many 1s, 2s
L = [randint(1,100) for i in range(100)]
frequencies = [L.count(i) for i in range(1,101)]
print(L)
print(frequencies)
# [2, ] means there are two 1s in the list & so on

#random assortment of 100 letters
from random import choice
alphabet = 'abcdedfghijklmnopqrstuvwxyz'
print(alphabet)
s = ''.join([choice(alphabet) for i in range(100)])
print(s)
# flip order of list of size 2
L = [[1,2], [3,4], [5,6]]
M = [[y,x] for x,y in L]
print(L)
print(M)

x=3 ; y=5
print(x,y)
x,y = y,x # swap
print(x,y)
"""
# 2dim list
L = [[1,2,3],
     [4,5,6],
     [7,8,9]]
print(L)
"""
print(L[1][2])  # L[r][c] r/c=0 onwards

#printing 2 dimlist
for i in range(3):
    for j in range(3):
        print(L[i][j], end=' ')
    print()

from pprint import pprint
pprint(L)

#working with 2 dim - no of even nos
count= 0
for r in range(3):
    for c in range(3):
        if L[r][c]%2 == 0 :
            count = count + 1
print(count)

#another way
count=sum([1 for r in range(3) for c in range(3) if L[r][c]%2 == 0])
print(count)

# create list
L = [[1+i,2+i,3+i,4+i,5+i] * 5 for i in range(10)]  # 5 cols, 10 rows
for i in range(10):
    for j in range(5):
        print(L[i][j], end='\t')
    print()
#print('\n')
from pprint import pprint
print(L)
print('\n')
#pprint(L)
print(L[0])  # 1st row  ??
print(len(L))  # no of rows - len
print([L[i][0] for i in range(len(L))]) #1st col   
print([L[0][i] for i in range(5)])   #1st row

"""

#flatten list -> single dim
#[ j for M in L for in M]
print(L)
print([ j for M in L for j in M])  # ???

#create higher dim list
L = [[[0] * 5 for i in range(5)] for j in range(5) ]  # 5x5x5 list
print(L)
from pprint import pprint
pprint(L)
print()
L = [[[1,2,3,4,5]  for i in range(5)] for j in range(5) ]  # 5x5x5 list
from pprint import pprint
pprint(L)

print(L[0][0][0])  #1st item in the list 0,0,0

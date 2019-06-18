# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 20:11:12 2017 by Dhiraj Upadhyaya
Chp 7 : Lists
"""

"""
# 30 scores - 30 variables -> put in a list
L = [1,2,3]
print(L)
#print(L.sort())

print(range(1,10,2))

l = list(range(1, 100, 4)) + list(range(2, 100, 4))
print(l.sort())

l2 = ','.join(map(str, sorted(list(range(1, 100, 4))) + list(range(2, 100, 4))))
print(l2)

num = [0,1,2,3,4,5]
print('The first element is ', num[0])
print('The third element is ', num[2])


from sys import stdout
for i in range(1,11):
    stdout.write(str(i)+' ')
"""
# types of data in the lists
L1 = [1, 2, 2.718, 'abc', [5,6,7], 2]
#print(L1)

"""
#7.2 Similarities to string
print(len(L1))
if 2.718 in L1:
    print('List contains 2.718')
if 0 not in L1:
    print('List does not contain 0')
print(L1[0], L1[:3], L1[1:2], L1[-2])
print(L1.index([5,6,7]))
print(L1.count(2))

"""

#Built in function for List
# len, sum, min, max
# methods - append(x), sort(), count(), index, reverse, remove, pop, insert(p,x)
L2 = [1, 2, 2.718, [5,6,7], 2]
L3 = [1, 2, 5, 3, 2]
"""
print(L2)
L2.append(56)
print(L2)
L3.sort()  # sort list
print(L3)
#print(sort(L2))  # sort only number list of one type float or int
print(L2.count(2))
print(L2.index(2)) # first occurance of 2
L2.reverse()  # reverse the list
print(L2)   # print rev list
L2.remove(1)  #remove first occurance of 1
print(L2)
print(L2.pop(2)) # remove item as 2nd location and print it
print(L2)
L2.insert(2, 12345)  # insert item 12345 at 2+1nd location
print(L2)

# copy of List L to M
M = L3[:]
print(M)
# changing items in the list
L3[2] = 127 # easier than string
print(L3)
L3.insert(1,9) # insert 9 at 1+1st posn
print(L3)
del(L3[1])  # delete 1+1 item
print(L3)
del(L3[:2]) # delete 1st 2 items
print(L3)


#7.6 Examples
from random import randint
L = []
for i in range(50):
    L.append(randint(1,100)) # build the list
print(L)

count=0
for item in L:
    if item > 50:
        count = count + 1
print('Items more than 50 - ', count)

# Not clear
frequencies = []
for i in range(1, 10):
    frequencies.append(L.count(i))  # How many 1s, 2s etc
    print(i, end=' ')
    print(frequencies, end='\t')
print('\n')
print(frequencies)


# prints largest of 2 nos & 2 smallest elements of a listscoe
scores = [3,2,5,1,6,22,11,7]
scores.sort()
print('2 smallest :', scores[0], scores[1])
print('2 largest :', scores[-1], scores[-2])

"""


# Quiz
questions = ['What is the capital of UP ', 'What is the Capital of Bihar ']
answers = ['lucknow', 'patna']
num_right = 0

for i in range(len(questions)):
    guess = input(questions[i])
    if guess.lower() == answers[i].lower():
        print('Correct')
        num_right = num_right + 1
#        num_right +=1
    else:
        print('Incorrect ', 'The ans is ', answers[i])
print('You have ', num_right ,' answers, out of ', len(questions))

        
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 12:54:00 2017 by Dhiraj Upadhyaya
"""
#write to a file
fo= open('test.txt', 'w')
fo.write('Programming is fun with Python \n, R is also good')
print('The file no is : ', fo.fileno())
print('Current location of file : ', fo.tell())
fo.close()
print('File ', fo.name , ' is closed')

#read from a file
fo= open('test.txt', 'r')
str = fo.read(11)
print('String Read is ', str)
fo.close()
print('File ', fo.name , ' is closed')

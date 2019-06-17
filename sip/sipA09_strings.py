# -*- coding: utf-8 -*-
#Data Structure - Strings

#group of characters/ literals, surrounded by single or double quote

# 'hello' = "hello'

str1 = ' Hello , World '
str1
type(str1)

str1[0:7]

#removes blank spaces
str2 = str1.strip()
len(str2)
str2
str2.lower()
str2.upper()

str2.replace('H', 'Z')
str2  #temporary

liststr3 = str2.split(',')
type(liststr3)


#taking input from prompt
print('Enter your name ? ')
nameval = input()  #look at console, type your name
nameval



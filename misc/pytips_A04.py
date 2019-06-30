# -*- coding: utf-8 -*-
#Created on Fri Jun 21 11:09:09 2019 : dhiraj@sony


#2 inputs from user

x, y = raw_input(),  raw_input() 
x, y = raw_input().split() 
x, y = [int(x) for x in raw_input().split()]   
# Reads two numbers from input and typecasts them to int using  
# map function 
x, y = map(int, raw_input().split()) 


#Print list vertically
test_list = [[1, 4, 5], [4, 6, 8], [8, 3, 10]] 
test_list
# printing original list 
print ("The original list is : " + str(test_list)) 
# using naive method   
# to print list vertically : like a matrix
for i in range(len(test_list)): 
    for x in test_list: 
        print(x[i], end =' ') 
    print() 
    
# using zip()  # to print list vertically 
for x, y, z in zip(*test_list): 
    print(x, y, z) 

#Avoid quotes in list
# initializing list 
test_list = ['Dhiraj', 'Upadhyaya', 'Noida'] 
# printing original list  
print ("The original list is : " + str(test_list)) 
# using join() # avoiding printing last comma 
print ("The formatted output is : " , ' '.join(test_list))
print(*test_list, sep =', ') 

#Splitting strings
# using split() + list comprehension 
  
# initializing list 
test_list = [['Python is  the best'], ['All love R and Python'], ['Including me']] 
test_list  
# using split() + list comprehension  # Split Sublist Strings 
res = [sub.split() for subl in test_list for sub in subl] 
res  
str(res)
# using map() + lambda + split()  # Split Sublist Strings 
res = list(map(lambda sub: sub[0].split(' '), test_list)) 
str(res)




#links
https://towardsdatascience.com/23-great-pandas-codes-for-data-scientists-cca5ed9d8a38

#https://www.dataquest.io/blog/python-vs-r/
#https://shiring.github.io/r_vs_python/2017/01/22/R_vs_Py_post
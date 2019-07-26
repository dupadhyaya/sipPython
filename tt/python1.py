#Topic: TT
#-----------------------------
#
#Ex1.1
#Write a program to get the Python version you are using
import sys
print(sys.version)

#or in anacond command prompt
#C:\>python

#Ex1.2
#Write a python programm which accepts the radius of a circle from the user and computes the area

name = input("Enter your name : ") 
radius = float(input("Enter your radius : "))
#if int values has to passed use : int(input())
print(name, ' Area of Circle is ', 3.14 * radius **2)

#using lib
import math
print(math.pi)
print(name, " Area is ", math.pi * pow(radius,2))

#%%%

#Ex2.1
#Write a python program to displya the current date and time
import datetime
currentDT = datetime.datetime.now()
print(str(currentDT))    
print (currentDT.strftime("%Y-%m-%d %H:%M:%S"))
#https://tecadmin.net/get-current-date-time-python/
#Ex2.2 : same as Ex2.1

#%%%
#Ex2.2 
#Accept user's first and last name and print them in reverse order with a space in between 
#https://www.geeksforgeeks.org/reverse-words-given-string-python/

name='Tanvi Tiwari'
print(name)
namesplit = name.split()  # split first
namesplit
namesplit.reverse() # reverse list
namesplit  #should ['Tiwari', 'Tanvi']
# now join them
result = " ".join(namesplit)
print(result)

#another method
myname = input("Enter Your Name")
print(" ".join(myname.split(" ")[::-1]))
#another method
my_string = "I live in Wakhnaghat"
reversed_string = " ".join(my_string.split(" ")[::-1])
reversed_string
#https://stackoverflow.com/questions/34128842/how-to-reverse-the-order-of-the-words-string-using-python

##3.2 : Display first and last colors from the following list
color_list = ['Red', 'Green', 'White', 'Black']
len(color_list)
color_list[0]
color_list[len(color_list)-1]
for color in color_list: print(color, "=", len(color))  #size of word
for i in range(len(color_list)):    print(color_list[i], end=' ,')
#another method
for i in range(len(color_list)):    
    if (i==0)   :
        print(color_list[i])
    elif( i == len(color_list)-1)  :
        print(color_list[i])


#%%%
#Ex4: Write a python program to print the documents (syntax, description etc of python built in function)
abs(-4.4)
help(abs)
abs?
def printSyntax(functionName):  print(help(functionName))
printSyntax(abs)
printSyntax(max)

#%%%
#Ex5 Write a python program to get the difference between a given number and 17.If the no is > 178, return double the absoluted difference
inputNo = int(input("Enter your number "))
if( inputNo - 17 > 178):
    print(2 * abs(inputNo-17))
#using a function: run next 3 lines together to create function
def lab5a(inputValue):
    if( inputValue - 17 > 178):
        print(2 * abs(inputValue-17))
    
lab5a(inputNo)

#Write a program to test whether a number is between 1000 or 2000:
inputNo = int(input("Enter your number "))
if((inputNo > 100) & (inputNo < 2000)):
    print(" Number between 100 and 2000")
else:
    print(" Number NOT between 100 and 2000")
    

    
#Write a program to check whether a specified value is contained in a group of values
#Test Data : 3 -> [1,5,8,3] : True ; -1 -> False
list1 = [1,5,8,3]
n1= 3
n1 in list1
n2 in list1
#using a function
def lab5c(no):
    if no in list1:
        print(no, " is in the list ", list1)
    else:
        print(no, " is NOT in the list ", list1)    
lab5c(n1)
lab5c(n2)


#%%%
#%%%
#Ex6a : Write a program to print all even nos from a given no list in the same order and stop printing if any no that come after 237 in the sequence
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978,328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566,826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]
#check for even no
3%2==0
4%2==0

for no in numbers:
    if (no%2 == 0)  :
        print(no , end=', ')

for no in numbers:
    if (no%2 == 0)  :
        print(no , end=', ')
    if (no == 237)  :
        break
print(numbers, end=' , ')
numbers.index(237)  #this is position of 237 in the list : 21st
#print this list into a file
#printing list
print(*numbers, sep='\n')
print(*numbers, file='tt/numbers2.txt')
print('\n'.join(map(str, numbers))) 

#saving into a file
import pickle
with open('tt/numbers2.txt', 'wb') as fp:
    pickle.dump(numbers, fp)
#reading it pack
with open ('tt/numbers2', 'rb') as fp:
    itemlist = pickle.load(fp)
itemlist

#Ex: using file as input: change the path of the file.
#data = [line.strip() for line in open("tt/numbers2.txt", 'r')]
#execute the earlier function
for no in itemlist:
    if (no%2 == 0)  :
        print(no , end=', ')
    if (no == 237)  :
        break

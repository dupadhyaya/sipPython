#Data Time - Introduction

import datetime

#current date and time
x1 = datetime.datetime.now()
print(x1)

#Extract Year from todays date
print(x1.year)

#Day of the week
print(x1.strftime("%A"))

#particular Date
x2 = datetime.datetime(1947,8,15)
print(x2.year)
print(x2)
print(x2.strftime("%B %A"))

#lets import in different way
from datetime import datetime as dt
today = dt.now()
today
#parts of the data : Year, Month, Day, HH, MM, SEC, 
#Formatted Date
dt.strftime(today, '%d-%m-%y')

#Other formating codes
#%a, %A, %w, %d, %b, %B, %m, %y, %Y, %H, %H, %i, %p, %p, %M, %S
#%f, %z, %Z, %j, %U, %W, %C, %x, %X, %%

print(dt.strftime(today,"%a %A : %d : %b %B %m : %y %Y :: %H %M %S :: %I %p"))
print(dt.strftime(today,"%w %u %M : %f : %z %Z : %U %W %C :: %x %X %% "))


#read more at
#https://docs.python.org/2/library/datetime.html


#string to Date
today
type(today)
dt.strptime("4/7/2019", "%d/%m/%Y")  #no prefix of 0: 04
date1 = dt.strptime("4/7/2019", "%d/%m/%Y")
type(date1)  #datetype
date1 + 1

#Date to String
type(date1)

strdate1 = dt.strftime(date1, format="%d-%B-%Y")
strdate1
type(strdate1)  #string

#The strftime() method is defined under classes date, datetime and time. The method creates a formatted string from a given date, datetime or time object.
%Y - year [0001,..., 2018, 2019,..., 9999]
%m - month [01, 02, ..., 11, 12]
%d - day [01, 02, ..., 30, 31]
%H - hour [00, 01, ..., 22, 23
%M - month [00, 01, ..., 58, 59]
%S - second [00, 01, ..., 58, 59]
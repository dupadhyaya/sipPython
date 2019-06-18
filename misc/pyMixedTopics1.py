# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 06:57:11 2017 by Dhiraj Upadhyaya
Chp-10 : Misc Topics -II
"""
"""
#10.1 str, int, float, list
#string to nos
x=37
print(x*2,str(x) ,str(x)*2, sep='\t' )

x1=3.14
print(x1*2,str(x1), str(x1)*2, sep='\t' )

x2=[1,2,3]
print(x2*2, str(x2) , str(x2)*2, sep='\t' )
#convert to integers, float
y='37'
print(y, y*2, int(y), int(y)*2)

y1='3.14'
print(y1, y1*2, float(y1), float(y1)*2)

y2=3.14   # float value to int
print(y2, y2*2 )
print(int(y2), int(y2)*2)  # removes decimal places

# convert to list
print(list(range(5)))
print(list('abc'))

p = '99'
print(p==p[::-1], p, p[::-1])  # fwd order & rev order


for i in range(1, 101):
    s = str(i)  # convert to string
    if s == s[::-1]:  # check for palindrome nos
        print(s, end=' ')


birthday='January 1, 1996'
year = int(birthday[-4:]) # last 4 characters extract & convert to int
print(' you are ', 2017-year, ' yrs old')

# add digits of num in string
digit = str('45') # convert to string and read thru index
print(' Sum of digits', digit, ' are ', int(digit[0]) + int(digit[1]))

# any no of digits
num= 1991
digits = str(num)
answer = 0
for i in range(len(digits)):
    answer = answer + int(digits[i])
print(' Sum of digits of number ', num, ' is ', answer)



# decimal and integer part sum
num = 1991.1992
ipart = str(int(num))
#dpart = str(num - int(num))
dpart = str(round(num - int(num),4)) #round off nos to 4 decimal places

answer = 0
for i in range(len(ipart)):
    answer = answer + int(ipart[i])
print(' Sum of integer digits of number ', num, ' is ', answer)
answer = 0
for i in range(2,len(dpart)):
    answer = answer + int(dpart[i])
print('Integer part is ', ipart, ' Decimal part is ', dpart)
print(' Sum of decimal digits of number ', num, ' is ', answer)

# Checking of primenos
# move upto sqrt(no) - less traversal, less CPU time
num = 111
for i in range(2, int(num**.5)+1):
    print(i, end='')


#10.2 Boolean
game_over = True
highlight_text = False

if game_over == True:
    print(' Bye !')

#while not game_over -> while game_over = False

x = (6==6)  # assign True to x
print(x)


# shortcuts
count=1
count = count + 1
count2=1
count2 += 1
print(count, count2)

total = 10
total = total - 5
total2 = 10
total2 -= 5
print(total, total2)

prod = 3
prod = prod * 2 
prod2 = 3
prod2 *= 2
print(prod, prod2)
#others - /= , %= , //=, **=

a = 0; b=0; c= 0
print(a,b,c)
a = b = c = 0
print(a,b,c)
print()
x = L[0] ; y = L[1] ; z =L[2]
print(x, y, z)
print()
L = [0,1,2]
x,y,z = L
print(' L= ' , L)
print(x,y,z)
x,y,z  = 1,2,3
print(x,y,z)
x,y,z = y,z,z # swap values
print('Swapped values are ', x,y,z) 


# shortcuts with conditions
a=b=c=0
if a==0 and b==0 and c==0:
    print(' All a, b, c are 0', a, b, c)
if a==b==c==0:
    print(' All a, b, c are 0', a, b, c)

a=1; b=2 ; c=3
if 0<a and a<b and b<c:
    print(' 0 < a < b < c : ', 0, a, b, c)
if 0<a<b<c:
    print(' 0 < a < b < c : ', 0, a, b, c)

#10.4 Short Circuiting
words = ['dhixaj', 'rdhiraj', 'xdhilaj', 'ldhimaj', 'mdhirj' ]
#words = ['dhixaj', 'rdhiraj', 'xdhilaj', 'mdh' ]  #this will give error len of last element < 5

for w in words:
    if w[4] == 'r':
        print(w)  # sometimes error due to index out of range
print(' 2nd method ' )
for w in words:
    if len(w) >=5 and w[4] == 'r':
        print(w)
print(' 2nd method - part 2' )

words = ['dhixaj', 'rdhiraj', 'xdhilaj', 'mdh' ]  #this will work here
for w in words:
    if len(w) >=5 and w[4] == 'r':
        print(w)

#10.5 Continuation of code with \
string = 'dhiraj'
if 'a' in string or 'b' in string or 'c' in string \
or 'd' in string or 'e' in string:
    print(' a or b or c or d or e in string ', string)

#skip backslash when entering list, dictionary or arguments
L = ['A', 'B', \
     'C', 'D' ]
print(L)    
L = ['A', 'B', 'E',  # without backslash
     'C', 'D' ]
pass  # does nothing
print(L)    


# 10.7 String formating
bill = 23.60
tip = 23.60 * .25
print(' Bill is ', bill, ' Tip is ', tip)
print(' The tip is {:.3f}'.format(tip))
print(' The bill is  ${:.2f}'.format(bill+tip), ' and the tip is {:.2f}'.format(tip))
print(' The bill is  ${:.2f}  and the tip is ${:.3f}'.format(bill+tip, tip))


# formating for integers
print(2)
print(format(2))
print('{:3d}')
print('{:3d}'.format(2))  # d - for integers - right justify
print('{:3d}'.format(123))  # 3 says - values has been alloted 3 spots
print('{:4d}'.format(123))  # 4 says - values has been alloted 4 spots shifting

print('{:3f}'.format(1022.45678))
# centering integers
print('{:^5d}'.format(2))  # allot 5 spaces xx2xx
print('{:^5d}'.format(123)) # format x123x
print('{:^5d}'.format(12345)) # format 12345

print('{:,d}'.format(12345))  # comma sep for thousand value
print('{:,^5d}'.format(123456789))  # ^ does not work with ,

print('{:.3f}'.format(123.45678))  # change decimal placess rounds off nos
print('{:.1f}'.format(123.45678))
print('{:.0f}'.format(123.45678))
print('{:-2f}'.format(123.45678))
print('{:-8f}'.format(123.45678))  # orginal nos
#print('{2:f}'.format(123.45678))  # error

print('{:^10s}'.format('Hi'))
print('{:^10s}'.format('Hi Dhiraj How are you'))  # center only 10 characters
print('{:^10s}'.format('abcdedfghi'))  # center only 10 characters


# right justify 
print('{:>6s}'.format('hi'))
print('{:>6s}'.format('there'))

#10.8 Nested Loops
for i in range(1,11):
    for  j in range(1,11):
        print('{:3d}'.format(i*j), sep=' ', end=' ')
    print()

# equation
for x in range(-50, 51):
    for y in range(-50,51):
        if 2*x + 3*y == 4 and x - y == 7:
            print(x,y, sep = ' ')

# pythograrous
count1=0
for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            if x**2 + y**2 == z**2:
                print(x,y,z)
                count1+=1
print('Solutions 1 ', count1)
# redundant (3,4,5) and (4,3,5) are same swapping x, y values
count2=0
for x in range(1,100):
    for y in range(x,100):
        for z in range(1,100):
            if x**2 + y**2 == z**2:
                print(x,y,z)
                count2 +=1
print(' Solutions 2 ' ,count2)
# some are multiples : (6,8,10) (9,12,15) x of (3,4,5)
count3=0
for x in range(1,100):
    for y in range(x,100):
        for z in range(y,100):
            if x**2 + y**2 == z**2:
                for i in range(2,x):
                    if x%i == 0 and y%i == 0 and z%i==0:
                        break
                else:
                    print(x,y,z)
                    count3 +=1
print(' Solutions 3 ' ,count3)
print(count1, count2, count3)
#100, 50, 16

"""
i=0
x=''.join([c*i for c in 'Python' for i in range(1,7)])
print(x)
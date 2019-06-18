# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 17:56:58 2017 by Dhiraj Upadhyaya
Chp-12 Text Files
"""
"""
#12.1 Reading from files
lines = [ line.strip() for line in open('example.txt')]
print(lines)
# strip() removes blank spaces from beginning & end
lines = [ du.strip() for du in open('example.txt')]
print(lines)

# will not work
lines = [ open('example.txt')]
print(lines)

# rstrip
lines = [ line.rstrip() for line in open('example.txt')]
print(lines)

#entire file as a string
s = open('example.txt').read()
print(s)
# different di open('c:/xxx/xxxx/example.txt').read()

#12.3 writing to files
f = open('writefile.txt','w')  # write mode overwritten contents
print('This is line1 ', file=f)
print('This is line2 ', file=f)
f.close()
# read the file
s = open('writefile.txt').read()
print(s)


#12.4 Examples
# read data for calc from 1 file and write to other
file1 = open('ftemps.txt', 'w')
temp = [line.strip() for line in open('temps.txt')]
for t in temp:
    print(int(t) * 9/5 + 32, file = file1)
file1.close()

s = open('ftemps.txt').read()
print(s)

questions = [ line.strip() for line in open('questions.txt')]
answers = [line.strip() for line in open('answers.txt')]

lines = [line.strip() for line in open('scores.txt')]
games = [line.split(',') for line in lines]
print(max([abs(int(g[11]) - int(g[12]))  for g in games]))

biggest_diff = 0
for g in games:
    diff = abs(int(g[11]) - int(g[12]))
    if diff > biggest_diff:
        biggest_diff = diff
        game_info = g
print(game_info)
# print all records
for g in games:
    print(g[0], g[1], g[2], sep=' ')


"""    
#12.4 Wordplay
wordlist = [line.strip() for line in open('wordlist.txt')]

"""
#print all 3 letter words
for word in wordlist:
    if len(word) >= 15:
        print(word, len(word), sep=' ')


for word in wordlist:
    if word[:1].upper() == 'K' or word[:1].upper() == 'R' :
        print(word)
print()
#% of words starting with vowel
count=0
for word in wordlist:
    if word[0].lower() in 'aeiou':
        count +=1
        print(word)
print("No of words starting with Vowel ", count )
print("% ", round(100*count / len(wordlist),2) , ' words Starting with Vowel' )

print()

# 7 letters words starting with
for word in wordlist:
    if len(word) == 7 and word[:2].upper() == 'AC' or word[-2:].upper() == 'AR':
        print(' Result is ', word, sep=' ')
# Print names
print(wordlist[0:3])  # 1st 3 names
i=0
while( i < 11):
    print(wordlist[i])
    i = i + 1
"""

# longest word that can be made only letters a b c d e
for word in wordlist:
    print(word, len(word), sep=' ')

for word in wordlist:
    for c in word:   # each character of word
        print(c, sep='', end='')
    print()

print()
largest = 0
for word in wordlist:
    for c in word:
        if c.lower() not in 'abcde':
            break
        else:
            if len(word) > largest:
                largest = len(word)
                largest_word = word
print("Largest Word is ", largest_word)



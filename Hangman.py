#Create Hangman game
#import libraries
import random
import re

#open sowpods file
fname = 'C:/Users/Oyinkan/Desktop/Python/Personal projects/sowpods.txt'
fhand = open(fname)

#count the number of words in sowpods dict
count =0
for line in fhand:
    count+=1

#select random number which will be used to select word to pick in sowpods 
rnumber = random.randint(0, count-1)

#pick a random word in sowpods
count= 0
with open(fname) as fhand:
    for line in fhand:
        count +=1
        if count == rnumber:
            rword = line.lower().strip()

#split the word to guess the letters in it
rword_list= list()
rword.split()
for letter in rword:
    rword_list.append(letter)

#calculate the number of letters in word
rword_len= len(rword_list)

#Let the user know how many letters in the word
print ('\nHint: The word contains {} letters\n'.format(rword_len))

dashed_list = list('_'*rword_len)

#allow 5 false guesses
count = 0
while count <5:
    guess= input('Please input your guess:')
    if guess in rword_list:
        for i, x in enumerate(rword_list):
            if x == guess:
                dashed_list[i]= rword_list[i]
        print('\nCorrect guess')
        print('\nThe current state of the word is:', str(dashed_list).strip('[]'))
    else:
        count+=1
        print('\nYou have', 5-count, 'more guesse(s)')
    if '_' not in dashed_list:
        print('You guessed the word rightly')
        break
    if count == 5:
        print('\nYou did not guess the word, the correct word is \'{}\''.format(rword))
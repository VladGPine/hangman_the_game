'''
This is a popular game. It called "H A N G M A N"
'''

import random


print('H A N G M A N')
print('Guess the word:')

languages_list = ['python', 'java', 'kotlin', 'javascript']

right_choice = random.choice(languages_list)
player_choice = input()

if right_choice == player_choice:
    print('You survived!')
else:
    print('You are hanged!')

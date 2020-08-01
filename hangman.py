'''
This is a popular game. It called "H A N G M A N"
'''

import random

languages_list = ['python', 'java', 'kotlin', 'javascript']
right_choice = random.choice(languages_list)
three_open_letters_word = (right_choice[:3] + '-' * (len(right_choice) - 3)).strip()

print('H A N G M A N')
print(f'Guess the word: {three_open_letters_word}')

player_choice = input()
if right_choice == player_choice:
    print('You survived!')
else:
    print('You are hanged!')

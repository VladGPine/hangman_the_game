'''
This is a popular game. It called "H A N G M A N"
'''

import random

languages_list = ['python', 'java', 'kotlin', 'javascript']
right_choice = random.choice(languages_list)
three_open_letters_word = (right_choice[:3] + '-' * (len(right_choice) - 3)).strip()
no_open_letters_word = '-' * len(right_choice)

print('H A N G M A N')
print()

counter = 8
while counter > 0:
    print(no_open_letters_word)
    print('Input a letter: ')

    player_choice = input()

    if player_choice not in right_choice:
        print('No such letter in the word')
    else:
        no_open_letters_word = list(no_open_letters_word)
        founded_indices = [k for k, x in enumerate(right_choice) if x == player_choice]
        for i in right_choice:
            for j in founded_indices:
                no_open_letters_word[j] = player_choice
        no_open_letters_word = ''.join(no_open_letters_word)

    counter -= 1
    print()

print('Thanks for playing!')
print("We'll see how well you did in the next stage")

# if no_open_letters_word == player_choice:
#     print('You survived!')
# else:
#     print('You are hanged!')

from random import randint
from numberguessinggameart import logo

def difficulty_level():
    choose_difficulty_level = input('Choose a difficulty. Type easy or hard -> ')
    if choose_difficulty_level == 'easy':
        return 10
    else:
        return 5
    
def compare(x, y):
    if x > y:
        print('Too high.')
    elif x < y:
        print('Too low.')
    else:
        print(f'You got it! The answer was {rm_number}.')

rm_number = randint(1, 100)
print(rm_number)

print(logo)
print('Welcome to the Number Guessing Game!')
print('I am thinking of a number between 1 and 100.')
    
attemps_remaining = difficulty_level()

while attemps_remaining != -1:
    print(f'You have {attemps_remaining} attempts remaining to guess the number.')
    user_guess = int(input('Make a guess -> '))
    compare(user_guess, rm_number)
    if user_guess != rm_number:
        attemps_remaining -= 1
    else:
        break    
    
    if attemps_remaining == 0:
        print('You have run out of guesses, you lose.')
        break


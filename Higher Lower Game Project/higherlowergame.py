from higherlowergamedata import data
import higherlowergameart
import random

score = 0

def my_function():
    item = random.choice(data)
    return item

def compare(a, b):
    user_guess = input('Who has more followers? Type A or B -> ')

    print('\n' * 20)

    print(higherlowergameart.logo)

    if user_guess == 'A':
        if a > b:
            return True
        else:
            return False
    if user_guess == 'B':
        if b > a:
            return True
    else:
        return False

itemB = my_function()

should_continue = True

while should_continue:   
    itemA = itemB
    itemB = my_function()
    
    followerCountA = itemA['follower_count']
    followerCountB = itemB['follower_count']

    print(higherlowergameart.logo)

    print(f'Compare A: {itemA['name']}, a {itemA['description']}, from {itemA['country']}.')

    print(higherlowergameart.vs)

    print(f'Against B: {itemB['name']}, a {itemB['description']}, from {itemB['country']}.')

    answer = compare(followerCountA, followerCountB)

    if answer == True:
        score += 1
        print(f'You are right! Current score {score}.')
    else:
        print(f'Sorry that is wrong. Final score: {score}.')
        should_continue = False
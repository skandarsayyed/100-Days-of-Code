import random

# Description
# A simple program for practicing loops in python

"""Easy Version"""

"""Ignore-start"""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
"""-end"""


tmp_contains = [] # each item from the lists are appended here for simplicity
user_password = '' # then each item of the list is converted into string

"""Loops-start""" 

for _ in range(nr_letters):
    tmp_contains.append(random.choice(letters))

for _ in range(nr_numbers):
    tmp_contains.append(random.choice(numbers))

for _ in range(nr_symbols):
    tmp_contains.append(random.choice(symbols))

for itemX in tmp_contains:
    user_password += itemX

"""-end"""

print(f'Your password -> {user_password}')
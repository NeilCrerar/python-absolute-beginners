'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: craps_roller.py
created on: May, 2017
@author: Neil_Crerar

Demonstrate random number generation
'''


import random

# generate random numbers 1 - 6
die1 = random.randint(1, 6)
die2 = random.randrange(6)+1

total = die1 + die2

print("You rolled a", die1, "and a", die2, " for a total of", total)

input("\n\nPress the enter key to exit")
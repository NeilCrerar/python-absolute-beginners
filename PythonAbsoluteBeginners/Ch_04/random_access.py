'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: random_access.py
created on: May, 2017
@author: Neil_Crerar

Demonstrates string indexing
'''

import random

word = "index"
print("The word is:", word, "\n")

high = len(word)
low = -len(word)

for i in range(10):
    position = random.randrange(low,high)
    print("word[", position, "]\t", word[position])

input("\n\nPress the enter key to exit.")
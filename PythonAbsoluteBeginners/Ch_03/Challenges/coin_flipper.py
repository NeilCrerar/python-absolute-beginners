"""
Python Programming For the Absolute Beginner, 3rd Edition
filename: coin_flipper.py
created on: May, 2017
@author: Neil_Crerar

Chapter 3, Challenge 2
Write a program that flips a coin 100 times and then tells you the number of heads and tails.
"""

import random

print("\tWelcome to the Coin Flipper program")
print("\nThis program will toss a coin 100 times and tell you the results")
input("Press the enter key to begin flipping the coin.\n\n")

counter = 1
heads = 0
tails = 0

while counter <=100:
    result = random.randint(1,2)
    if result == 1:
        print("Coin flip", counter, " landed as 'heads'")
        heads += 1
    else:
        print("Coin flip", counter, " landed as 'tails'")
        tails +=1
    counter += 1

print("\n\nThe coin landed as a 'heads' a total of", heads, "times.")
print("The coin landed as a 'tails' a total of", tails, "times.")

input("\n\nPress the enter key to exit.")

"""
Python Programming For the Absolute Beginner, 3rd Edition
filename: backwards_word.py
created on: May, 2017
@author: Neil_Crerar

Chapter 3, Challenge 2
Create a program that gets a message from the user and then prints it out 
backwards.
"""

print("Welcome to the backwards words program.")
print("Enter a word and see it printed out backwards.")

# Get a word from the user
word = input("\nWhat is your word? ")

# Create new string of the word backwards
backwards = ""

while word:
    letter = word[-1]
    backwards += letter
    word = word[:-1]

print("\nYour word backwards is ", backwards)

input("\n\nPress the enter key to exit.")

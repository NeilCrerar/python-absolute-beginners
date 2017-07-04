'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: random_words.py
created: 12 May, 2017
@author: user

Chapter 5, Challenge 1
Create a program that prints a list of words in random order.  The program 
should print all the words and not repeat any
'''

# Pseudocode for this program: 
# Create constant set of words to be printed out
# Print out words in original order
# Create a copy of the word list
# Loop until the copied list is empty
# Select a word at random from that list and print it 
# Remove that word from the copy list

# imports
import random

# Create constant set of words to be printed out
WORD_LIST = ("The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog")

# intrp text for the program
print("Welcome to the Word Scrambler program!")
print("This program takes a list of words and then randomises them without any repetitions.")
# Print out words in original order
print("The list of word to be randomised is:")
print(WORD_LIST)
input("\nPress the enter key to see the word list after it has been randomised")

# Create a copy of the word list by converting the original constant tuple to a list
randomised_words = list(WORD_LIST)
# Loop while the copied list is not empty
while len(randomised_words) != 0:
    # Select a word at random from that list and print it
    word = random.choice(randomised_words)
    print(word, end=" ")
    # Remove that word from the copy list
    randomised_words.remove(word)


input("\n\nPress the enter key to exit the program")
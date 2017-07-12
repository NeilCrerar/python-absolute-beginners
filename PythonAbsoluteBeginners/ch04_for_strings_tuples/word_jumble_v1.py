"""
Python Programming For the Absolute Beginner, 3rd Edition
filename: word_jumble_v1.py
created on: May, 2017
@author: Neil_Crerar

The computer picks a random word and then jumbles it.  The player then has to 
guess the original word.
"""

import random

# create sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

# pick one word randomly from the sequence
word = random.choice(WORDS)

# create a variable to use later to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble = ""

while word:
    # identify a random letter in the word
    position = random.randrange(len(word))
    # concatenate that letter and the existing jumble string
    jumble += word[position]
    # re-assign word as a  concatenation of the letters up to but not including the letter
    # position identified and the letters after the letter position to the end of the word
    word = word[:position] + word[(position+1):]

# start the game
print("""
           Welcome to Word Jumble!

     Unscramble the letters to make a word
(Press the enter key at the prompt to quit the game)
""")
print("\nThe jumble is:", jumble)

# get the users guess and evaluate it
guess = input("\nYour guess is: ")
while guess != correct and guess != "":
    print("Sorry, that's not it, please try again.")
    guess = input("\nYour guess is: ")

# congratulate the user when the guess is correct
if guess == correct:
    print("\nThats it! You guessed the word correctly!")

print("\nThanks for playing")

input("\n\nPress the enter key to exit.")


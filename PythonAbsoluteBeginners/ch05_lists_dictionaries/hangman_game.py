"""
Python Programming For the Absolute Beginner, 3rd Edition
filename: hangman_game.py
created: 12 May, 2017
@author: Neil_Crerar

The classic game of Hangman.The computer picks a random word and 
the player gets to guess it one letter at a time.  If the player 
can't guess in time, the little stick figure gets hanged. 
"""

# Imports
import random

# Create constant tuple for the hangman images
HANGMAN = (
    """
    """
    ,"""
  -------------
    """
    ,"""
    |
    |
    |
    |
    |
    |
    |
  -------------
    """
    ,"""
    ------
    |
    |
    |
    |
    |
    |
    |
  -------------
    """
    ,"""
    ------
    |     |
    |     O
    |    -+-
    |
    |
    |
    |
  -------------
    """
    ,"""
    ------
    |     |
    |     O
    |  ---+-
    |
    |
    |
    |
  -------------
    """
    ,"""
    ------
    |     |
    |     O
    |  ---+---
    |
    |
    |
    |
  -------------
    """
    ,"""
    ------
    |     |
    |     O
    |  ---+---
    |     |
    |     +
    |
    |
  -------------
    """
    ,"""
    ------
    |     |
    |     O
    |  ---+---
    |     |
    |    |+
    |    | 
    |
  -------------
    """
    ,"""
    ------
    |     |
    |     O
    |  ---+---
    |     |
    |    |+|
    |    | |
    |
  -------------
    """
    )

# Create constant for max no wrong guesses allowed
MAX_WRONG = len(HANGMAN) - 1

# Create constant tuple for words used in the game
WORDS = ("OVERUSED", "CLAM", "GUAM", "TAFFETA", "PYTHON", "EASY", "ANSWER", "XYLOPHONE"
"PENGUIN", "HOROSCOPE", "DIFFICULT", "TAXES", "DEATH", "JUMBLE", "WHITE", "NIGHT", "MOON", 
"KALEIDOSCOPE", "KITCHEN", "HIGHWAY", "RECORD", "METEOR", "MICROSCOPE", "PEBBLE", "PENDULUM", 
"RAINBOW", "COMPASS", "TEST", "RESTAURANT", "CRYSTAL", "POINT", "HABITUAL", "SELECTION", 
"FRANTIC", "FAMOUS", "HYSTERICAL", "AFTERNOON", "ABSTRACTED", "HELPFUL", "DEFECTIVE", "WHIRL",  
"ERRATIC", "AVOID", "BUILDING", "THREE","RESPECT", "RIGHTEOUS", "FIDDLER", "AARDVARK")
# Initialise variables
word = random.choice(WORDS) # The word selected for the game
so_far = "-" * len(word) # One dash for each letter in the word to be guessed
wrong = 0  # Number of wrong guesses the player has made
used = []  # Letter guessed by the player

# Intro text for the game
print("Welcome to the Hangman Game!")
print("----------------------------\n")

# Main program loop
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("You've used the following letters:\n", used)
    print("\nSo far, the word is:\n", so_far)
    
    # Get the player to guess a letter
    guess = input("\n\nEnter your guess: ")
    guess = guess.upper()
    
    # Check if the letter already been guessed already in the game
    while guess in used:
        print("You've already guessed the letter", guess)
        guess = input("Enter you letter: ")
        guess = guess.upper()
    used.append(guess)
    
    # Check if the letter is in the word
    if guess in word:
        print("\nYes!", guess, "is in the word!")
        
        # Create a new so_far to include the guess
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nSorry.", guess, "isn't in the word.")
        wrong += 1
    
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou've been hanged!")
else:
    print("\nYou guessed it!")

print("\nThe word was:", word)

input("\n\nPress the enter key to exit the program.")

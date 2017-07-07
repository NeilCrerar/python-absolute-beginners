"""
Python Programming For the Absolute Beginner, 3rd Edition
filename: word_guesser.py
created on: May, 2017
@author: Neil_Crerar

Chapter 3, Challenge 4
Create a game where the computer picks a random word and the player has to 
guess that word.  The computer tells the player how many letters are in the 
word.  Then the player gets five chances to ask if a letter is in the word. The 
computer can only respond with "yes" or "no". Then, the player must guess the 
word.
"""

# Import required modules
import random

# Create a list of words to select from
WORDS = ("easy", "answer", "xylophone", "penguin", "horoscope", "difficult", "taxes", "death", "python",
         "jumble", "white", "night", "moon", "kaleidoscope","kitchen", "highway", "record", "meteor",
         "microscope", "pebble", "pendulum", "rainbow", "compass", "test", "restaurant", "crystal",
         "point", "habitual", "selection", "frantic", "famous", "hysterical", "afternoon", "abstracted",
         "helpful", "defective", "erratic", "avoid", "whirl", "building", "three", "respect", "righteous")

# Select a word at random from the list
selected_word = random.choice(WORDS)

# Intro text for the program
print("\t\tWelcome to the word guessing game")
print("\t\t---------------------------------")
print("\nThe computer will pick a random word and tell you how many letters it contains.")
print("You can then ask about 7 different letters the word might contain and the computer will")
print("tell you if the word does contain those letters.  You must then try and guess the word.")
input("\nPress the enter key to start the game.")

# Show the list of words and say how many letters are in the word the computer has chosen
print("\nThe computer has chosen a word containing", len(selected_word), "letters")

# Create variables for what letters are and aren't in the word
in_word = ""
not_in_word = ""

# Loop for user asking if letter is in the word
for i in range(7):
    letter = input("What letter do you want to check is in the word? ")

    # validate if letter in word
    if letter.lower() in selected_word:
        print("The letter", letter, "is in the word.\n")
        in_word += letter.lower() + ", "
    else:
        print("Unfortunatley, the letter", letter, "is not the word.\n")
        not_in_word += letter.lower() + ", "

# Prompt user to guess the word
print("\nYou've now asked about the letters that might be in the word the computer has chosen.")
print("The word contains", len(selected_word), "letters of which", in_word, "are in the word and", not_in_word, "are not in the word.")
guess = input("You must now try and guess the word: ")

# Validate is users response is correct
if guess == selected_word:
    print("\nCongratulations, you have correctly guessed the word! You win!")
else:
    print("\nUnfortunately that was not the word the computer had chosen, you have lost.")
    print("The word that was chosen was'", selected_word,"'.")

input("\n\nPress the enter key to exit.")

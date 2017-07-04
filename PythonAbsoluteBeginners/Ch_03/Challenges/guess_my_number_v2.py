'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: guess_my_number_v2.py
created on: May, 2017
@author: user

Chapter 3, Challenge 3
Modify the Guess My Number game so that the player has a limited number of 
guesses.  If the player fails to guess in time, the program should display an 
appropriately chastising message.
'''

import random

# set the initial values
the_number = random.randint(1,100)
max_no_attempts = 7

print("\tWelcome to the 'Guess My Number' game!")
print("\nI'm thinking of a number between 1 and 100.")
print("You have", max_no_attempts, "attempts to try to guess it.\n")

for counter in range(max_no_attempts):
    guess = int(input("Take a guess: "))
    if guess > the_number:
        print("That's not the number I'm thinking of, it's lower than that.")
    elif  guess < the_number:
        print("That's not the number I'm thinking of, it's higher than that.")
    else:
        print("You guessed my number!  It was", the_number)
        if counter == 1:
            print("And it only took you one guess to get it!\n")
        else:
            print("And it only took you", counter + 1, "guesses to get it!\n")
else:
    print("You failed to guess my number, it's Game Over I'm afraid.")

input("\n\nPress the enter key to exit.")
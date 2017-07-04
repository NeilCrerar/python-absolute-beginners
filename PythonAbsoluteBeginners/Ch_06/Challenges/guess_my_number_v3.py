'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: guess_my_number_v3.py
created on: 19 May, 2017
@author: user

Chapter 6, Challenge 2
Modify the Guess My Number chapter project from Chapter 3 by re-using the 
function: ask_number().  
NOTE: Also added additional game text to tell the player how many guesses they
have left in the game.
'''

# import required modules
import random

# set the initial values
LOWER_RANGE = 0
HIGHER_RANGE = 100
the_number = random.randint(LOWER_RANGE,HIGHER_RANGE)
MAX_ATTEMPTS = 7


def get_player_guess(question, low, high):
    """Ask for a number within a range"""
    response = None
    while response not in range(low, high): 
        response = int(input(question))
    return response

# print game instructions to screen
print("\nWelcome to the 'Guess My Number' game.")
print("\nThe computer will pick a number at random between", LOWER_RANGE,\
      "and", HIGHER_RANGE)
print("You have", MAX_ATTEMPTS, "attempts to try to guess what it is.\n")

# control loop giving player multiple attempts to guess the number
for counter in range(MAX_ATTEMPTS):
    # get the guess from the player
    guess = get_player_guess("Take your guess: ", LOWER_RANGE, HIGHER_RANGE)
    # evaluate the players guess and output higher/lower response
    if guess > the_number:
        print("That's not the number I'm thinking of, it's lower than that.")
        print("Number of guesses left is:", MAX_ATTEMPTS - (counter + 1), "\n")
    elif  guess < the_number:
        print("That's not the number I'm thinking of, it's higher than that.")
        print("Number of guesses left is:", MAX_ATTEMPTS - (counter + 1), "\n")
    else:
        print("You guessed my number!  It was", the_number)
        # implement a modified message for getting it on the first guess
        if counter == 1:
            print("And it only took you one guess to get it!\n")
            break
        else:
            print("And it only took you", counter + 1, "out of",\
                  MAX_ATTEMPTS, "guesses to get it right!\n")
            break
else:
    print("You failed to guess my number, it was", the_number)
    print("That means it's Game Over I'm afraid.")
    
input("\n\nPress the enter key to exit.")

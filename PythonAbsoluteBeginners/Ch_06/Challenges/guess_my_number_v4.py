'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: guess_my_number_v4.py
created on: 22 May, 2017
@author: user

Chapter 6, Challenge 3
Modify the new version of Guess My Number you created in the last challenge so
that the programs code is in a function called main().  Don't forget to call 
main() so that you can play the game.
NOTE: I've also put the game instructions in a function as well just for the 
practice
'''

# import required modules
import random

# set the initial values
LOWER_RANGE = 0
HIGHER_RANGE = 100
the_number = random.randint(LOWER_RANGE,HIGHER_RANGE)
MAX_ATTEMPTS = 7


def game_instructions():
    print("\nWelcome to the 'Guess My Number' game.")
    print("\nThe computer will pick a number at random between", LOWER_RANGE,\
          "and", HIGHER_RANGE)
    print("You have", MAX_ATTEMPTS, "attempts to try to guess what it is.\n")


def get_player_guess(question, low, high):
    """Ask for a number within a range"""
    response = None
    while response not in range(low, high): 
        response = int(input(question))
    return response


def main():
    game_instructions()
    for counter in range(MAX_ATTEMPTS):
        guess = get_player_guess("Take your guess: ", LOWER_RANGE,\
                                 HIGHER_RANGE)
        if guess > the_number:
            print("That's not the number I'm thinking of,"\
                  "it's lower than that.")
            print("Number of guesses left is:", MAX_ATTEMPTS - (counter + 1),\
                   "\n")
        elif  guess < the_number:
            print("That's not the number I'm thinking of,"\
                  " it's higher than that.")
            print("Number of guesses left is:", MAX_ATTEMPTS - (counter + 1),\
                   "\n")
        else:
            print("You guessed my number!  It was", the_number, end=" ")
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
    
main()
input("\n\nPress the enter key to exit.")

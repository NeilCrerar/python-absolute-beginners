'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: reveresed_my_number.py
created on: May, 2017
@author: Neil_Crerar

Chapter 3, Challenge 4
Write the pseudocode for a program where the player and the computer trade 
places in the number guessing game.  That is, the player picks a random number
between 1 and 100 and the computer has to guess.  Before you start, think 
about how you guess.  If all goes well, try coding the game.
'''
###############################################################################
# Introduce the program and specify the rules
# Prompt user to select a number to continue
# Computer makes first guess as number halfway between the upper and lower bounds
# User evaluates guess and informs Computer if lower or higher
# Loop: Computer uses feedback to create binary chop process
#   If higher, set guess as lower boundary
#   If lower, set guess to upper boundary
###############################################################################

# set the initial values
upper_boundary = 100
lower_boundary = 0
guess = 50

# program instructions
print("\tWelcome to the 'Reversed Guess My Number' game!")
print("\t-----------------------------------------------\n")
print("The user will think of a number between 1 and 10 which the computer will try and guess.\n")
print("On each guess from the computer, the user can respond:")
print("  'L' if the number is lower than the computers guess")
print("  'H' if the number is higher than the computers guess")
print("  'C' if the number has been successfully guessed by the computer\n")
input("Once you have though of a number, press enter to start the game...")

print("\nThe computers first guess is... ", guess)
response = input("Enter C-guessed correctly, H-it's higher than that, or L-it's lower than that. ")

# guessing loop - uses binary chop to refine the guessing
while response != "C":
    if response == "L":
        upper_boundary = guess
    elif response == "H":
        lower_boundary = guess
    else:
        print("I didn't recognise that input?  What are you doing?")
        
    guess = int(((upper_boundary - lower_boundary) / 2) + lower_boundary)
    print("\nThe computers guess is... ", guess)
    # print("--debug: new boundaries are", lower_boundary ,"to", upper_boundary)
    response = input("Has it guessed the number (C) or is it higher (H) or lower (L) than that? ")

print("\n\nWoohoo, the computer got it right!!\n\n")
    
input("Press the enter key to exit.")


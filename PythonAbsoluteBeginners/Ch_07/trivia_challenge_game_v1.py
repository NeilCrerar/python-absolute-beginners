'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: trivia_challenge_game_v1.py
created on: 19 Jun, 2017
@author: user

Trivia challenge game that reads from a plain text file containing the 
questions to be asked.
'''

# Declare imports
import sys


def open_file(file_name, mode):
    """
    Verify can open a file containing the trivia questions to be used.    
    :param file_name: the name of the question file to be used
    :param mode: the mode in which the question file is to be used
    :returns: the name of the file it was first passed
    :raises IOError: raises an exception for file not found
    """   
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else: 
        return the_file


def next_line(the_file):
    """
    Return next line from the supplied question file, formatted.
    :param the_file: name of the file to read from
    :returns: the question file title line
    """
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line


def next_block(the_file):
    """
    Return the next block of text from the supplied question file
    :param the_file: name of the file to read from
    :returns:  multiple variables representing different parts of the question
    """ 
    category = next_line(the_file)
    question = next_line(the_file)
    # Read answer lines and save into a list
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    return category, question, answers, correct, explanation


def welcome(title):
    """
    Welcome screen for the game that also displays the question area title.
    :param title: the title line for the question area
    """
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")


def main():
    """
    Main game loop
    """
    # Open question file and get question area title
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    # Welcome player and initialise score
    welcome(title)
    score=0
    # Get first question block
    category, question, answers, correct, explanation = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])
        # Get answer from player
        answer = input("What is your answer?: ")
        # Check the answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += 1
        else:
            print("\nWrong!", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")
        # Get next question block
        category, question, answers, correct, \
        explanation = next_block(trivia_file)
    # Close the question file, end the game and display final score
    trivia_file.close()
    print("That was the last question!")
    print("Your final score is", score)

# Start the game
main()
   
# Default program exit control code
input("\n\nPress the enter key to exit.")

'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: trivia_challenge_game_v2a.py
created on: 20 Jun, 2017
@author: user

Chapter 7, Challenge 1
Improve the previous Trivia Challenge game so that each question has a unique 
point value associated with it.  Th3e players score should be the total of all 
of the points values of the questions he or she answer correctly.
Solution implemented is to have an accumulator that starts at 1 and increased 
by 2 for each correct but resets to 1 if a wrong answer is given.  This is then 
added to the score as questions answered correctly.
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
    # Open question file
    trivia_file = open_file("trivia01.txt", "r")
    title = next_line(trivia_file)
    # Welcome player and initialise score and accumulator
    welcome(title)
    score=0
    accumulator = 1    
    # Get first question block
    category, question, answers, correct, explanation = next_block(trivia_file)
    while category:
        # Ask a question
        print(category)
        if accumulator == 1:
            print("This question is worth", accumulator, "point.")
        else:
            print("This question is worth", accumulator, "points.")
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])        
        # Get answer from player
        player_answer = input("What is your answer?: ")
        # Check the players answer
        if player_answer == correct:
            print("\nRight!", end=" ")
            score += accumulator
            accumulator +=2
        else:
            print("\nWrong!", end=" ")
            accumulator = 1
        print(explanation)
        print("Score:", score, "\n\n")
        # Get next question block
        category, question, answers, correct, \
        explanation = next_block(trivia_file)
    # Close the question file, end the game and display final score
    trivia_file.close()
    print("That was the last question!")
    print("Your final score is", score)


main()
input("\n\nPress the enter key to exit.")
'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: trivia_challenge_game_v3.py
created on: 21 Jun, 2017
@author: Neil_Crerar

Chapter 7, Challenge 2
Improve the previous Trivia Challenge game so that it maintains a high-scores 
list in a file.  THe program should record the players name and score if the 
player makes the list.  Store the high scores using a pickled object.
NOTE: This program doesn't account for matching lowest scores.  If match 
current lowest score then new score replaces old one.

NOTE: Originally written with rb+ and a single check and update high score 
function to save on number times opening and closing high score file but despite 
getting logic working, couldn't get the updated high scores to write to file 
- always retrieved the original content when display high score table? 
'''

# Declare imports
import sys
import pickle


def open_file(file_name, mode):
    """
    Verify can open a file containing the trivia questions to be used.    
    :param file_name: the name of the question file to be used
    :param mode: the mode in which the question file is to be used
    :returns: the name of the file it was first passed
    :raises IOError: if supplied filename is not found
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


def display_high_scores():
    """
    Displays the current top 5 high scores for the game
    """
    f = open("high_scores.dat", "rb")
    high_scores = pickle.load(f)
    print("\n\nCurrent High Scores")
    print("-------------------")
    print("NAME\t\tSCORE")
    for entry in high_scores:
        score, name = entry
        print(name, "\t\t", score)
    f.close()


def high_sore_check(score):
    """
    Check if current score to go into high score list and adds if needed
    :param score: score from the current game
    """
    # Verify can open high score file
    f = open_file("high_scores.dat", "rb")
    high_scores = pickle.load(f)
    f.close()
    high_scores.sort(reverse = True)
    lowest_score = high_scores[9][0]
    if score >= lowest_score:
        print("Congratulations, you've made the high-score list!")
        name = input("Enter your name: ")
        # Entry created in this order to allow sorting on high score table
        entry = [score, name]
        high_scores.append(entry)
        high_scores.sort(reverse = True)
        new_high_scores = high_scores[:10]  # keep only the top 5 scores
        f = open("high_scores.dat", "wb")
        pickle.dump(new_high_scores, f)
        f.close()   
    else:
        print("Unfortunately your score wasn't good enough to make it onto"\
              " the high score list.  Better luck next time!")


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
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])        
        # Get answer from player
        if accumulator == 1:
            print("Your current score is:", score,\
                  "and this question is worth", accumulator, "point.")
        else:
            print("Your current score is:", score,\
                  "and this question is worth", accumulator, "points.")
        answer = input("What is your answer?: ")       
        # Check the answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += accumulator
            accumulator +=2
        else:
            print("\nWrong!", end=" ")
            accumulator = 1
        print(explanation, "\n\n")
        # Get next question block
        category, question, answers, correct, \
        explanation = next_block(trivia_file)    
    # Close the question file, and display final score
    trivia_file.close()
    print("That was the last question!")
    print("Your final score is", score)    
    # Check for new high-score and add if required
    high_sore_check(score)
    display_high_scores()


main()
input("\n\nPress the enter key to exit.")
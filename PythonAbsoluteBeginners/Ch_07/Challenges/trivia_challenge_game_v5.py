'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: trivia_challenge_game_v5.py
created on: 22 Jun, 2017
@author: Neil_Crerar

Chapter 7, Challenge 4
Create a trivia game episode that tests a players knowledge of python files and
exceptions

NOTE: This program holds high scores in a binary file and doesn't account for 
matching lowest scores. If match current lowest score then new score simply 
replaces the old one.

NOTE: This also resolves the rb+ overwrite issue seen in Version 3
'''

# Declare imports
import sys
import pickle

# Declare defaults
hscore_file = "high_scores.dat"


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


def next_line(trivia_file):
    """
    Return next line from the supplied question file, formatted.
    :param trivia_file: name of the file to read from
    :returns: the question file title line
    """
    line = trivia_file.readline()
    line = line.replace("/", "\n")
    return line


def next_block(trivia_file):
    """
    Return the next block of text from the supplied question file
    :param trivia_file: name of the file to read from
    :returns: multiple variables representing different parts of the question
    """ 
    category = next_line(trivia_file)
    question = next_line(trivia_file)
    answers = []
    for i in range(4):
        answers.append(next_line(trivia_file))
    correct = next_line(trivia_file)
    if correct:
        correct = correct[0]
    explanation = next_line(trivia_file)
    return category, question, answers, correct, explanation


def display_high_scores(hscore_file):
    """
    Displays the current top 5 high scores for the game
    :param hscore_file: The name of the high score file
    """
    f = open(hscore_file, "rb")
    high_scores = pickle.load(f)
    print("\n\nCurrent High Scores")
    print("-------------------")
    print("NAME\tSCORE")
    for entry in high_scores:
        score, name = entry
        print(name, "\t", score)
    f.close()


def high_sore_check(score, hscore_file):
    """
    Check if current score to go into high score list and adds if needed
    :param score: score from the current game
    :hscore_file: the name of the high score file
    """
    f = open(hscore_file, "rb+")
    high_scores = pickle.load(f)
    high_scores.sort(reverse = True)
    lowest_score = high_scores[9][0]
    if score >= lowest_score:
        print("Congratulations, you've made the high-score list!")
        name = input("Enter your name: ")
        # entry created in this order to allow sorting on high score table
        entry = [score, name]
        high_scores.append(entry)
        high_scores.sort(reverse = True)
        new_high_scores = high_scores[:10]  # keep only the top 5 scores
        
        # Had to put this seek in to overwrite the existing high scores content
        # with the new scores - this requirement not mentioned in the book!!
        f.seek(0,0)
        pickle.dump(new_high_scores, f)
        f.close()   
    else:
        print("Unfortunately your score wasn't good enough to make it onto" \
              " the high score list.  Better luck next time!")
        f.close()
    

def welcome():
    """
    Welcome screen and prompt for question area.
    :param title: the title line for the question area
    :returns: question file to be used for the quiz
    """
    print("\t\tWelcome to Trivia Challenge!")
    print("\t\t----------------------------\n")
    print("We have the following question categories to choose from:\n")
    print("\t1 - The Mafia")
    print("\t2 - Exceptions in Python")
    print("\t3 - Files in Python")
    # Get menu choice and set corresponding trivia file
    choice = input("\nSelect an option: ")
    if choice == "1":
        question_area = "trivia01.txt"
    elif choice == "2":
        question_area = "trivia03.txt"
    elif choice == "3":
        question_area = "trivia04.txt"
    else:
        print("That entered menu option was invalid.")
    return question_area


def main():
    """
    Main game loop
    """
    # Welcome player and initialise variables
    question_area = welcome()
    score=0
    accumulator = 1
    # Open question file and get first block of content
    trivia_file = open_file(question_area, "r")
    title = next_line(trivia_file)
    print("\n\n", title, "\n")
    category, question, answers, correct, explanation = next_block(trivia_file)
    # Print question and get answer
    while category:
        print(category, end="")
        if accumulator == 1:
            print("Your current score is", score,\
                  "and this question is worth", accumulator, "point.\n")
        else:
            print("Your current score is", score,\
                  "and this question is worth", accumulator, "points.\n")
        print("Question:", question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])
        player_answer = input("What is your answer?: ")
        # Get players answer
        if player_answer == correct:
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
    # Check for new high-score and display current high scores
    high_sore_check(score, hscore_file)
    display_high_scores(hscore_file) 


main()
input("\n\nPress the enter key to exit.")
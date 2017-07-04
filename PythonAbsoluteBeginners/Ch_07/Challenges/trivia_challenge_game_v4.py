'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: trivia_challenge_game_v4.py
created on: 21 Jun, 2017
@author: user

Chapter 7, Challenge 3
Improve the previous Trivia Challenge game so that it maintains a high-scores 
list in a file.  THe program should record the players name and score if the 
player makes the list.  Store the high scores using a plain text file.
NOTE: This program doesn't account for matching lowest scores.  If match 
current lowest score then new score replaces old one
'''

# Declare imports
import sys


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


def open_high_scores_to_list():
    """
    Converts text file of high scores to paired list
    :returns: paired list of score/name
    """
    # Verify can open high score file
    high_score_file = open_file("high_scores.txt", "r")    
    # Convert text file to sorted list pairs of scores/players then return
    high_scores = []
    for line in high_score_file:
        line = line.replace("\n", "")
        entry = line.split(":")
        high_scores.append(entry)    
    high_score_file.close()
    for i in range(len(high_scores)):
        high_scores[i][0] = int(high_scores[i][0])     
    high_scores.sort(reverse = True)
    return high_scores


def save_high_scores_to_text(scores_to_save):
    """
    Converts list of high scores to text and writes to file
    :param scores_to save: list of high scores to be saved
    """
    high_score_file = open("high_scores.txt", "w")
    for i in range(len(scores_to_save)):
        player_score = scores_to_save[i][0]
        player_name = scores_to_save[i][1]
        entry = str(player_score) + ":" + player_name + "\n"
        high_score_file.write(entry)
    high_score_file.close()


def display_high_scores():
    """
    Displays the current high scores for the game
    """
    high_scores = open_high_scores_to_list()
    print("\n\nCurrent High Scores")
    print("-------------------")
    print("NAME\t\tSCORE")
    for entry in high_scores:
        score, name = entry
        print(name, "\t\t", score)


def high_sore_check(score):
    """
    Check if current score to go into high score list and adds if needed
    :param score: score from the current game
    :raises IndexError: if high scores list is wrong length
    """
    # Get high_scores as a sorted list
    high_scores = open_high_scores_to_list()    
    # Check returned list is populated with score data 
    try:
        lowest_score = high_scores[9][0]
    except IndexError as e:
        print("Unable to access the high scores. Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    # Check if current score better than lowest current high score
    if score >= lowest_score:
        # Congratulate user, get their name, create new high score entry
        print("Congratulations, you've made the high-score list!")
        name = input("Enter your name: ")
        # Entry created in this order to allow sorting on high score table
        entry = [score, name]
        # Add new high score to high score list and re-order
        high_scores.append(entry)
        high_scores.sort(reverse = True)
        new_high_scores = high_scores[:10]  # Keep only the top 10 scores
        save_high_scores_to_text(new_high_scores) # Write new scores to file
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
            print("Your current score is", score,\
                  "and this question is worth", accumulator, "point.")
        else:
            print("Your current score is", score,\
                  "and this question is worth", accumulator, "points.")
        player_answer = input("What is your answer?: ")
        # Check the answer
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
    # Check for new high-score and add if required
    high_sore_check(score)
    display_high_scores() 


main() 
input("\n\nPress the enter key to exit.")
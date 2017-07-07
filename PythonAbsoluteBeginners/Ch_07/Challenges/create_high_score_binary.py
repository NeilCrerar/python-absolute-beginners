"""
Python Programming For the Absolute Beginner, 3rd Edition
filename: create_high_score_binary
created on: 22 Jun, 2017
@author: Neil_Crerar

Chapter 7 Challenge helper file
Creates a default high score binary file for the Trivia Challenge game 
"""

# Define imports
import pickle

# Create list of scores and pickle to file
scores = [[1,"Rita"],[1,"Kurt"],[1,"Aaron"],[1,"Susie"],[3,"Annie"],[5,"Alex"],
     [7,"Eric"],[8,"Basil"],[9,"Susan"],[6,"Jane"]]

f = open("high_scores.dat", "wb")
pickle.dump(scores, f)
f.close()

print("File created.")
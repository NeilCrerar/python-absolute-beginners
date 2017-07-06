'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: high_scores_v1.py
created: 11 May, 2017
@author: Neil_Crerar

Demonstrates list methods
'''

scores = []
choice = None

while choice != "0":
    print("""
    High Scores
    -----------
    
    0 - Exit
    1 - Show Scores
    2 - Add A Score
    3 - Delete A Score
    4 - Sort Scores
    """)

    choice = input("Select an option: ")
    print()

    # exit program
    if choice == "0":
        print("Thanks for playing, good bye.")
    # list high-score table
    elif choice == "1":
        print("High Scores")
        for score in scores:
            print(score)
    # add a score
    elif choice == "2":
        score = input("What score did you get? ")
        scores.append(score)
    # remove a score
    elif choice == "3":
        score = int(input("Which score do you want to remove? "))
        if score in scores:
            scores.remove(score)
    # sort the scores
    elif choice == "4":
        scores.sort(reverse = True)
    # handle invalid choices
    else:
        print("Sorry, but", choice, "is not a valid choice.")


input("\n\nPress the enter key to exit the program.")

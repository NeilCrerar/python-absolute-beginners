'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: high_scores_v2.py
created: 12 May, 2017
@author: user

Demonstrates the use of nested sequences
'''

scores = []
choice = None

while choice != "0":
    print("""
    High Scores v2.0
    ----------------
    
    0 - Exit
    1 - List Scores
    2 - Add A Score
    """)

    # prompt user to select a menu option
    choice = input("Select an option: ")
    print()

    # exit program
    if choice == "0":
        print("Thanks for playing, good bye.")
    
    # display high score table
    elif choice == "1":
        print("High Score Table")
        print("----------------")
        print("NAME\tSCORE")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)
        # seems the wrong way round but is needed in this order for later sorting
    
    # add a new score
    elif choice == "2":
        name = input("Enter the players name: ")
        score = int(input("Enter the players score: "))
        # entry created in this order to allow sorting to create the high score table
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse = True)
        scores = scores[:5]  # keep only the top 5 sorted scores 
    
        # handle invalid choices
    else:
        print("Sorry, but", choice, "is not a valid choice.")

input("\n\nPress the enter key to exit the program.")

        
        
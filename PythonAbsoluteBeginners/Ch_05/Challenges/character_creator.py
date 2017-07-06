'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: character_creator.py
created: 12 May, 2017
@author: Neil_Crerar

Chapter 5, Challenge 2
Write a Character Creator program for a role playing game.  The player should 
be given a pool of 30 points to spend on four attribute: Strength, Health, 
Wisdom and Dexterity.  The player should be able to spend points from the pool
on any attribute and take points from any attribute and return them to the 
pool.
'''

# Program pseudocode......
# Will closely mimic that from the high_score programs
# Have list with each element having two components like the high score 2 program
# Elements relate to the attribute and points allocated plus the pool
# Menu options for assign or reclaim points
#   - Both options ask for attribute then the points to move
#   - Assigning should verify against pool that there are enough points
#   - Reclaiming does same against what is currently allocated to the attribute
# Include menu option to quit
# Include menu protection against invalid choices
# After each action print out the current status for pool and attributes 

# implement variables
allocations = [["Health", 1], ["Strength", 2], ["Wisdom", 3], ["Dexterity", 4], 
               ["Pool", 30]]
choice = None

# intro text for program
print("\tCharacter Creator")
print("\t-----------------")
print("\nWelcome to the Character Creator program.")
print("You have a pool of 30 character points to allocate to four different attributes.")
print("You can move points in and out of the pool and attributes using the menu below.\n\n")

# main program loop
while choice != "0":
    print("""Main Menu
---------
What would you like to do?
  0 - Exit
  1 - Add points to an attribute
  2 - Take points away from an attribute
  3 - View current character statistics
""")
    # prompt user to select a menu option
    choice = input("\nSelect an option: ")
    print()

    # Menu 0: Exit program
    if choice == "0":
        print("\nThanks for playing, good bye.")
    
    # Menu 1: Add points to an attribute
    elif choice == "1":
        
        # print sub-menu
        print("\nAdd Pool Points")
        print("---------------")
        print("Your character has the following attributes and points allocated:")
        print("  1 - Health (",allocations[0][1], ")")
        print("  2 - Strength (", allocations[1][1], ")")
        print("  3 - Wisdom (", allocations[2][1], ")")
        print("  4 - Dexterity (", allocations[3][1], ")")
        
        # prompt user to select a menu option
        add_choice = int(input("\nWhich attribute do you want to add points to? "))
        attribute = add_choice -1
        
        # prompt user to enter the number of points to add to the attribute
        if attribute in range(4):
            points_to_add = int(input("How many points do you want to add to this attribute? "))
            current_points = allocations[attribute][1]
            
            # check there's enough points in the pool to add
            if points_to_add <= allocations[4][1]:
                # set the new points value for the attribute 
                allocations[attribute][1] = current_points + points_to_add
                print("\n",points_to_add, "points have been added to the attribute.")
                print("It now has", allocations[attribute][1], "points assigned to it.")
                # remove the added points from the pool
                pool_points = allocations[4][1]
                allocations[4][1] = pool_points - points_to_add
                print("There are also now", allocations[4][1], "pool points available.\n\n")
            else:
                # inform user action cannot be performed
                print("\nYou do not have that enough points in the pool for that.")
                print("Try re-allocating some back to the pool from another attribute.\n\n")

        # handle invalid menu choices being entered
        else:
            print("\nSorry, but", choice, "is not a valid choice.")

    # Menu 2: Re-allocate points back to the pool
    elif choice =="2":
        #print sub-menu
        print("\nRe-Allocate Points Back to the Pool")
        print("-----------------------------------")
        print("Your character currently has the following attributes and points allocated:")
        print("  1 - Health (",allocations[0][1], ")")
        print("  2 - Strength (", allocations[1][1], ")")
        print("  3 - Wisdom (", allocations[2][1], ")")
        print("  4 - Dexterity (", allocations[3][1], ")")
        remove_choice = int(input("Which attribute do you want to re-allocate points from? "))
        attribute = remove_choice -1
        
        # prompt user to enter the number of points to add to the attribute
        if attribute in range(4):
            points_to_remove = int(input("How many points do you want to re-allocate? "))
            current_points = allocations[attribute][1]
            
            # check there's enough points currently assigned to the attribute
            if points_to_remove <= current_points:
                # set the new points value for the attribute 
                allocations[attribute][1] = current_points - points_to_remove
                print("\n", points_to_remove, "points have been reallocated from the attribute.")
                print("It now has", allocations[attribute][1], "points assigned to it.")
                # remove the added points from the pool
                pool_points = allocations[4][1]
                allocations[4][1] = pool_points + points_to_remove
                print("There are also now", allocations[4][1], "pool points available.\n\n")                
            else:
                # inform user action cannot be performed
                print("\nThats more points than that attribute has currently assigned.")
                print("Try splitting the points to re-allocating from multiple attributes.\n\n")

        # handle invalid menu choices being entered
        else:
            print("\nSorry, but", choice, "is not a valid choice.")

    # Menu 3: Display character statistics
    elif choice == "3":
        print("\nYour current character statistics are:")
        print("\nATTRIBUTE\tPOINTS")
        print("----------------------")
        print("Health:\t\t", allocations[0][1])
        print("Strength:\t", allocations[1][1])
        print("Wisdom:\t\t", allocations[2][1])
        print("Dexterity:\t", allocations[3][1])
        print("\nAvailable pool points: ", allocations[4][1], "\n\n")

    # handle invalid menu choices being entered
    else:
        print("\nSorry, but", choice, "is not a valid choice.")


# prompt to exit the program
input("\n\nPress the enter key to exit the program.")

"""
Python Programming For the Absolute Beginner, 3rd Edition
filename: whos_your_grandaddy_v2.py
created: 18 May 18, 2017
@author: Neil_Crerar

Chapter 5, Challenge 4 - alternative solution
Improve the Who's Your Daddy? program by adding a choice that lets the user
enter a name and get back a grandfather.  Your program should still only use 
one dictionary of son-father pairs.  Make sure to include several generations
in your dictionary so that a match can be found.

NOTE: Variation on this challenge where use a nested dictionary to achieve the
same outcome as extending the dictionary.
"""

#NOTE TO SELF - to see the entries listed under a given son is...
#print("Full entry for a son is:", register["son"])
#To see the first nested value under a son is...
#print("The Father entry for a son is:", register["son"]["father"])
#To see the second nested value under a son is...
#print("The Grandfather entry for a son is:", register["son"]["grandfather"])

# create dictionary for paternal pairings in format {son: {father: grandfather}}
register ={"son": {"father": "Mr Smith", "grandfather": "Mr Smith Snr"}
    ,"John Smith": {"father": "Bob Smith", "grandfather": "Grandfather Smith"}
    ,"David Kilroy": {"father": "Samuel Kilroy", "grandfather": "Grandfather Kilroy"}
    ,"Michael Douglas": {"father": "Kirk Douglas", "grandfather": "Grandfather Douglas"}
    ,"Kiefer Sutherland": {"father": "Donald Sutherland", "grandfather": "Grandfather Sutherland"}
    ,"Charlie Sheen": {"father": "Martin Sheen", "grandfather": "unknown"}
    ,"Jaden Smith": {"father": "Will Smith", "grandfather": "unknown"}
    ,"David Carradine": {"father": "John Carradine", "grandfather": "unknown"}
    ,"Scott Caan": {"father": "James Caan", "grandfather": "Grandfather Caan"}   
    }


print("""Paternal Lookup Register
--------------------------------
This register records listings of paternal family lines for son-father-grandfather
relationships.  The register can be queried by entering the name of the 'son' to 
identify the father and grandfather.""")

menu_choice = None
while menu_choice != "0":
    print("""
--------------------------------
    Menu
    ----
    1 - Display all son/father/grandfather listings
    2 - Look up a son/father/grandfather listing
    3 - Add a new son/father/grandfather listing
    4 - Edit a son/father/grandfather listing
    5 - Delete a son/father/grandfather listing
    
    0 - Quit
    """)
    # Get term to look up from user
    menu_choice = input("Please select a menu option: ")

    # Exit the program
    if menu_choice == "0":
        print("Thank you for using this program.  Good Bye.")

    elif menu_choice == "1":
        print("\nThe son, father and grandfather listings currently recorded in the register are:")
        # Print every entry in the register dictionary
        for son in register:
            print("  ", son, "is the son of", register[son]["father"],\
                  "and the grandson of", register[son]["grandfather"])

    elif menu_choice == "2":
        # Get the name of the son
        son = input("\nEnter the son's name: ")
        # Use title capitalisation as that's how the dictionary is setup
        if son.title() in register:
            generation_choice = input("Do you want to see the father (F),"\
                                      "the grandfather (G) or both (B) ?")
            if generation_choice.upper() == "F":
                # Note still have to do the title conversion when looking up 
                # in the dictionary via dictionary[key]
                print("\nThe father of", son.title(), "is",\
                      register[son.title()]["father"])
            elif generation_choice.upper() == "G":
                print("\nThe father of", son.title(), "is",\
                      register[son.title()]["grandfather"])
            elif generation_choice.upper() == "B":
                print("The father of", son.title(), "is", \
                      register[son.title()]["father"], end=" ")
                print("and the grandfather is", register[son.title()]["grandfather"], "\n")
            else:
                print("That was not a valid choice!\n")
        else:
            print("That name does not exist in the register, you may want to add it.\n")

    elif menu_choice == "3":
        son = input("\nEnter the name of the son to be added: ")
        if son.title() not in register:
            father = input("Enter the name of the father to be added for that son: ")
            add_choice = input("Do you also want to add a grandfather for that son?"\
                               "('Y' to add or any other key to return to the main menu).")
            if add_choice.upper() == "Y":
                grandfather = input("Enter the name for the grandfather in this pairing: ")
                # Create new entry with the entered son, father and grandfather
                # names and add to the dictionary
                register[son.title()] = {"father": father.title(),\
                                         "grandfather": grandfather.title()}
                # Print out confirmation of the new entry being created
                print(son.title(), "the son of", father.title(),"and grandson of",\
                      grandfather.title(), "has been added.\n")
            else:
                # Create new entry with the entered son, father and grandfather 
                # names and add to the dictionary
                register[son.title()] = {"father": father.title(),\
                                         "grandfather": "unknown"}
                # Print out confirmation of the new addition
                print(son.title(), "the son of", father.title(),\
                      "has been added but the grandfather has " \
                      "not been recorded.\n")
        else:
            print("That name is is already recorded in the register.\n")
            
    elif menu_choice == "4":
        son = input("\nEnter the name of the son who's entry you want to edit: ")
        if son.title() in register:
            generation_choice = input("Do you want to edit the father (F),"\
                                      "grandfather (G) or both (B)?")
            if generation_choice.upper() == "F":
                # Still have to do the title conversion when looking up in
                # the dictionary via dictionary[key]
                father = input("Enter the name for the new father in this pairing: ")
                register[son.title()]["father"] = father.title()
                print("The father for", son.title(), "has been updated.\n")
            elif generation_choice.upper() == "G":
                grandfather = input("Enter the name for the new grandfather in this pairing: ")
                register[son.title()]["grandfather"] = grandfather.title()
                print("The grandfather for", son.title(), "has been updated.\n")
            elif generation_choice.upper() == "B":
                father = input("Enter the name for the new father in this pairing: ")
                register[son.title()]["father"] = father.title()
                grandfather = input("Enter the name for the new grandfather in this pairing: ")
                register[son.title()]["grandfather"] = grandfather.title()
                print("The father and grandfather for", son.title(),\
                      "has been updated.\n")
            else:
                print("That was not a valid choice!\n")
        else:
            print("That name does not exist in the register. Try adding it.\n")
            
    elif menu_choice == "5":
        son = input("\nEnter the name of the son for the listing to be deleted: ")
        if son.title() in register:
            print("This will delete the listing of", \
                  son.title(), "being the son of", \
                  register[son.title()]["father"], "and grandson of", \
                  register[son.title()]["grandfather"])
            confirm = input("Press Y to confirm or any other key to cancel")
            if confirm.upper() == "Y":
                del register[son.title()]
                print("That son-father-grandfather listing has been deleted from the register.\n")
        else:
            print("That name does not exist in the register, it may have already been deleted.\n")

input("\n\nPress the enter key to exit the program.")

'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: whos_your_grandaddy_v1.py
created: 15 May, 2017
@author: user

Chapter 5, Challenge 4
Improve the Who's Your Daddy? program by adding a choice that lets the user
enter a name and get back a grandfather.  Your program should still only use 
one dictionary of son-father pairs.  Make sure to include several generations
in your dictionary so that a match can be found.
NOTE: First attempt at this using an extended dictionary where son-father are
treated as a pair as before, but the father then becomes the son in a new 
entry for a father-grandfather pairing (as they are also son-father to each 
other).
'''

# NOTE: This doesn't allow you to enter a grandfather directly for a son
# If don't enter it at the time,  have to enter it as a separate father-son
# relationship.  Same for deleting - can only delete father-son pairings so 
# can delete a father-son and leave the father-grandfather

# Create dictionary of father/son pairs in format {son: father}
# Treats father/grandfather as a separate father/son relationship
# Think you can do nested dictionary lists but didn't discover then until afterwards
name_register ={"John Smith" : "Bob Smith"
    ,"Bob Smith": "Grandfather Smith"
    ,"David Kilroy" : "Samuel Kilroy"
    , "SAmuel Kilroy": "Grandfather Kilroy"
    ,"Michael Douglas": "Kirk Douglas"
    ,"Kirk Douglas": "Grandfather Douglas"
    ,"Kiefer Sutherland": "Donald Sutherland"
    ,"Donald Sutherland": "Grandfather Sutherland"
    ,"Charlie Sheen": "Martin Sheen"
    ,"Jaden Smith": "Will Smith"
    ,"David Carradine": "John Carradine"
    ,"Scott Caan": "James Caan"
    ,"James Caan": "Grandfather Caan"
    
    }

# Introduction text for program
print("""Who's Your Daddy Lookup Register
--------------------------------
This register records father/son pairing that can be queried
by entering the name of the 'son' to identify the 'father'.""")


menu_choice = None
while menu_choice != "0":
    print("""
    Menu
    ----
    1 - Display all father/son pairings
    2 - Look up a father/son pairing
    3 - Add a new father/son pairing
    4 - Edit a father/son pairing
    5 - Delete a father/son pairing
    
    0 - Quit
    """)
        # get term to look up from user
    menu_choice = input("Please select a menu option: ")

    # 0 exit the program
    if menu_choice == "0":
        print("Thank you for using this program.  Good Bye.")


    elif menu_choice == "1":
        print("\nThe father and son pairings currently recorded in the register are:")
        # print every entry in the name_register dictionary
        for son in name_register.keys():
            print("  ", son, "is the son of", name_register[son])


    elif menu_choice == "2":
        # get the name of the son
        son = input("\nEnter the son's name: ")
        # Use title capitalisation as that's how the dictionary is setup
        if son.title() in name_register:
            generation_choice = input("Do you want to see the father (enter 'F')"\
                                      " or the grandfather (enter 'G')?")
            if generation_choice.upper() == "F":
                # Note still have to do the title conversion when looking up in the dictionary via dictionary[key]
                print("\nThe father of", son.title(), "is", name_register[son.title()])
            elif generation_choice.upper() == "G":
                father = name_register[son.title()]
                if father.title() in name_register:
                    print("\nThe grandfather of", son.title(), "is", name_register[father.title()])
                else:
                    print("There is no grandfather currently recorded for", son.title())                       
            else:
                print("\nThat was not a valid entry!")
        else:
            print("\nThat name does not exist in the register, you may want to add it.")
           
            
    elif menu_choice == "3":
        son = input("\nEnter the name of the son to be added: ")
        if son.title() not in name_register:
            father = input("Enter the name of the father to be added for that son: ")
            name_register[son.title()] = father.title()
            add_choice = input("Do you also want to add a grandfather for that son?"\
                               " ('Y' to add or any other key to return to the main menu).")
            if add_choice.upper() == "Y":
                grandfather = input("Enter the name for the grandfather in this pairing: ")
                name_register[father.title()] = grandfather.title()
                print(son.title(), "the son of", father.title(),"and grandson of",\
                      grandfather.title(), "has been added.")
            else:
                print(son.title(), "the son of", father.title(), "has been added.")
        else:
            print("\nThat name is is already recorded in the register.")
        

    elif menu_choice == "4":
        son = input("\nEnter the name of the son who's father you want to edit: ")
        if son.title() in name_register:
            generation_choice = input("Do you want to edit the father (enter 'F')"\
                                      " or the grandfather (enter 'G')?")
            if generation_choice.upper() == "F":
                # Note still have to do the title conversion when looking up in the dictionary via dictionary[key]
                father = input("Enter the name for the new father in this pairing: ")
                name_register[son.title()] = father.title()
                print("\nThe father for", son.title(), "has been updated.")
            elif generation_choice.upper() == "G":
                father = name_register[son.title()]
                if father.title() in name_register:
                    grandfather = input("Enter the name for the new grandfather in this pairing: ")
                    name_register[father.title()] = grandfather.title()
                    print("\nThe grandfather for", son.title(), "has been updated.")
                else:
                    print("That person does not have a grandfather currently recorded."\
                          " Try adding them to the register.")
        else:
            print("\nThat name does not exist in the register. Try adding it.")


    elif menu_choice == "5":
        son = input("\nEnter the name of the son for the pairing to be deleted: ")
        if son.title() in name_register:
            print("This will delete the pairing of", son.title(), "being the son of",\
                  name_register[son.title()])
            confirm = input("Press Y to confirm or any other key to cancel")
            if confirm.upper() == "Y":
                del name_register[son.title()]
                print("\nThat father/son pairing has been deleted from the register.")
        else:
            print("\nThat name does not exist in the register, it may have already been deleted.")
            
   
input("\n\nPress the enter key to exit the program.")

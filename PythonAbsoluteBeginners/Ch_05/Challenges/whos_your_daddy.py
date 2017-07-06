'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: whos_your_daddy.py
created: 15 May, 2017
@author: Neil_Crerar

Chapter 5, Challenge 3
Write a Who's Your Daddy? program that lets the user enter the name of a male
and produces the name of his father.  You can use celebrities, fictional 
characters , or even historical figures for fun.  Allow the user to add, 
replace, and delete son-father pairs.
'''

# Program pseudocode.....
# Create a pre-populated dictionary of father-son pairs
# Display a menu of action to select from
# 0 - Exit program
# 1 - Display all pairings
#     For all entries in list, display entry on-screen
# 2 - Look up a pair
#     Request 'son' name from user
#     Look up 'son' entry in list and select the 'father' element
#     Display father-son pairing on screen
# 3 - Add a new pairing
#     Request 'son' name from user
#     Request 'father' name from user
#     Append new pairing to the list
# 4 - Replace a pairing
#     Ask user if replacing father or son?
#     Get name they want to keep
#     Get the replacement name for the other half of the pair
#     Look up entry and replace part of pair as needed
#     - elif for the two options then else for invalid entry handling
# 5 - Un-relate a pair? Should this be the same as delete? or create two entries

#create dictionary of father/son pairs in format {son: father}
name_register ={"John Smith" : "Bob Smith"
    ,"David Kilroy" : "Samuel Kilroy"
    ,"Michael Douglas": "Kirk Douglas"
    ,"Kiefer Sutherland": "Donald Sutherland"
    ,"Charlie Sheen": "Martin Sheen"
    ,"Jaden Smith": "Will Smith"
    ,"David Carradine": "John Carradine"
    ,"Scott Caan": "James Caan"
    }

# Introduction text for program
print("""Who's Your Daddy Lookup Register
--------------------------------
This register records father/son pairing that can be queried
by entering the name of the 'son' to identify the 'father'.""")


choice = None
while choice.upper() != "X":
    print("""
    Menu
    ----
    1 - Display all father/son pairings
    2 - Look up a father/son pairing
    3 - Add a new father/son pairing
    4 - Edit a father/son pairing
    5 - Delete a father/son pairing
    
    X - Quit
    """)
        # get term to look up from user
    choice = input("Please select a menu option: ")

    # 0 exit the program
    if choice.upper() == "X":
        print("Thank you for using this program.  Good Bye.")


    elif choice == "1":
        print("\nThe father and son pairings currently recorded in the register are:")
        # print every entry in the name_register dictionary
        for son in name_register.keys():
            print("  ", son, "is the son of", name_register[son])


    elif choice == "2":
        # get the name of the son
        son = input("\nEnter the son's name: ")
        # Use title capitalisation as that's how the dictionary is setup
        if son.title() in name_register:
            # Still have to do the title conversion when looking up in the
            # dictionary via dictionary[key]
            print("\nThe father of ", son.title(), "is", name_register[son.title()])
        else:
            print("\nThat son's name does not exist in the register,"\
                  " you may want to add it.")
           
            
    elif choice == "3":
        son = input("\nEnter the name of the son to be added: ")
        if son.title() not in name_register:
            father = input("Enter the name of the father to be added for that son: ")
            name_register[son.title()] = father.title()
            print("\nThat pairing has been added to the register.")
        else:
            print("\nThat son's name is is already recorded in the register.")
        

    elif choice == "4":
        son = input("\nEnter the name of the son who's father you want to edit: ")
        if son.title() in name_register:
            father = input("Enter the name for the new father in this pairing: ")
            name_register[son.title()] = father.title()
            print("\nThe father-son pairing for", son.title(), "has been updated.")
        else:
            print("\nThat father-son pairing does not exist in the register."\
                  " Try adding it.")


    elif choice == "5":
        son = input("\nEnter the name of the son for the pairing to be deleted: ")
        if son.title() in name_register:
            print("This will delete the pairing of", son.title(), \
                  "being the son of", name_register[son.title()])
            confirm = input("Press Y to confirm or any other key to cancel")
            if confirm.upper() == "Y":
                del name_register[son.title()]
                print("\nThat father/son pairing has been deleted from the register.")
        else:
            print("\nThat son's name does not exist in the register,"\
                  "it may have already been deleted.")

input("\n\nPress the enter key to exit the program.")
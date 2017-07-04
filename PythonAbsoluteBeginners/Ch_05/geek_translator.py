'''
Python Programming For the Absolute Beginner, 3rd Edition
Filename: geek_translator.py
created: 12 May, 2017
@author: user

Demonstrates using dictionaries
'''

# define dictionary contents
geek = {"404": "Clueless. From the web error message 404, meaning not found."
        ,"Googling": "Searching the Internet for background information on a topic."
        ,"Keyboard Plaque": "The collection of debris found in computer keyboards."
        ,"Link Rot": "The process by which web page links become obsolete."
        ,"Percussive Maintenance": "The act of striking an electronic device to make it work."
        ,"Uninstalled": "Being fired, especially popular during the dot-bomb era."
        ,"Dancing Baloney": "Animated graphics or other visual effects that serve \
        no purpose or have no substantive value.  Often used by web designers to impress clients."
        }

choice = None
while choice != "0":
    print("""
    Geek Dictionary
    ---------------
    
    0 - Quit
    1 - Look up a geek term
    2 - Add a geek term
    3 - Redefine a geek term
    4 - Delete a geek term
    5 - Show all terms in the dictionary
    """)
    
    # get term to look up from user
    choice = input("Please select a menu option: ")

    # 0 exit the program
    if choice == "0":
        print("Thank you for using this program.  Good Bye.")
    
    # 1 look up term in dictionary and display 
    elif choice == "1":
        term = input("What term do you want to look up? ")
        if term in geek:
            print(term, " refers to:\n", geek[term])
        else:
            print("The term,", term, "is not listed in the Geek Dictionary")

        # or can use 'get' method instead and define the 'not found' message
        #print(geek.get(term, "That term is not listed in the dictionary"))
    
    # 2 add a new term and definition
    elif choice == "2":
        term = input("What term do you want to add? ")
        if term not in geek:
            definition = input("What is the definition for that term? ")
            geek[term] = definition
            print("\n", term, "has been added to the Geek Dictionary.")
        else:
            print("\nThat term is already listed in the Geek Dictionary. Try re-defining it.")

    # redefine an existing term
    elif choice == "3":
        term = input("What term do you want to redefine? ")
        if term in geek:
            definition = input("What's the new definition? ")
            geek[term] = definition
            print("\n", term, "has been redefined.")
        else:
            print("\nThat term does not exist in the Geek Dictionary. Try adding it.")
    
    # delete a term-definition pair
    elif choice == "4":
        term = input("What term do you want to delete? ")
        if term in geek:
            del geek[term]
            print("\n", term, "has been deleted from the dictionary.")
        else:
            print("That term does not exist in the Geek Dictionary.")
    
    # show all keys in the dictionary
    elif choice == "5":
        print("The terms defined in the dictionary are:")
        for term in geek.keys():
            print("  ", term)
    
    # handle invalid choices
    else:
        print("\nThat option has not been recognised.  Please try again.")
    
input("\n\nPress the enter key to exit the program.")

        
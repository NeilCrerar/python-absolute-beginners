"""
Python Programming For the Absolute Beginner, 3rd Edition
filename: receive_and_return.py
created: 19 May, 2017
@author: Neil_Crerar

Demonstrates parameters and return values
"""

def display(message):
    print(message)


def give_me_five():
    five = 5
    return five


def ask_yes_no(question):
    """Ask a yes or no question"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


# Main
display("Here's a message for you.\n")

number = give_me_five()
print("Here's what I got from give me five:", number)

answer = ask_yes_no("\nPlease enter 'y' or 'n': ")
print("Thanks for entering:", answer)

input("\n\nPress the enter key to exit")

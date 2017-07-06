'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: handle_it.py
created on: 19 Jun, 2017
@author: Neil_Crerar

Demonstrates exception handling
'''

# Basic try/except
try:
    num = float(input("Enter a number: "))
except:
    print("Something went wrong!")

# Specifying exception type
try:
    num = float(input("\nEnter another number: "))
except ValueError:
    print("That was not a number!")

# Handle multiple exception types
print()
for value in (None, "Hi!"):
    try:
        print("Attempting to convert", value, "-->", end=" ")
        print(float(value))
    except (TypeError, ValueError):
        print("Something went wrong!")
    
# More handling of multiple exception types
print()
for value in (None, "Hi!"):
    try:
        print("Attempting to convert", value, "-->", end=" ")
        print(float(value))
    except TypeError:
        print("I can only convert a string or a number!")
    except ValueError:
        print("I can only convert a string of digits!")

# Get an exceptions argument
try:
    num = float(input("\nEnter a number: "))
except ValueError as e:
    print("That was not a number! Or as python would say...")
    print(e)
    
# Try/except/else
try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")
else:
    print("You entered the number", num)

# Default program exit control code
input("\n\nPress the enter key to exit.")

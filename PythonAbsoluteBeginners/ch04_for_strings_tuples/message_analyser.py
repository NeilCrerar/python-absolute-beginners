"""
Python Programming For the Absolute Beginner, 3rd Edition
filename: message_analyser.py
created on: May, 2017
@author: Neil_Crerar

Demonstrates the len() function in an operation
"""

message = input("Enter a message: ")

print("\nThe length of your message is:", len(message))

print("\nThe most common letter in the English language, 'e',")
if 'e' in message:
    print("is in your message.")
else:
    print("is not in your message.")

input("\n\nPress the enter key to exit.")
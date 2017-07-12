"""
Python Programming For the Absolute Beginner, 3rd Edition
filename: granted_or_denied.py
created on: May, 2017
@author: Neil_Crerar

Demonstrates the else clause
"""

print("Welcome to System Security Inc.")
print("-- where security is our middle name\n")

password = input("Enter your password: ")

if password == "secret":
    print("Access Granted")
else:
    print("Access Denied")

input("\n\nPress the enter key to exit")

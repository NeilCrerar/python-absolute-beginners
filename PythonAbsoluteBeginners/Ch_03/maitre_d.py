'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: maitre_d.py
created on: May, 2017
@author: Neil_Crerar

Demonstrates treating a value as a condition
'''

print("Welcome to Chateau D'Food")
print("It seems  we are quite full this evening.\n")

money = int(input("How many dollars do you slip the Maitre'D? "))

if money:
    print("Ah, I am reminded of a table, right this way sir.")
else:
    print("Please, sit, it may be a while.")

input("\n\nPress the enter key to continue")

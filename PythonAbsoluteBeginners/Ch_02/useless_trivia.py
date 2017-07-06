'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: useless_trivia.py
created on: May, 2017
@author: Neil_Crerar

Gets personal information from the user and then prints true but useless 
information about them
'''

name = input("Hi. What is your name? ")

age = input("How old are you? ")
age = int(age)

weight = int(input("Okay, last question.  How many pounds do you weigh? "))

print("\nIf poet E.E.Cummings were to email you, he'd address you as", name.lower())
print("But if he were mad, he'd call you", name.upper())

called = name * 5
print("\nIf a small child were trying to get your attention",)
print("Your name would become:")
print(called)

seconds = age *365 * 24 * 60 * 60
print("\nYou'reover", seconds, "seconds old.")

moon_weight = weight / 6
print("\nDid you know that on the moon you would weigh only", moon_weight, "pounds!")

input("\n\nPress the enter key to exit")
"""
Python Programming For the Absolute Beginner, 3rd Edition
filename: favourite_food.py
created on: 22 May, 2017
@author: Neil_Crerar

Chapter 2, Challenge 2
Write a program that allows a user to enter his or her two favourite foods.
The program should then print out the name of a new food by joining the 
original food names together.  NOTE: created several outputs with the two foods
in different combinations.
"""

firstFood = input("What is your favourite food? ")
secondFood = input("What is your second favourite food? ")

print("\nWouldn't it be weird to have food of......", firstFood, secondFood)
print("or...", firstFood + secondFood)
print("or...", secondFood + firstFood)

input("\n\nPress the enter key to exit")
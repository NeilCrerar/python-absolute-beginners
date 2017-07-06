'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: tipper.py
created on: May, 2017
@author: Neil_Crerar

Chapter 2, Challenge 3
Write a tipper program where the user enters a restaurant bill total.  The 
program should then display two amounts: a 15 percent tip and a 20 percent tip.
'''

from decimal import Decimal

meal_amount = Decimal(input("How much was your meal? $"))
tip15 = meal_amount * Decimal(1.15)
print("\nA 15 percent tip for that meal would be $", round(tip15, 2))
tip20 = meal_amount * Decimal(1.20)
print("\nA 20 percent tip for that meal would be $", round(tip20, 2))
input("\n\nPress the enter key to exit")

"""
Python Programming For the Absolute Beginner, 3rd Edition
filename: trust_fund_buddy_broken.py
created on: May, 2017
@author: Neil_Crerar

Demonstrates a logical error
"""

print("""
        Trust Fund Buddy

    Totals your monthly spending so that your trust fund doesn't run out
    (and you are forced to get a real job)

    Please enter the the requested monthly costs.
    Since you're rich ignore the pennies and use only dollar amounts.
    """)

car = input("lamborghini Tune Ups: $")
rent = input("Manhattan Apartment: $")
jet = input("Private Jet Rental: $")
gifts = input("Gifts: $")
food = input("Dining Out: $")
staff = input("Staff (butlers, chef, driver, assistant): $")
guru = input("Personal Guru and Coach: $")
games = input("Computer Games: $")

total = car + rent + jet + gifts + food + staff + guru + games

print("\nGrand Total: ", total)

input("\n\nPress the enter key to exit")

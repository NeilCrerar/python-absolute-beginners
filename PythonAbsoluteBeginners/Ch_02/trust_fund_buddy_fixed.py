'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: trust_fund_buddy_fixed.py
created on: May, 2017
@author: user

Demonstrates a logical error after it's resolved
'''

print("""
        Trust Fund Buddy

    Totals your monthly spending so that your trust fund doesn't run out
    (and you are forced to get a real job)

    Please enter the the requested monthly costs.
    Since you're rich ignore the pennies and use only dollar amounts.
    """)

car = input("lamborghini Tune Ups: $")
car = int(car)

rent = int(input("Manhattan Apartment: $"))
jet = int(input("Private Jet Rental: $"))
gifts = int(input("Gifts: $"))
food = int(input("Dining Out: $"))
staff = int(input("Staff (butlers, chef, driver, assistant): $"))
guru = int(input("Personal Guru and Coach: $"))
games = int(input("Computer Games: $"))

total = car + rent + jet + gifts + food + staff + guru + games

print("\nGrand Total: ", total)

input("\n\nPress the enter key to exit")
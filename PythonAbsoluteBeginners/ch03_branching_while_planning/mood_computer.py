"""
Python Programming For the Absolute Beginner, 3rd Edition
filename: mood_computer.py
created on: May, 2017
@author: Neil_Crerar

Demonstrates the 'elif' clause
"""

import random

print("I sense your energy.  Your true emotions are coming across my screen.")
print("You are...")

mood = random.randint(1,3)

if mood == 1:
    # Happy
    print("""
             __________
            |          |
            |  O    O  |
            |    <     |
            |          |
            | \      / |
            |  \____/  |
            |__________|

            """)
elif mood == 2:
    # Neutral
    print("""
             __________
            |          |
            |  O    O  |
            |    <     |
            |          |
            | ________ |
            |          |
            |__________|

            """)
elif mood == 3:
    # Sad
    print("""
             __________
            |          |
            |  O    O  |
            |    <     |
            |          |
            |  ______  |
            | /      \ |
            |__________|

            """)
else:
    print("Illegal mood value! (you must be in a really bad mood)")

print("...today.")

input("\n\nPress the enter key to exit")

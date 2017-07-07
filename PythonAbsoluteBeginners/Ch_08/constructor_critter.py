"""
Python Programming For the Absolute Beginner, 3rd Edition
filename: constructor_critter.py
created on: 30 Jun, 2017
@author: Neil_Crerar

Demonstrates constructors
"""

class Critter(object):
    """A virtual pet"""

    
    def __init__(self):
        print("A new critter has been born.")

    
    def talk(self):
        print("Hi.  I'm an instance of class Critter.")


# Main
crit1 = Critter()
crit2 = Critter()

crit1.talk()
crit2.talk()

input("\n\nPress the enter key to exit.")

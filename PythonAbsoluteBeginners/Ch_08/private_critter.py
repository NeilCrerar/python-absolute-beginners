'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: private_critter.py
created on: 30 Jun, 2017
@author: Neil_Crerar

Demonstrates private variables and methods
'''

class Critter(object):
    """A virtual pet"""

        
    def __init__(self, name, mood):
        print("A new critter has been born.")
        self.name = name    # Public attribute
        self.__mood = mood  # Private attribute
    
    
    def talk(self):
        print("\nI'm", self.name)
        print("Right now I feel", self.__mood, "\n")
    
    
    def __private_method(self):
        print("This is a private method.")

        
    def public_method(self):
        print("This is a public method.")
        self.__private_method()


# Main
crit = Critter(name="Poochie", mood="happy")
crit.talk()
crit.public_method()


# Default program exit control code
input("\n\nPress the enter key to exit.")

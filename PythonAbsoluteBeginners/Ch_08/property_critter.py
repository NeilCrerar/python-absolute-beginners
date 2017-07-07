"""
Python Programming For the Absolute Beginner, 3rd Edition
filename: property_critter.py
created on: 30 Jun, 2017
@author: Neil_Crerar

Demonstrates properties
"""

class Critter(object):
    """A virtual pet"""

    
    def __init__(self, name):
        print("A new critter has been born.")
        self.__name = name

        
    @property
    def name(self):
        return self.__name

    
    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("A critter's name can't be an empty string.")
        else:
            self.__name = new_name
            print("Name change successful.")

    
    def talk(self):
        print("Hi, I'm", self.name)


# Main
crit = Critter("Poochie")
crit.talk()

print("\nMy critters name is:", end=" ")
print(crit.name)

print("\nAttempting to change my critters name to Randolph...")
crit.name = "Randolph"

print("My critters name is:", end=" ")
print(crit.name)

print("\nAttempting to change my critters name to an empty string...")
crit.name = ""

print("My critters name is:", end=" ")
print(crit.name)

input("\n\nPress the enter key to exit.")

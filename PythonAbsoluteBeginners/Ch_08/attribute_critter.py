'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: attribute_critter.py
created on: 30 Jun, 2017
@author: Neil_Crerar

Demonstrates creating and accessing object attributes
'''

class Critter(object):
    """A virtual pet"""

    
    def __init__(self, name):
        print("A new critter has been born.")
        self.name = name
    
    
    def __str__(self, ):
        rep = "Critter object\n"
        rep += "Name: " + self.name + "\n"
        return rep
    
    
    def talk(self):
        print("Hi.  I'm", self.name, "\n")

        
# Main
crit1 = Critter("Poochie")
crit1.talk()

crit2 = Critter("Randolph")
crit2.talk()

print("Printing crit1:")
print(crit1)

print("Directly accessing crit1.name:")
print(crit1.name)

# Default program exit control code
input("\n\nPress the enter key to exit.")

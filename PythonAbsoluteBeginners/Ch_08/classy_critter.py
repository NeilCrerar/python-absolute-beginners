'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: classy_critter
created on: 30 Jun, 2017
@author: user

Demonstrates class attributes and static methods
'''

class Critter(object):
    """A virtual pet"""
    total = 0

    
    @staticmethod
    def status():
        print("\nThe total number of critters is", Critter.total)

    
    def __init__(self, name):
        print("A new critter has been born.")
        self.name = name
        Critter.total +=1


# Main
# Book text state there was this command at the start of the program but it's
# not in the written code example?
#Critter.status()

print("Accessing the class attribute Critter.total: ", end=" ")
print(Critter.total)

print("\nCreating critters")
crit1 = Critter("critter 1")
crit2 = Critter("critter 2")
crit3 = Critter("critter 3")

Critter.status()

print("\nAccessing the class attribute through an object: ", end=" ")
print(crit1.total)

# Default program exit control code
input("\n\nPress the enter key to exit.")

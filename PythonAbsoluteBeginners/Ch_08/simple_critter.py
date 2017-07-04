'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: simple_critter.py
created on: 30 Jun, 2017
@author: user

Demonstrates a basic class and object
'''

class Critter(object):
    """A virtual pet"""
    
    def talk(self):
        print("Hi.  I'm an instance of the Critter class.")
        
        
# Main
crit = Critter()
crit.talk()


# Default program exit control code
input("\n\nPress the enter key to exit.")

"""
Python Programming For the Absolute Beginner, 3rd Edition
filename: loosing_battle_fixed.py
created on: May, 2017
@author: Neil_Crerar

Demonstrate the dreaded infinite loop - fixed
"""

print("Your lone hero is surrounded by a massive army of trolls.")
print("Their decaying green bodies stretch out, melting into the horizon.")
print("Your hero unsheathes his sword for the last fight of his life.\n")

health = 10
trolls = 0
damage = 3

while health > 0:
    trolls += 1
    health -= damage

    print("Your hero swings and defeats an evil troll, " \
          "but takes", damage, "damage points.\n")

print("Your hero fought valiantly and defeated", trolls, "trolls.")
print("But alas, your hero is no more.")

input("\n\nPress the enter key to exit.")

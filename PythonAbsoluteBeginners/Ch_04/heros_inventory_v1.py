'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: heros_inventory_v1.py
created on: May, 2017
@author: Neil_Crerar

Demonstrates tuple creation
'''

# create an empty tuple
inventory = ()

# treat the tuple as a condition
if not inventory:
    print("You are empty handed.")
    
input("\n\nPress the enter key to continue.")

# create a tuple with some items
inventory = ("Sword",
             "Armour",
             "Shield",
             "Healing Potion")

# print the tuple
print("\nThe tuple inventory is:")
print(inventory)

# print each element in the tuple
print("\nYour items are:")
for item in inventory:
    print("\t", item)

input("\n\nPress the enter key to exit.")

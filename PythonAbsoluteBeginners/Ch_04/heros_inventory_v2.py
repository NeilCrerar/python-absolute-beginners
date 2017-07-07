"""
Python Programming For the Absolute Beginner, 3rd Edition
filename: heros_inventory_v2.py
created on: May, 2017
@author: Neil_Crerar

Create a tuple with some items and display with a for loop
"""

inventory = ("Sword", "Armour", "Shield", "Healing Potion")

print("Your items are:")
for item in inventory:
    print("\t", item)

input("\nPress the enter key to continue.")

#get the length of a tuple
print("\nYou have", len(inventory), "items in your possession.")

# test for membership with in
if "Healing Potion" in inventory:
    print("\nYou will live to fight another day.")

# display one item through the index
index = int(input("\nEnter the index number for an item in the inventory: "))
print("At index", index, "is", inventory[index])

# display a slice
start = int(input("\nEnter the index number to begin the slice: "))
finish = int(input("Enter the index number to end the slice: "))
print("Inventory[", start, ":", finish, "] is", end=" ")
print(inventory[start:finish])

input("\nPress the enter key to continue.")

# concatenate two tuples
chest = ("Gold", "Gems")
print("\nYou find a chest.  It contains:")
print(chest)

print("\nYou add the contents of the chest to your inventory.")
inventory += chest
print("You inventory is now:")
print(inventory)

input("\nPress the enter key to exit.")

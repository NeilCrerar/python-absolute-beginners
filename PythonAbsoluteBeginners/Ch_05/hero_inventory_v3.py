'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: hero_inventory_v3.py
created: 11 May, 2017
@author: user

Demonstrates lists
'''

# create a list with some items and display with a for loop
inventory = ["sword", "armour", "shield", "healing potion"]
print("Your Items: ")
for item in inventory:
    print(item)

# get the length of a list
print("\nYou have", len(inventory), "items in your inventory.")

# test for membership with in
if "healing potion" in inventory:
    print("You will live to fight another day.")

input("\nPress the enter key to continue.")

# display one item through an index
index = int(input("Enter the index number for an item in the inventory: "))
print("At index", index, "is", inventory[index])

# display a slice of the list
start = int(input("Enter the index number to begin a slice of the inventory: "))
finish = int(input("Enter the index number to end the slice: "))
print("Inventory[", start, ":", finish, "] is", end=" ")
print(inventory[start:finish])

input("\nPress the enter key to continue.")

# concatenate two lists
chest = ["gold", "gems"]
print("\nYou find a chest that contains:")
print(chest)

print("You add the contents of the chest to your inventory.  It now contains:")
inventory += chest
print(inventory)

input("\nPress the enter key to continue.")

# assign by index
print("\nYou trade your sword for a crossbow.")
inventory[0] = "crossbow"
print("Your inventory is now:")
print(inventory)

input("\nPress the enter key to continue.")


# assign by slice
print("\nYou use your gold and gems to buy an orb of future telling.")
inventory[4:6] = ["orb of future telling"]
print("Your inventory is now:")
print(inventory)

input("\nPress the enter key to continue.")

# delete an element
print("\nIn a great battle your shield is destroyed.")
del inventory[2]
print("Your inventory is now:")
print(inventory)

input("\nPress the enter key to continue.")

#delete a slice
print("\nYour crossbow and armour are stolen by thieves.")
del inventory[:2]
print("Your inventory is now:")
print(inventory)


input("\n\nPress the enter key to exit.")


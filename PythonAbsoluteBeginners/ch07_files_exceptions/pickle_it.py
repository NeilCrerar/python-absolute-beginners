"""
Python Programming For the Absolute Beginner, 3rd Edition
filename: pickle_it
created on: 26 May, 2017
@author: Neil_Crerar

Demonstrates pickling and shelving data
"""

# Define imports
import pickle, shelve

# Define lists content
print("Pickling Lists.")
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz", "Vlassic"]

f = open("pickles.dat", "wb")

# Pickle the lists and dump to file
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

# Un-pickle the file contents and assign back to variables
# NOTE: this is done in the same order they were written so is there 
# some sort of order dependency in this
print("\nUn-pickling lists......")
f  = open("pickles.dat", "rb")
variety2 = pickle.load(f)
shape2 = pickle.load(f)
brand2 = pickle.load(f)
f. close()

# Print out the un-pickled lists
print("\tVariety is", variety2)
print("\tShape is", shape2)
print("\tBrand is", brand2)

# Create a shelf for data going into a file
print("\nShelving lists...")
s = shelve.open("pickles2.dat")

# Add lists to the shelve
s["variety"] = ["sweet", "hot", "dill"]
s["shape"] = ["whole", "spear", "chip"]
s["brand"] = ["Claussen", "Heinz", "Vlassic"]

# Sync the shelve
s.sync()

# Retrieve pickled data via a shelve
print("\nRetrieving lists from a shelved file...")
print("\tBrand - ", s["brand"])
print("\tShape - ", s["shape"])
print("\tVariety - ", s["variety"])
print("\nRetrieving the middle list (shape) only - ", s["shape"])

# Close the shelve file
s.close()

# Default program exit control code
input("\n\nPress the enter key to exit.")

"""
Python Programming For the Absolute Beginner, 3rd Edition
filename: user_counting.py
created on: May, 2017
@author: Neil_Crerar

Chapter 3, Challenge 1
Write a program that counts for the user.  Let the user enter the starting 
number, the ending number , and the amount by which to count.
"""

print("Welcome to the number counting program.")
print("Enter a start, end and increment number...")
print("...and let the program do the hard work for you.")

# Get values from user
start = int(input("\nEnter the number to start counting from: "))
end = int(input("Enter the number to count up to: "))
increment = int(input("Enter the increment to count up by: "))

# Output values to screen
print("\nThe numbers in that range are:")
for i in range(start, end, increment):
    print(i)

input("\n\nPress and key to exit.")

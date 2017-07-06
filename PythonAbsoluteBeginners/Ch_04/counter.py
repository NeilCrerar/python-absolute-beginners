'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: counter.py
created on: May, 2017
@author: Neil_Crerar

Demonstrates the range() function
'''

print("Counting:")
for i in range(10):
    print(i, end=" ")

print("\n\nCounting by fives:")
for i in range(0, 50, 5):
    print(i, end=" ")

print("\n\nCounting backwards:")
for i in range(10,0,-1):
    print(i, end=" ")

input("\n\nPress the neter key to exit.")
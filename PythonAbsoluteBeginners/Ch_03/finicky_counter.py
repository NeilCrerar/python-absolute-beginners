'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: finicky_counter.py
created on: May, 2017
@author: user

Demonstrates the break and continue statements
'''

count = 0
while True:
    count +=1

    # end loop if count greater than 10
    if count > 10:
        break

    # skip 5
    if count == 5:
        continue
    print(count)

input("\n\nPress the enter key to exit.")

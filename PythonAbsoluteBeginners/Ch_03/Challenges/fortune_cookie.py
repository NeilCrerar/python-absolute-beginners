'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: fortune_cookie.py
created on: May, 2017
@author: Neil_Crerar

Chapter 3, Challenge 1
Write  a program that simulates a fortune cookie. The program should display 
one of five unique fortunes, at random, each time it's run.
'''

import random

print("\tWelcome to the Electronic Fortune Cookie")
input("\nPress and key to get your personalised fortune...\n\n")

random_number = random.randint(1,20)

if random_number == 1:
    print("...Life is a sexually transmitted condition.")
elif random_number == 2:
    print("...Person who rests on laurels gets thorn in backside.")
elif random_number == 3:
    print("...You will soon have an out of money experience.")
elif random_number == 4:
    print("...Okay to look at past and future. Just don't stare")
elif random_number == 5:
    print("...You are cleverly disguised as responsible adult.")
elif random_number == 6:
    print("...Two days from now, tomorrow will be yesterday.")
elif random_number == 7:
    print("...Person who argues with idiot is taken for fool.")
elif random_number == 8:
    print("...This fortune no good. Try another.")
elif random_number == 9:
    print("...Wise husband is one who thinks twice before saying nothing.")
elif random_number == 10:
    print("...Marriage lets you annoy one special person for the rest of your life")
elif random_number == 11:
    print("...I cannot help you, for I'm just a cookie")
elif random_number == 12:
    print("...The fortune you seek, is in another cookie")
elif random_number == 13:
    print("...You will be hungry again in one hour")
elif random_number == 14:
    print("...You will die alone and poorly dressed")
elif random_number == 15:
    print("...Warning: do not eat your fortune")
elif random_number == 16:
    print("...If you can read this, you are literate. Congratulations")
elif random_number == 17:
    print("...Ignore all previous fortunes,only this one counts")
elif random_number == 18:
    print("...Hearty laughter is a good way to jog internally without having to go outdoors")
elif random_number == 19:
    print("...Today is probably a huge improvement over yesterday")
else:
    print("...Every exit is an entrance to new experiences")


input("\n\nPress the enter key to exit")
'''
Python Programming For the Absolute Beginner, 3rd Edition
filename: word_jumble_v2.py
created on: May, 2017
@author: user

Chapter 3, Challenge 3
Improve the Word Jumble program so that each word is paired with a hint.  The 
player should be able to see the hint if her or she is stuck.  Add a scoring 
system that rewards players who solve a jumble without asking for the hint.
'''

import random

# create sequence of words to choose from
PUZZLES = (
    ("easy", "It's not difficult"),
    ("answer", "Your looking for the right one"),
    ("xylophone", "Hit it with sticks"),
    ("penguin", "black and white and loves the cold"),
    ("test", "what you should do to any computer program"),
    ("difficult", "It's not easy"),
    ("taxes", "Only guarantee in life other than death"),
    ("death", "Only guarantee in life other than taxes"),
    ("python", "It's a type of snake"),
    ("jumble", "It's what this program does to words"),
    ("white", "Considered the opposite of black"),
    ("night", "The opposite of day"),
    ("moon", "Large celestial orb")
    )

# pick a random position in the puzzles list to use for the word and associated hint
selection = random.choice(range(len(PUZZLES)))
# use the selection to pick out the word and hint and assign to variables
word = PUZZLES[selection][0] # as have two parts to each tuple entry using index 0/1 to distinguish between them
hint = PUZZLES[selection][1]

# create a variable to use later to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble = ""
while word:
    # identify a random letter in the word
    position = random.randrange(len(word))
    # concatentate that letter and the existing jumble string
    jumble += word[position]
    # re-assign word as a  concatenation of the letters up to but not including the letter
    # position identified and the letters after the letter position to the end of the word
    word = word[:position] + word[(position+1):]

# print the game introduction text
print("""
           Welcome to Word Jumble!
     Unscramble the letters to make a word

Start with 10 points and:
  -Lose 1 point for each incorrect answer
  -Lose 5 points if you need to take a hint (type 'H' at the prompt)
  -Press ENTER at the prompt to exit the game
""")

# print the word the user has to guess
print("\nThe jumbled word is:", jumble)

# create variable to hold user score
user_score = 10

# get the users guess and evaluate it
guess = input("\nWhat is your first guess? ")
while guess != correct and guess != "":
    print("--debug: guess is", guess)

    #check if the user has asked for a hint, print it if they have
    if guess.upper() == 'H':
        print("Your hint is...", hint)
        user_score -= 5
    # if not tell them their answer was incorrect
    else:
        print("Sorry, that's not it and you lose a point, please try again.")
        user_score -= 1
    guess = input("\nWhat is your next guess? ")

# congratulate the user when the guess is correct
if guess == correct:
    print("\nThats it! You guessed the word correctly!")
    print("Your score was", user_score, "out of 10.")

print("\nThanks for playing")
input("\n\nPress the enter key to exit.")



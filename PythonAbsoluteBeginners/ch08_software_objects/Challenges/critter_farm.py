"""
Python Programming For the Absolute Beginner, 3rd Edition
filename: critter_farm.py
created on: 03 Jul, 2017
@author: Neil_Crerar

Chapter 8, Challenge 4
Create a critter farm program by instantiating several critter objects and 
keeping track of them through a list.  Mimic the Critter Caretaker program , 
but instead of requiring the user to care for a single critter, require them 
to care for an entire farm.  EAch menu choice should allow the user to perform 
some action for all of the critters, or listen to all of the critters (feed 
all of the critters, play with all of the critters, or listen to all of the 
critters).  To make the program interesting, give each critter random starting 
hunger or boredom levels.

Not too happy with this solution as want all the looping through list of 
critters within the talk, eat, play, etc. methods themselves so menu and 
actions are truly separate. Would need a fairly substantial re-write though. 
"""

# Define imports
from random import randint
from random import randrange
    
    
class Critter(object):
    """
    Create a set of virtual pets you can feed and play with, but watch out, if 
    they get too bored or hungry, they'll get mad!
    """    
    
    def __init__(self):
        """
        Set initial values for critter object
        """
        # Get random name from list
        with open("first_names.txt") as f:
            name_list = [line.rstrip() for line in f]
        position = randrange(len(name_list))
        self.name = name_list[position] 
        # Get random initial values for hunger and boredom levels
        self.hunger = randint(1,5)
        self.boredom = randint(1,5)


    def __str__(self):
        """
        :returns: current details for a critter object
        """
        unhappiness = self.hunger + self.boredom
        crit_details = "Critter Details\n"
        crit_details += "Name: " + self.name + "\n"
        crit_details += "Hunger: " + str(self.hunger) + "\n"
        crit_details += "Boredom: " + str(self.boredom) + "\n"
        crit_details += "Unhappiness: " + str(unhappiness) + "\n"
        return crit_details
    
            
    def __pass_time(self):
        """
        Imitate passing of time and increase hunger and boredom levels.
        """
        self.hunger += 1
        self.boredom += 1
        
    
    @property
    def mood(self):
        """
        Calculates critter mood by sum of hunger and boredom levels.
        :returns: the mood calculated for the critter object
        """
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5<= unhappiness <= 10:
            m = "okay"
        elif 11<= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m
    
    
    def talk(self):
        """
        Prints name and current mood for critter object.
        """   
        print("I'm", self.name, "and I feel", self.mood, "now.")
        self.__pass_time()
    
    
    def eat(self, food):
        """
        Takes value for feeding a critter and subtracts from hunger level.
        :param food: value to reduce hunger level by
        """       
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

            
    def play(self, playtime):
        """
        Takes value for playing with a critter and subtracts from boredom level.
        :param playtime: value to reduce boredom level by
        """  
        self.boredom -= playtime
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    """
    Main program menu and control.
    """
    print("Welcome to the Critter Farm!\n")
    # create list of critters on farm
    number_of_critters = int(input("How many critters do you want on your farm?: "))
    critter_list = []
    for i in range(number_of_critters):        
        critter_list.append(Critter())
        
    # Game menu an player selection
    choice = None
    while choice != "0":
        print \
        ("""
        
        Critter Options
        ---------------        
        
        0 - Quit
        1 - Listen to your critters
        2 - Feed your critters
        3 - Play with your critters
        4 - See the details for each critter
        """)
        choice = input("Choice: ")
        print()
        
        # Exit program
        if choice == "0":
            print("Good-bye.")
            
        # Listen to your critter
        elif choice == "1":
            for critter in critter_list:
                critter.talk()

        # Feed your critter
        elif choice == "2":          
            # Try/except for invalid entries
            try:
                food = int(input(
                    "How much food do you want to give your critters? (1-3): "))
                if food < 1 or food > 3:
                    print("\nThat was not a valid amount to feed your critters!")
                else:
                    for critter in critter_list:                                
                        critter.eat(food)
                    print("\nMunch, munch, munch, bbbbbbuuuuurrrrrppppp!")
                    print("Your critters seem to like eating a lot!")    
            except ValueError:
                print("Sorry, but that was not a valid entry!")
        
        # Play with your critter
        elif choice == "3":
            # Try/except for invalid entries
            try:
                playtime = int(input(
                    "How much time do you want to play with your critters? (1-5): "))
                if playtime < 1 or playtime > 5:
                    print("\nThat was not a valid amount to play with your critters!")
                else:
                    for critter in critter_list:                                
                        critter.play(playtime)
                    print("\nWheeeee!  Your critters seem much happier now!")    
            except ValueError:
                print("\nSorry, but that was not a valid entry!")

        # Get details for each critter on the farm
        elif choice == "4":
            for critter in critter_list:
                print(critter.__str__())    
        # Any other entry
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

                
main()
input("\n\nPress the enter key to exit.")

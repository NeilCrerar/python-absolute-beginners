"""
Python Programming For the Absolute Beginner, 3rd Edition
filename: television.py
created on: 03 Jul, 2017
@author: Neil_Crerar

Chapter 8, Challenge 2
Write a program that simulates a television by creating it as an object.  The
user should be able to enter a channel number and raise or lower the volume.
Make sure that the channel number and volume stay within valid ranges.
"""

class Television(object):
    """
    Create a virtual television
    """    
    
    def __init__(self, channel=1, volume=10):
        """
        :param name: name assigned to the new critter object
        :param channel: initial channel value assigned to television
        :param volume: initial volume value assigned to television
        """ 
        self.channel = channel
        self.volume = volume

    
    def __str__(self):
        """
        :returns: current details for the television object
        """
        tv_details = "Television Details\n"
        tv_details += "Channel: " + str(self.channel) + "\n"
        tv_details += "Volume: " + str(self.volume) + "\n"
        return tv_details    


    def get_listings(self):
        """
        :returns: a list of tv channel names from a file
        """
        f = open("tv_channel_list.txt", "r")
        channel_list = f.readlines()
        f.close()
        return channel_list
       
    
    def change_channel(self):
        """
        User specified value for the tv channel to change to.
        """
        listings = self.get_listings()
        print("You are currently watching", listings[self.channel-1], end="")
        # Try/except for invalid entries
        try:
            entry = int(input(
                "What channel number (1-30) do you want to change to?: "))
            if entry < 1 or entry > 30:
                print("That's not a valid channel choice!")
            else:   
                self.channel = entry
                print("\nThe television has been changed to Channel",
                      self.channel,
                      ":",
                      listings[self.channel-1],
                      "\n")
        except ValueError:
            print("That was not a valid entry!")


    def change_volume(self):
        """
        User specified value for the tv volume to change to.
        """
        print("The television's current volume is:", self.volume)
        # Try/except for invalid entries
        try:
            entry = int(input(
                "What volume do you want to change the tv to?: "))
            if entry < 1 or entry > 20:
                print("That's not a valid channel choice!")
            else:
                self.volume = entry
                print("\nThe television volume has been changed to:", self.volume)
                if self.volume < 7:
                    print("This may be a bit quiet, you might want to turn it up.\n")
                elif self.volume > 15:
                    print("This may be a bit loud,you might want to turn it down.\n")
        except ValueError:
            print("That was not a valid entry!")

   
def main():
    """
    Main program menu and control
    """
    tv_instance = Television()
    # Menu an player selection
    choice = None
    while choice != "0":
        print \
        ("""
        TV Control
        
        0 - Quit
        1 - Change the channel
        2 - Change the volume
        """)
        choice = input("Choice: ")
        print()
        # Exit program
        if choice == "0":
            print("Good-bye.")
        # Change the channel on the tv
        elif choice == "1":
            tv_instance.change_channel()
        # Change the volume on the tv
        elif choice == "2":
            tv_instance.change_volume()
        # Change the volume on the tv
        elif choice == "9":
            print(tv_instance.__str__())        
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

                
main()
input("\n\nPress the enter key to exit.")

'''
filename: write_it
created on: 26 May, 2017
@author: user

Python Programming For the Absolute Beginner, 3rd Edition
Chapter 7, Exercise 2

Demonstrates writing to a file
'''

print("Creating a text file with the write() method.")

# create a new text file to write some content to it
text_file = open("write_it.txt", "w")

text_file.write("Line 1\n")
text_file.write("This is Line 2\n")
text_file.write("..and that makes this Line 3\n")
text_file.close()

print("\nReading the newly created file.")
text_file = open("write_it.txt", "r")
print(text_file.read())
text_file.close()

# re-create the text file, wiping out the one created above
print("More write() methods ....")
text_file = open("write_it.txt", "w")
# create a list with the new content
lines = ["This is Line 1\n",
         "This is Line 2\n",
         "This is Line 3\n"]
# write the new content to the file
text_file.writelines(lines)
text_file.close()

print("\nReading the newly created file.")
text_file = open("write_it.txt", "r")
print(text_file.read())
text_file.close()
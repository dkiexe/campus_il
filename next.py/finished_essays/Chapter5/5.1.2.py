# We mentioned in the unit the well-known children's song "Little Jonathan" and now it's time to write code that plays it!

# How do you do that?

# In order to play a note, we need to know its frequency and how long it should be played. For this purpose, use the following two variables:

# A dictionary called freqs where the keys are strings representing the name of a character and the values ​​are numbers representing frequencies.

# freqs = {"la": 220,
#          "si": 247,
#          "do": 261,
#          "re": 293,
#          "mi": 329,
#          "fa": 349,
#          "sol": 392,
#          }
# Strings that include the notes of the song:

# notes =
# "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol 500"
# The strings are constructed as follows:

# Each note is followed by a comma followed by a number representing how long the note should be played. Each character is separated from the other by a dash.

# Do the following tasks:

# Use the split method to split the character strings by the hyphen character. Is the resulting object an iterable? Verify this by using the dir and type functions.

# To play a note, use the following code:

# import winsound
# ...
# winsound.Beep(frequency, duration)
# The Beep function accepts two parameters: the frequency of a note and the length of time it should be played.

# Write a program that plays the song Little Jonathan. For this purpose, create an iterable from the character strings and run a for loop on it, or alternatively use the next function.

# My solution
import os, winsound
clear= lambda: os.system('cls')
clear()

freqs = {
    "la": 220,
    "si": 247,
    "do": 261,
    "re": 293,
    "mi": 329,
    "fa": 349,
    "sol": 392,
        }

notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"

notes_split= notes.split('-')
operation_obj= iter(notes_split)
operation_list= []
while True:
    try:
        inner_obj= next(operation_obj).split(',')
        operation_list.append(inner_obj)
    except StopIteration:
        break
for list_item in operation_list:
    winsound.Beep(int(freqs[list_item[0]]),int(list_item[1]))
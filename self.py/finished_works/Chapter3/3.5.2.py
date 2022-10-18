# In the previous exercise, 
# you implemented a short program that asks the player to guess a letter, 
# but you have not yet shown him the word pattern for which he must guess letters, 
# that is, the number of letters that make up the secret word.

# It's time to create the "game board" for the player, that is, 
# the sequence of underscores that mark the position of the missing letters in the word to be guessed.

# Write a piece of code according to the following sections:

# Accept a one-word string (without spaces) from the user.
# Print a new string that will contain multiple underscores spaced next to each other, the length of the received string.

#example:
# Please enter a word: hangman
# _ _ _ _ _ _ _

# Guidelines:
# Solve the section without using loops.
# Ensure accurate output.
user_input= input("Please enter a word: ")
print("_ "*len(user_input))
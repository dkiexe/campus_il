# In the unfolding task at the end of the previous unit, you began to realize the basis of the game. 
# You have captured a character guess from the user and printed it to the screen.

# Since the size of the letters that are guessed in the game is not important (ie, lowercase or uppercase),
# you must change the piece of code you wrote so that the guessed letter is always displayed on the screen as a lowercase letter.

#example:
# Guess a letter: a
# a

# Guidelines
# Use the code section you wrote at the end of the previous unit and make the appropriate change in it.

# My solution
user_input= input("Guess a letter: ")
print(user_input.lower())
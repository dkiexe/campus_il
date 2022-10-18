# To remind you, in the task at the end of the previous unit you designed a designed opening screen for the game, and in addition you printed on the screen a random value indicating the number of (wrong) attempts available to the player in the game. Let's do the process again, but this time we'll improve it and write it correctly.

# As we have learned, as part of a proper code writing process, we must design and create variables. In this exercise you will create variables for your program, and print them.

# Write a piece of code according to the following sections:

# Define the variables:
# A constant variable called HANGMAN_ASCII_ART. The variable will point to the opening sentence and the string you printed as part of the formatted opening page you created.
# A constant variable called MAX_TRIES. The value of the variable represents the maximum number of failed attempts and is 6.
# Print the opening screen (similar to the one you printed in the rolling task at the end of the previous unit) with one print command. This time do it by using the variables you defined.

# Guidelines:
# Ensure accurate output.
# To drop a line (ie start a new line) write the character n\ in the desired place in the string.
# Do not hesitate to use the code you wrote in the exercise at the end of the previous unit.

# My solution
HANGMAN_ASCII_ART = "Welcome to the game Hangman\n" + """  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/        """
MAX_TRIES = 6

print(HANGMAN_ASCII_ART + "\n" + str(MAX_TRIES))
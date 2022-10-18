# Remember the unfolding task at the end of the previous unit, 
# where we received a guess from the player? 
# Have you ever wondered what happens if the player accidentally types a character that is not an English letter? 
# Or more than one died?
# When we ask for input from the user, 
# we must assume that the input will not necessarily be correct and therefore it is our responsibility to perform correctness checks on it.

# In this exercise you must receive a note from the user (the player). 
# Depending on the received character, print a message to the screen regarding its correctness, 
# according to the following requirements:

# For an invalid character:
# If the player entered a string of letters with more than one letter, print the string "E1" to the screen.
# If the player entered a character that is not an English letter (for example a sign like: &, *), 
# print the string "E2" to the screen.
# If the player entered a letter string that has more than one character and also contains non-English characters, 
# print the string "E3" to the screen.
# For a valid character:
# If the received character is one character and also an English letter (and not another character), 
# print it to the screen as a lowercase letter.

# example
# Guess a letter: a
# a
# Guess a letter: A
# a
# Guess a letter: $
# E2
# Guess a letter: ab
# E1
# Guess a letter: app$
# E3

# Guidelines
# Ensure accurate output.
# Observe spacing conventions, choose clear variable names and observe proper block structure.
# If necessary, use the code you wrote in the exercise at the end of the previous unit as a skeleton for building this program.

#My solution
user_input= input("Guess a letter: ")
if len(user_input)<=1:
    if user_input.isidentifier():
        print(user_input.lower())
    else:
        print('E2')
else:
    if user_input.isidentifier():
        print('E1')
    else:
        print('E3')
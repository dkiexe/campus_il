# In the task at the end of the previous unit, you thoroughly dealt with cases where the player types input that is not correct. 
# Since the game "Hanged Man" includes many guesses, the question arises: 
# will we copy all these lines of code over and over again for each guess? of course not.

# That's why we will bundle part of the logic from the previous task as a function called is_valid_input. The function is defined as:

# def is_valid_input(letter_guessed):

# Implement the is_valid_input function. 
# The function receives as a parameter the string letter_guessed, 
# which represents the received character, and returns a Boolean value representing whether the character is correct or not.

# The function returns false (False, an invalid string) in the following cases:
# If the letter_guessed string consists of two or more characters
# If the string letter_guessed contains a sign that is not an English letter (like: &, *)
# The function returns true (True, a valid character) if the letter_guessed string consists of only one letter that is an English letter (and not another character).
# 
# Examples of running the is_valid_input function
# >>> is_valid_input('a')
# True
# >>> is_valid_input('A')
# True
# >>> is_valid_input('$')
# False
# >>> is_valid_input("ab")
# False
# >>> is_valid_input("app$")
# False

# Guidelines
# Ensure accurate output.
# Use the program you wrote in the task at the end of the previous unit.

#My solution
def is_valid_input(letter_guessed):
    """
    Checks the users input string for a valid english character or if the user inputed
    more than one english character.
    :arguments: users string
    :argument-type: Str  
    :returns: True/False
    :return-type: Bool 
    """
    if len(letter_guessed)>=2:
        return False
        #checking if user guessed more then one letter
    else:
        # english_char_checker
        return letter_guessed.isidentifier()
# To remind you, in the unfolding task at the end of the previous unit, you wrote a function to check the correctness of input from the user. In this exercise, you will upgrade the function so that it also refers to the letters that the player has already guessed in the game in the tests.

# Write the function again, this time call it check_valid_input, and define it as follows:

# def check_valid_input(letter_guessed, old_letters_guessed):
# Acceptance values ​​of the function:
# A string called letter_guessed. The string represents the character received from the player.
# A list called old_letters_guessed. The list contains the letters the player has guessed so far.
# The return values ​​of the function
# The function returns a Boolean value representing the correctness of the string and whether the user has already guessed the character before.

# The function returns false (False, an invalid string) in the following cases:
# If the letter_guessed string consists of two or more characters
# If the string letter_guessed contains a sign that is not an English letter (like: &, *)
# If the letter_guessed string is a character already in the old_letters_guessed list (that is, this character has been guessed before and therefore it is illegal to guess it again)
# The function returns true (True, a valid character) if the letter_guessed string consists of only one letter that is an English letter (and not another character) that is not in the old_letters_guessed list (that is, this character was not guessed before).
# Examples of running the check_valid_input function

# >>> old_letters = ['a', 'b', 'c']
# >>> check_valid_input('C', old_letters)
# False
# >>> check_valid_input('ep', old_letters)
# False
# >>> check_valid_input('$', old_letters)
# False
# >>> check_valid_input('s', old_letters)
# True

# My solution:
def check_valid_input(letter_guessed, old_letters_guessed):
    lowercase_letter_guessed= letter_guessed.casefold()
    """
    Checks the users input string for a valid english character or if the user inputed
    more than one english character, than checks if the user already inputed that character if not adds it
    to a global list.
    :arguments: users string
    :argument-type: Str  
    :returns: True/False
    :return-type: Bool 
    """
    if len(lowercase_letter_guessed)>=2:
        return False
        #checking if user guessed more then one letter
    else:
        # english_char_checker
        if lowercase_letter_guessed.isidentifier():
            if lowercase_letter_guessed not in old_letters_guessed:
                old_letters_guessed.append(lowercase_letter_guessed)
                return True
            else:
                return False
        else:
            return False
# In this exercise, you will act in accordance with the new letter that the player guessed: either you will add it to the list of guesses, or you will print a message if it is not possible to add it.

# Write a function called try_update_letter_guessed defined as follows:

# def try_update_letter_guessed(letter_guessed, old_letters_guessed):
# The function's acceptance values
# A string called letter_guessed. The string represents the character received from the player.
# A list called old_letters_guessed. The list contains the letters the player has guessed so far.
# function operation
# If the character is correct (ie one English letter) and has not been guessed before, the function will add the letter_guessed character to the old_letters_guessed list. Then it will return a true value (True) indicating that the addition was successful.
# If the character is not correct (that is, it is not a single English letter) or it is already in the list of guesses, the function will print the character X (the capital letter X) and below it the list old_letters_guessed as a string of small letters that are sorted from small to large and separated from each other by arrows (an arrow consists of the signs: <- , see sample output). The printing of the organs is to remind the player which characters he has already guessed. At the end, the function will return a false value (False), which means that it is not possible to add the character to the list of already guessed characters.
# directive
# Use the check_valid_input function that you implemented in the previous exercise.

# Examples of running the try_update_letter_guessed function

# >>> old_letters = ['a', 'p', 'c', 'f']
# >>> try_update_letter_guessed('A', old_letters)
# X
# a -> c -> f -> p
# False
# >>> try_update_letter_guessed('s', old_letters)
# True
# >>> old_letters
# ['a', 'p', 'c', 'f', 's']
# >>> try_update_letter_guessed('$', old_letters)
# X
# a -> c -> f -> p -> s
# False
# >>> try_update_letter_guessed('d', old_letters)
# True
# >>> old_letters
# ['a', 'p', 'c', 'f', 's', 'd']

#My solution
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    lowercase_letter_guessed= letter_guessed.casefold()
    old_letters_guessed.sort()
    old_letters_guessed_lowercase = list(map(lambda letter: letter.casefold(), old_letters_guessed))
    """
    This function does 3 things:
    1) checks the users input for more then one letter
    2) checks the users input for a english letter
    3) checks if the user has already inputed that letter using a list.
    :arguments: users input
    :argument-type: Str, list
    :returns: boolean value + string(if false)
    :return-type: bool
    """ 
    if len(lowercase_letter_guessed)>=2:
        #checking if user guessed more then one letter
        print('X'+'\n'+" -> ".join(old_letters_guessed[:len(old_letters_guessed)]))
        return False
    else:
        # english_char_checker
        if lowercase_letter_guessed.isidentifier():
            if lowercase_letter_guessed not in old_letters_guessed_lowercase:
                old_letters_guessed.append(letter_guessed)
                return True
            else:
                print('X'+'\n'+" -> ".join(old_letters_guessed[:len(old_letters_guessed)]))
                return False
        else:
            print('X'+'\n'+" -> ".join(old_letters_guessed[:len(old_letters_guessed)]))
            return False
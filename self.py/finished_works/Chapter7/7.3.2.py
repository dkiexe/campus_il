# Time to check if the player has already won, right?
# In this exercise you will write a function that checks whether the player was able to guess the secret word and thus won the game!

# Write a function called check_win defined as follows:
# def check_win(secret_word, old_letters_guessed):

# The function's acceptance values
# A string called secret_word. The string represents the secret word that the player has to guess.
# A list called old_letters_guessed. The list contains the letters the player has guessed so far.
# The return values ​​of the function
# The function returns true if all the letters that make up the secret word are included in the list of letters that the user guessed. 
# Otherwise, the function returns false.

# Examples of running the check_win function
# >>> secret_word = "friends"
# >>> old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']
# >>> print(check_win(secret_word, old_letters_guessed))
# False
# >>> secret_word = "yes"
# >>> old_letters_guessed = ['d', 'g', 'e', ​​'i', 's', 'k', 'y']
# >>> print(check_win(secret_word, old_letters_guessed))
# True

# My solution
def check_win(secret_word, old_letters_guessed):
    right_letters= []
    for letter in secret_word:
        if letter in old_letters_guessed:
            right_letters.append(letter)
        else:
            continue
    if len("".join(right_letters)) == len(secret_word):
        return True
    else:
        return False
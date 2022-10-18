# In this exercise you will show the player his progress in guessing the secret word.

# Write a function called show_hidden_word defined as follows:
# def show_hidden_word(secret_word, old_letters_guessed):

# The function's acceptance values
# A string called secret_word. The string represents the secret word that the player has to guess.
# A list called old_letters_guessed. The list contains the letters the player has guessed so far.
# The return values ​​of the function
# The function returns a string consisting of letters and underscores.
# The string shows the letters from the old_letters_guessed list that are in the secret_word string in their appropriate position, 
# and the other letters in the string (which the player has not yet guessed) as underlines.

# Example of running the show_hidden_word function:
# >>> secret_word = "mammals"
# >>> old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
# >>> print(show_hidden_word(secret_word, old_letters_guessed))
# m _ m m _ _ s

# Guidelines
# To make it clear to the player how many letters he has left to guess, space the string when you print the underscores 
# (compare the readability of the sequence _____ to the sequence _ _ _ _ _ ). When the underscores are not separated by a space, 
# they form a continuous line).
# Please note, this is an example of improving the user experience, called in the professional language "usability". 
# That is, you emphasized that the program you wrote would be simple for the user to understand and use.

# My solution
def show_hidden_word(secret_word, old_letters_guessed):
    final = []
    for i in secret_word:
        if i in old_letters_guessed:
            final.append(i)
        else:
            final.append("_")
    return " ".join(final)
# In this task you will choose for the player a word that will be the secret word for guessing, 
# from a text file containing a list of words separated by spaces.

# Write a function called choose_word defined as follows:
# def choose_word(file_path, index):

# The function accepts as parameters:
# A string (file_path) representing a path to the text file.
# An integer (index) representing the position of a certain word in the file.
# The function returns a tuple consisting of two members in the following order:

# The number of different words in the file, i.e. not including repeated words.
# A word in the position received as an argument to the function (index), which will be used as the secret word for guessing.
# Guidelines
# Treat the positions the player enters as starting from 1 (rather than zero).
# If the position (index) is greater than the number of words in the file, the function continues to count positions in a circular fashion (that is, returns to the first position in the original list of words in the file and God forbid).
# An example of a text file that contains a list of words, called words.txt
# hangman song most broadly is a song hangman work music work broadly is typically

# Examples of running the choose_word function with the words.txt file
# >>> choose_word(r"c:\words.txt", 3)
# (9, 'most')
# >>> choose_word(r"c:\words.txt", 15)
# (9, 'hangman')

# My solution
def choose_word(file_path,index):
    with open(file_path, 'r') as file:
        words_list= file.read().strip().split(' ')
        no_dupes_list= []
        for elem in words_list:
            if elem not in no_dupes_list:
                no_dupes_list.append(elem)
                continue
            else:
                continue
        list_wrap_word_selector= words_list[index % len(words_list)-1]
        final_list= [len(no_dupes_list), list_wrap_word_selector]
    return tuple(final_list)
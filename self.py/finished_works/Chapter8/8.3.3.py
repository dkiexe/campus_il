# Write a function called count_chars defined as follows:

# def count_chars(my_str):
# The function accepts a string as a parameter.
# The function returns a dictionary, so that each element in it is a pair consisting of a key: 
# a character from the passed string (not including spaces), and an array: the number of times the character appears in the string.

# An example of running the count_chars function:
# >>> magic_str = "abra cadabra"
# >>> count_chars(magic_str)
# {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

# My solution
def count_chars(my_str):
    final_dict= {}
    for letter in my_str:
        if letter not in final_dict:
            if letter != ' ':
                final_dict[letter]= 1
                continue
            else:
                continue
        else:
            final_dict[letter]+=1
    return final_dict
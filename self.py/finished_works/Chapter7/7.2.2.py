# Write a function called numbers_letters_count defined as follows:
# def numbers_letters_count(my_str):

# The function accepts as a string parameter.
# The function returns a list in which the first member represents the number of digits in the string, 
# and the second member represents the number of letters in the string, including spaces, periods, punctuation marks, 
# and anything other than digits.

# An example of running the numbers_letters_count function:
# >>> print(numbers_letters_count("Python 3.6.3"))
# [3, 9]

# My solution
def numbers_letters_count(my_str):
    str_list= []
    num_of_numbers= 0
    num_of_chars= 0
    for elem in my_str:
        str_list.append(elem)
    for elem in str_list:
        try:
            int(elem)
        except:
            num_of_chars+=1
        else:
            num_of_numbers+=1
    return [num_of_numbers, num_of_chars]
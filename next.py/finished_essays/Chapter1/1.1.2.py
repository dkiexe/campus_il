# Write a function called double_letter defined as follows:
# def double_letter(my_str):
# The function accepts a string and returns a new string made up of two consecutive occurrences of each character in the original string.

# Examples of running the double_letter function:
# print(double_letter("python"))
# print(double_letter("we are the champions!"))
# 'ppyytthhoonn'
# 'wwee aarree tthhee cchhaammppiioonnss!!'

# Guidelines:
# It is forbidden to use an external library, except the functools library.
# Do not use loops.
# The double_letter function block must contain only one line of code.
# You can implement an additional auxiliary function as you wish.


# My solution version 1
def double_letter(my_str):
    return "".join(list(map(lambda letter: letter*2 if letter != ' ' else ' ', my_str)))
print(double_letter('python'))
print(double_letter('we are the champions!'))

#version 2
def double_letter_v2(my_str):
    return "".join(list(map(lambda letter: letter*2, my_str)))
print(double_letter_v2('python'))
print(double_letter_v2('we are the champions!'))
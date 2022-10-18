# Write a function called arrow defined as follows:

# def arrow(my_char, max_length):
# The function accepts two parameters: the first is a single character, the second is a maximum size.
# The function returns a string representing an "arrow" structure (see example), built from the input, 
# where the center of the arrow (the longest line) is the length of the size passed as a parameter.

# An example of running the arrow function
# print(arrow('*', 5))
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# In this example, the asterisk character * is passed and the maximum size is 5. That is, the middle line is 5 in length.

# My solution
def arrow(my_char, max_length):
    first_list= []
    for x in range(1, max_length+1):
        first_list.append("".join(x*my_char))
    for y in range(max_length-1, 0, -1):
        first_list.append("".join(y*my_char))
    return "\n".join(first_list)
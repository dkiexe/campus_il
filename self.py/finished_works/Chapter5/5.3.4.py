# Write a function named last_early defined as follows:
# def last_early(my_str):

# The function accepts as a string parameter. 
# The function returns true if the last character that appears in the string also appears before.
# Otherwise the function returns false.

#example
# >>> last_early("happy birthday")
# True
# >>> last_early("best of luck")
# False
# >>> last_early("Wow")
# True
# >>> last_early("X")
# False

# Guidelines
# Uppercase or lowercase letters are not important.

# My solution
def last_early(my_str):
    str_input_lower_case= my_str.casefold()
    last_letter= str_input_lower_case[len(str_input_lower_case)-1]
    first_filter= str_input_lower_case[:str_input_lower_case.find(last_letter)]+str_input_lower_case[str_input_lower_case.find(last_letter)+1:]
    return last_letter in first_filter
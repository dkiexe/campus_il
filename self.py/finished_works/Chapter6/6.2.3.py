# Write a function called format_list defined as follows:

# def format_list(my_list):
# The function receives a list of strings of even length. The function returns a string containing the members of the list in the even positions, separated by a comma and a space, and also the last member with the inscription and before it.

# An example of running the format_list function
# >>> my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
# >>> format_list(my_list)
# hydrogen, lithium, boron, and magnesium

# Guidelines
# Do not use loops.

# My solution
def format_list(my_list):
    return (", ".join(my_list[::2])+', and '+ my_list[len(my_list)-1])
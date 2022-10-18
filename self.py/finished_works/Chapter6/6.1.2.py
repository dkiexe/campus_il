# Write a function called shift_left. The function accepts a list of length 3 and returns a new list shifted one step to the left.

# function definition
# def shift_left(my_list):

# Examples of running the shift_left function
# >>> shift_left([0, 1, 2])
# [1, 2, 0]
# >>> shift_left(['monkey', 2.0, 1])
# [2.0, 1, 'monkey']

# My solution
def shift_left(my_list):
    """
    moves the array one step left
    :arguments: users string
    :argument-type: list 
    :returns: list
    :return-type: list 
    """
    new_list= [my_list[1],my_list[2],my_list[0]]
    return new_list
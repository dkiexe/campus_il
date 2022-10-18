# Write a function called is_greater defined as follows:
# def is_greater(my_list, n):

# The function accepts two parameters: a list and a number n.
# The function returns a new list containing all the elements that are greater than the number n.

# An example of running the is_greater function:
# >>> result = is_greater([1, 30, 25, 60, 27, 28], 28)
# >>> print(result)
# [30, 60]

# My solution
def is_greater(my_list, n):
    resault= []
    for num in my_list:
        if num> n:
            resault.append(num)
        else:
            continue
    return resault
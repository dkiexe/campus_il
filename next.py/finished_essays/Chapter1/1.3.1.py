# Write a function called intersection defined as follows:
# def intersection(list_1, list_2):
# The function accepts two lists and returns a list of the members that are in the intersection between them. That is, members that are in both the first list and the second list. No member will appear twice in the cut list.

# An example of running the intersection function:
# print(intersection([1, 2, 3, 4], [8, 3, 9]))
# print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))
# [3]
# [5,6]

# Guidelines:
# It is forbidden to use an external library, except the functools library.
# It is allowed to use the for loop only within a list assembly structure.
# The intersection function block must contain only one line of code.
# Do not implement additional helper functions in the code.

# My solution
def intersection(list_1, list_2):
    return [x for x in set(list_1) for y in set(list_2) if x==y]

print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))
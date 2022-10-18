# Write a function called extend_list_x defined as follows:
# def extend_list_x(list_x, list_y):
# The function receives two lists list_y, list_x. The function expands list_x (changes it) so 
# that it also contains list_y at the beginning, and returns list_x.

# An example of running the extend_list_x function
# >>> x = [4, 5, 6]
# >>> y = [1, 2, 3]
# >>> extend_list_x(x, y)
# [1, 2, 3, 4, 5, 6]

# Guidelines
# Do not use the '+' operator.
# Do not use the extend method.

# My solution
def extend_list_x(list_x, list_y):
    list_x.insert(0, list_y)
    list_x[0].reverse()
    for z in list_x[0]:
        list_x.insert(0, z)
    for d in list_x:
        if isinstance(d, list):
            list_x.remove(d)
        else:
            pass
    return list_x
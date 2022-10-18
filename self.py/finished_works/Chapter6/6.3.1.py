# Write a function called are_lists_equal defined as follows:

# def are_lists_equal(list1, list2):
# The function accepts two lists containing members of the int and float types only. 
# The function returns true if the two lists contain exactly the same elements (even if in different order), 
# otherwise, the function returns false.

# An example of using the are_lists_equal function:
# >>> list1 = [0.6, 1, 2, 3]
# >>> list2 = [3, 2, 0.6, 1]
# >>> list3 = [9, 0, 5, 10.5]
# >>> are_lists_equal(list1, list2)
# True
# >>> are_lists_equal(list1, list3)
# False

# Guidelines:
# Do not use loops.

# My solution:
def are_lists_equal(list1, list2):
    list1.sort()
    list2.sort()
    if len(list1)==len(list2):
        first_list_to_str= str(list1)
        second_list_to_str= str(list2)
        if first_list_to_str== second_list_to_str:
            return True
        else:
            return False
    else:
        return False
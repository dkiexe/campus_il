# Write a function called mult_tuple defined as follows:
# def mult_tuple(tuple1, tuple2):

# The function accepts as parameters two members of the tuple type.
# The function returns a tuple containing all the pairs that can be created from the members of the tuples passed as arguments.

# Running examples of the mult_tuple function
# >>> first_tuple = (1, 2)
# >>> second_tuple = (4, 5)
# >>> mult_tuple(first_tuple, second_tuple)
# ((1, 4), (4, 1), (1, 5), (5, 1), (2, 4), (4, 2), (2, 5), (5, 2))
# >>> first_tuple = (1, 2, 3)
# >>> second_tuple = (4, 5, 6)
# >>> mult_tuple(first_tuple, second_tuple)
# ((1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), 
# ( 3, 6), (4, 1), (5, 1), (6, 1), (4, 2), (5, 2), (6, 2), (4, 3), (5, 3), (6, 3))

# Guidelines
# To represent all pairs, also return pairs with members in reverse order. For example: 
# the pair (1,4) will be returned in addition to the pair (1,4).

# My solution
def mult_tuple(tuple1, tuple2):
    final_list= []
    for num1 in tuple1:
        for num2 in tuple2:
            comb1= (num1,num2)
            comb2= (num2,num1)
            final_list.append(comb1)
            final_list.append(comb2)
    return tuple(final_list)
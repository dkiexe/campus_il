# We would like to connect chocolate cubes to a row that is x cm long. We have small chocolate cubes 1 cm long and 
# large chocolate cubes 5 cm long.

# For the purpose of the task, write a function called chocolate_maker defined as follows:

# def chocolate_maker(small, big, x):

# The function receives the number of small cubes (small), the number of large cubes (big) and the desired line length (x). 
# The function returns true if it is possible to create a line of length x using the number of chocolate cubes it received, all or some.

# Guidelines
# Do not use loops.

#My solution
def chocolate_maker(small, big, x):
    small_amount_in_cm= small*1
    big_amount_in_cm= big*5
    test_chocalate_table= small_amount_in_cm+big_amount_in_cm
    if test_chocalate_table >=x:
        return True
    else:
        return False
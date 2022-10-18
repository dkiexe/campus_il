# Write a function called four_dividers defined as follows:
# def four_dividers(number):
# The function accepts a number and returns a list of all numbers from 1 to that number (inclusive) that are divisible by four without a remainder.


# Examples of running the four_dividers function:
# print(four_dividers(9))
# print(four_dividers(3))
# [4, 8]
# []
# Guidelines:
# It is forbidden to use an external library, except the functools library.
# Do not use loops.
# The four_dividers function block must contain only one line of code.
# You can implement an additional auxiliary function as you wish.

# My solution
def four_dividers(number):
    return list(filter(lambda num: num if num%4 ==0 else None, range(1, number+1)))

print(four_dividers(40))
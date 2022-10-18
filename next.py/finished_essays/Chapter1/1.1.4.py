# Write a function called sum_of_digits defined as follows:
# def sum_of_digits(number):
# The function accepts a number and returns the sum of its digits.

# An example of running the sum_of_digits function:
# print(sum_of_digits(104))
# 5

# Guidelines:
# It is forbidden to use an external library, except the functools library.
# Do not use loops.
# The sum_of_digits function block must contain only one line of code.
# You can implement an additional auxiliary function as you wish.

# My solution
from functools import reduce

def sum_of_digits(number):
    return reduce(lambda num1,num2: int(num1)+int(num2),list(str(number)))

print(sum_of_digits(206))
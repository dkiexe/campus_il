# Write a function called is_prime defined as follows:
# def is_prime(number):
# The function accepts a number and returns a boolean value representing whether it is prime (True-prime, False-not prime). A prime number is a number that is divisible by itself and 1 without a remainder.

# An example of running the is_prime function:
# print(is_prime(42))
# print(is_prime(43))
# False
# True

# Guidelines:
# It is forbidden to use an external library, except the functools library.
# It is allowed to use the for loop only within a list assembly structure.
# The is_prime function block must contain only one line of code.
# Do not implement additional helper functions in the code.

# My solution
def is_prime(number):
    return False if True in list(map(lambda x: number%x==0, range(2,number))) else True
print(is_prime(43))
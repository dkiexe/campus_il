# Write a function called first_prime_over defined as follows:
# def first_prime_over(n):
# The function accepts as a parameter an integer (n). The function returns the first prime number that comes after n.

# An example of running the first_prime_over function:
# print(first_prime_over(1000000))
# 1000003
# Realize the function so that the process of producing the initial numbers is done using a generator.

# To remind you, a prime number is a number greater than 1 that is divisible by 1 and itself only. For your convenience, 
# below is an implementation of a boolean function that checks whether a number is prime or not:
# def is_prime(n):
#      # Corner case
#      if n <= 1:
#          return False
#      # Check from 2 to n-1
#      for i in range(2, n):
#          if n % i == 0:
#              return False
#      return True

# My solution
def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def first_prime_over(n):
    generator= (z for z in range(n,n**n) if is_prime(z))
    return next(generator)
print(first_prime_over(1000000))
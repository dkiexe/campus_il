# Write a generator function called get_fibo defined as follows:
# def get_fibo():
# The function returns a generator that produces members of the Fibonacci series.

# In mathematics, the Fibonacci series is a series whose first two terms are 0 and 1 and each term after that is equal to the sum of the two numbers preceding it.
#  Accordingly, the first members of the series are:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...

# An example of running the get_fibo generator function:

# fibo_gen = get_fibo()
# print(next(fibo_gen))
# print(next(fibo_gen))
# print(next(fibo_gen))
# print(next(fibo_gen))
# 0
# 1
# 1
# 2

# Guidelines:
# A generator function that returns a generator for generating numbers in the Fibonacci series.

# My solution
def get_fibo():
    """
    Fibonachi generator! my version
    """
    x= [0,1]
    y=0
    yield x[y]
    while True:
        b= x[len(x)-2]+x[len(x)-1]
        x.append(b)
        y+=1
        yield x[y]

lak= get_fibo()
print(next(lak))
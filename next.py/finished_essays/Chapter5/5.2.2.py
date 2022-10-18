# Given the following code:

# numbers = iter(list(range(1, 101)))
# for i in numbers:
#      print(i)
# Change the code so that it prints every third number only, 
# without using the if statement.

# My solution
numbers = iter(list(range(1, 101)))

for i in numbers:
    try:
        next(numbers)
        next(numbers)
        print(i)
    except:
        break
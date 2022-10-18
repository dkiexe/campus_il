# Write a function called squared_numbers defined as follows:
# def squared_numbers(start, stop):

# The function accepts two integers, start and stop (assume that: start <= stop).
# The function returns a list containing all the squares of the numbers between start and stop (inclusive).

# Guidelines
# Use a while loop only.

# Running examples of the squared_numbers function
# >>> squared_numbers(4, 8)
# [16, 25, 36, 49, 64]
# >>> squared_numbers(-3, 3)

# My solution
def squared_numbers(start, stop):
    final_list=[]
    final_list.append(start**2)
    while start<stop:
        start+=1
        final_list.append(start**2)
    final_list.append(stop**2)
    final_list.pop()
    return final_list
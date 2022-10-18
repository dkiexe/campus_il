# In your wallet are 3 $20 bills, 5 $10 bills, 2 $5 bills, and 5 $1 bills.

# In how many ways can you create a sum of 100 dollars from the bills?

# For example, one way could be using 3 20 bills and 4 10 bills.

# Write a program that prints to the screen all the options that can be used to create an amount of 100 dollars from the bills.

# How many options did you get?

# Guidelines:

# Use the function from the itertools library to perform the calculation.
# Avoid duplication in the calculation. For example, 
# the option: 10 10 10 10 20 20 20 is exactly the same as the option 20 20 20 10 10 10 10. The internal order does not matter, so these options are counted only once.

# My solution
import os
import itertools
clear= lambda: os.system('cls')
clear()

money= [20,20,20,10,10,10,10,10,5,5,1,1,1,1,1]
final_set= set({})

for length in range(len(money)+1):
    for comb in itertools.combinations(money,length):
        if sum(comb)==100:
            final_set.add(comb)

print(final_set)
print(len(final_set))
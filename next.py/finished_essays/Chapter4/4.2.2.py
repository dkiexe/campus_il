# Write a function called parse_ranges defined as follows:

# def parse_ranges(ranges_string):
# The function accepts as a parameter a string called ranges_string that represents ranges of numbers, 
# and returns a generator that produces all the numbers in these ranges.

# An example of running the parse_ranges function:
# print(list(parse_ranges("1-2,4-4,8-10")))
# print(list(parse_ranges("0-0,4-8,20-21,43-45")))
# [1, 2, 4, 8, 9, 10]
# [0, 4, 5, 6, 7, 8, 20, 21, 43, 44, 45]
# Pay attention in the example to how the string of number ranges is written: a number indicating the beginning of a range, a dash, a number indicating the end of a range, a comma, and so on).

# Guidelines:
# Realize the generator using a generator expression.
# You can divide the task into two separate operations by implementing two generators. Write the solution using the generator piping process.

# My solutionn
import os,time
clear= lambda: os.system('cls')
clear()

def parse_ranges(ranges_string):
    seperator= ranges_string.split(',')
    
    generator1= (gen_ele1.split('-') for gen_ele1 in seperator)

    generator2= (range(int(gen_ele2[0]),int(gen_ele2[1])+1) for gen_ele2 in generator1)

    generator3= (return_number for range_representor in generator2 for return_number in range_representor)
    return generator3

print(list(parse_ranges("0-0,4-8,20-21,43-45")))
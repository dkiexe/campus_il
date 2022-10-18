# Write a function called distance defined as follows:
# def distance(num1, num2, num3):

# The function accepts three integers: num1, num2, num3.

# The function returns true if both conditions are met:

# One of the numbers num2 or num3 is "close" to num1. "Near" = absolute distance 1.
# One of the numbers num2 or num3 is "far" from the other two numbers. "Far" = absolute distance 2 or more.

#example 
# >>> distance(1, 2, 10)
# True
# >>> distance(4, 5, 3)
# False

# Guidelines
# You can use the built-in function (abs(num)) which calculates the absolute value of a number

#My solution
def distance(num1, num2, num3):
    num1_pos= abs(num1)
    num2_pos= abs(num2)
    num3_pos= abs(num3)
    if (abs(num2_pos-num1_pos)==1 or abs(num3_pos-num1_pos)==1) and (abs(num2_pos-num1_pos)>=2 and abs(num2_pos-num3_pos)>=2) or (abs(num3_pos-num1_pos)>=2 and abs(num3_pos-num2_pos)>=2):
        return True
    else:
        return False
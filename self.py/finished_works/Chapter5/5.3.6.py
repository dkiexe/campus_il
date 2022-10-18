# Write a function called filter_teens defined as follows:

# def filter_teens(a, b, c):

# The function receives three values representing ages: a, b, c and returns their sum.

# Guidelines
# If the function is called with no parameters, the default value of each age is 13.
# If one of the values represents the age of teenagers between 13 and 19 (including them) 
# but excluding the ages 15 and 16 - adjust its value using the function described below, so that it is calculated as 0.

# Write a helper function fix_age defined as follows:
# def fix_age(age):

# Running examples of the filter_teens function
# >>> filter_teens()
# 0
# >>> filter_teens(1, 2, 3)
# 6
# >>> filter_teens(2, 13, 1)
# 3
# >>> filter_teens(2, 1, 15)
# 18

# My solution
def filter_teens(a=13, b=13, c=13):
    a_fixed= fix_age(a)
    b_fixed= fix_age(b)
    c_fixed= fix_age(c)
    return a_fixed+b_fixed+c_fixed

def fix_age(age):
    if age<=19 and age>=13:
        if age==16 or age==15:
            return age
        else:
            return 0
    else:
        return age
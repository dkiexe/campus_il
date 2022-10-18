# We are nearing the end of the course and at this stage you can combine the topics learned throughout the course, 
# explore additional options yourself and apply everything in writing the code.

# In this exercise, write a function called inverse_dict defined as follows:

# def inverse_dict(my_dict):
# The function accepts as a parameter a dictionary.
# The function returns a new dictionary with a "reverse" mapping: 
# each key in the passed dictionary is a value in the returned dictionary and each value in the passed dictionary is a key in the returned dictionary.

# Guidelines
# The inversion between keys and values ​​may create keys that appear more than once. Therefore, 
# display the values ​​in the returned dictionary as a list, which may contain one or more values.
# The returned lists should be sorted (it can be assumed that the values ​​in the dictionary are of the same type).
# In the last chapter you got to know several operations in working with dictionary type objects. In this exercise, 
# read on the Internet about useful methods for working with a dictionary and explore additional operations yourself.
# 
# An example of running the inverse_dict function
# >>> course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
# >>> inverse_dict(course_dict)
# {3: ['I', 'love'], 2: ['self.py!']}

# My solution
def inverse_dict(my_dict):
    new_dict= {}
    for value in my_dict.values():
        if value not in new_dict.keys():
            new_dict[value]= []
        else:
            continue
    for key in my_dict.keys():
        if my_dict[key] in new_dict.keys():
            new_dict[my_dict[key]].append(key)
            continue
        else:
            continue
    for list in new_dict.values():
        list= list.sort()
    return new_dict
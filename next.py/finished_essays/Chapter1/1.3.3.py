# Here is a function called is_funny that accepts a string and returns true only if the received string is made up entirely of the characters 'h' and 'a':
# def is_funny(string):
#      for char in string:
#          if char != 'h' and char != 'a':
#              return False
#      return True

# Write the function is_funny so that it performs the same operation, in only one line of code.
# An example of running the is_funny function:
# print(is_funny("hahahahahaha"))
# True

# My solution
def is_funny(string):
    return True if list(map(lambda letter: letter=='a' or letter=='h',[lett for lett in string])).count(True)==len([lett for lett in string]) else False

print(is_funny('ahahahahahahahb'))
print(is_funny('ahahahahahahaha'))
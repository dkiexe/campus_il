# Write a program that accepts a string of his choice from the user.
# The program will print to the screen a string in which all occurrences of the first character have been replaced by the character 'e',
#  except for the first character itself.

# Guidelines
# Do not use loops.
# Look for a useful method that can give you an answer to the problem.

# My solution
text = input("Please enter a string: ")
text = text[0] + text[1:].replace(text[0], "e")
print(text)
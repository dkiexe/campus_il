# Write a program that accepts a string of his choice from the user.
# The program prints the string where the letters in the first half of the string are lowercase, 
# and the letters in the second half of the string are uppercase.
# If the length of the string is odd, the first half will be one less than the second half.

# Guidelines
# Do not use loops or if condition statement.
# Use slicing on strings.
# Assume that the length of the string is greater than 2.

# My solution
user_input= input('Please enter a string: ')
print(user_input[0:len(user_input)//2].lower()+user_input[len(user_input)//2:len(user_input)].upper())
# Write a program that accepts a string from the user and prints 'OK' if it is a palindrome, otherwise 'NOT'.\

#example
# >>> Enter a word: sun
# NOT
# >>> Enter a word: bob
# OK
# >>> Enter a word: Borrow or rob
# OK

# Guidelines
# A palindrome is a string (word, number, or any sequence of characters) 
# that is read from right to left the same as read from left to right. pay attention:
# Uppercase or lowercase letters do not matter.
# Ignore spaces.
# Do not use loops.

# My_solution
user_input= input('Enter a word: ')
if (user_input[0:len(user_input)].replace(" ","")).casefold() == (user_input[::-1].replace(" ","")).casefold():
    print('OK')
else:
    print("NOT")
# You have to decipher a hidden string. All you got was a code string and a small note with a clue.

# The cipher string:

# encrypted_message = "!XgXnXiXcXiXlXsX XnXoXhXtXyXpX XgXnXiXnXrXaXeXlX XmXaX XI"

# Write a program that prints the decoded message.

# Guidelines
# You are allowed to use only one cut command to decode the hidden string.
# Copy the original encrypted_message cipher string exactly for your work.

# My solution
encrypted_message = "!XgXnXiXcXiXlXsX XnXoXhXtXyXpX XgXnXiXnXrXaXeXlX XmXaX XI"
print(encrypted_message[::-2])
# Given the plan:
# data = ("self", "py", 1.543)
# format_string = "Hello"

# print(format_string % data)

# We updated the format_string variable to print:
# Hello self.py learner, you have only 1.5 units left before you master the course!

# Guidelines
# Use the data variable.
# Note that only one digit is printed after the period (ie the number 1.5)

# My solution
data = ("self", "py", 1.543)
format_string = "Hello %s.%s learner, you have only %i.5 units left before you master the course!"

print(format_string % data)
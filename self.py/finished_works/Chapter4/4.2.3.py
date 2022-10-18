# Write a program that converts a temperature in degrees Celsius to a temperature in degrees Fahrenheit.
# The program receives a temperature from the user: either in degrees Celsius, with the suffix C, 
# or in degrees Fahrenheit, with the suffix F.
# If the temperature is in degrees Celsius, convert it to degrees Fahrenheit, 
# and if the temperature is in degrees Fahrenheit, convert it to degrees Celsius.

#example
# >>> Insert the temperature you would like to convert: 50F
# 10C

# Guidelines
# The temperature can be either an integer or a non-integer (int or float).
# The suffix can be a lowercase letter or an uppercase letter (c, C, f, F).
# To make sure your program is working properly, search the Internet for temperature conversion calculators.

#My solution
user_input= input('Insert the temperature you would like to convert: ')
if 'f' in user_input.casefold():
    f_index= user_input.casefold().find('f')
    user_input= user_input[:f_index]+user_input[f_index+1:]
    user_input= float(user_input)
    print(str((user_input - 32.0) * 5.0/9.0)+'c')
elif 'c' in user_input.casefold():
    c_index= user_input.casefold().find('c')
    user_input= user_input[:c_index]+user_input[c_index+1:]
    user_input= float(user_input)
    print(str(user_input * (9.0/5.0) + 32.0)+'f')
# Write a function called sequence_del defined as follows:
# def sequence_del(my_str):

# The function accepts a string and deletes the letters appearing in sequence.
# That is, the function returns a string in which only one character appears from each sequence of identical characters in the input string.

# Running examples of the sequence_del function
# >>> sequence_del("ppyyyyythhhhhooonnnnn")
# python
# >>> sequence_del("SSSSsssshhhh")
# 'ssh'
# >>> sequence_del("Heeyyy yyouuuu!!!")
# 'Hey you!

# My solution
def sequence_del(my_str):
    last_letter= ''
    new_str= []
    for letter in my_str:
        if letter != last_letter:
            last_letter= letter
            new_str.append(letter)
        else:
            continue
    return ''.join(new_str)
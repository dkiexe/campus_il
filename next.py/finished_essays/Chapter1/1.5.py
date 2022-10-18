# You have a file named names.txt that contains a list of names, one name per line.
# Click here to download the file to your computer. Place the file in the folder from which you run the code and perform the following tasks:

# Write a program that prints to the screen the longest name in the file. Here is the expected output:

# Valdimir
# Limitation: The solution must include no more than two lines of code.

# Write a program that prints to the screen the sum of the lengths of the names in the file. Here is the expected output:

# 38
# Limitation: The solution must include no more than two lines of code.

# Write a program that prints to the screen the shortest names in the file, each name on a separate line. Here is the expected output:

# Ed
# Jo
# Limitation: The solution must include no more than four lines of code.

# Write a program that creates a new file named name_length.txt that contains the length of each name in the names.txt file, in order, one per line. Here is the expected output:

# 4
# 4
# 8
# 7
# 2
# 5
# 6
# 2
# Limitation: The solution must include no more than three lines of code.

# Write a program that receives from the user a number representing the length of a name and prints all the names in the names.txt file that are of this length. Below is a sample run and output:

# Enter name length: 4
# Hans
# Anna

# My solution
from functools import reduce
def longest_list_element():
    with open('test_text.txt', 'r') as file:
        print(max([x.strip() for x in file.readlines()],key=len))

def leangth_of_all_list_elements():
    with open('test_text.txt', 'r') as file:
        print(reduce(lambda x,y: x+y,[len(z.strip()) for z in file.readlines()]))

def print_shortest_names():
    with open('test_text.txt', 'r') as file:
        main_list= [z.strip() for z in file.readlines()]
        smallest_element_len= len(min(main_list,key=len))
        print('\n'.join(list(filter(lambda x: len(x)==smallest_element_len,main_list))))

def leangths_of_each_list_elements():
    with open('test_text.txt', 'r') as file:
        print("\n".join(list(map(lambda x: str(len(x)),[z.strip() for z in file.readlines()]))))

def return_item_by_len_input():
    with open('test_text.txt', 'r') as file:
        user_input= input('Enter name length: ')
        print("\n".join(list(filter(lambda x: len(x)==int(user_input),[z.strip() for z in file.readlines()]))))
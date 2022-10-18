# Write a program that receives from the user a single string representing a list of products for shopping, 
# separated by commas without spaces.
# An example of an input string: "Milk,Cottage,Tomatoes".

# The program asks the user to key in a number (digit) in the range of one to nine 
# (there is no need to check the correctness of the input).
# Depending on the number received, perform one of the following actions, according to the following breakdown:

# Printing the list of products
# Printing the number of products in the list
# Printing the answer to the test "Is the product on the list?" (The user will be asked to enter a product name)
# Printing the answer to the test "How many times does a certain product appear?" (The user will be asked to enter a product name)
# Deleting a product from the list (the user will be asked to tap a product name, only one product will be deleted)
# Adding a product to the list (the user will be asked to tap a product name)
# Printing all invalid products (a product is invalid if its length is less than 3 or it contains characters other than letters)
# Removing all existing duplicates in the list
# Output
# Please note, after the user makes a selection, 
# the user will return to the main menu until he selects the exit (he will press the number 9).

# Guidelines
# Transfer the products that the program accepts to the list.
# Use additional functions of your choice.

# My solution
def shopping_list_commands():
    shopping_input= input('please enter list: ')
    shopping_list= shopping_input.split(',')
    on= True
    while on== True:
        user_command= input('Please input a number between (1-9): ')
        if user_command == '1':
            print(shopping_list)
        elif user_command == '2':
            print(len(shopping_list))
        elif user_command == '3':
            look_for= input('Input a item to search: ')
            print(look_for in shopping_list)
        elif user_command == '4':
            look_for= input('Input a item to look for: ')
            times_poped_up= 0
            for item in shopping_list:
                if item== look_for:
                    times_poped_up+=1
                else:
                    continue
            print(times_poped_up)
        elif user_command == '5':
            item_to_del= input('Input a item to delete: ')
            for item in shopping_list:
                if item== item_to_del:
                    shopping_list.remove(item)
                else:
                    continue
        elif user_command == '6':
            item= input('insert an item to add: ')
            shopping_list.append(item)
        elif user_command == '7':
            for item in shopping_list:
                if len(item)<3:
                    print(item)
                else:
                    if item.isidentifier():
                        continue
                    else:
                        print(item)
        elif user_command == '8':
            final_list= []
            for item in shopping_list:
                if item not in final_list:
                    final_list.append(item)
                else:
                    continue
            shopping_list.clear()
            shopping_list= final_list
        elif user_command == '9':
            on= False
        else:
            print('non valid input detected restart app...')

shopping_list_commands()
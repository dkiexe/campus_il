# Write a function called seven_boom which simulates the game "Seven Boom". The function is defined as:
# def seven_boom(end_number):

# The function accepts an integer, end_number.
# The function returns a list in the range of numbers 0 to end_number inclusive, 
# with certain numbers replaced by the string 'BOOM', if they meet one of the following conditions:

# The number is a multiple of the number 7.
# The number contains the digit 7.
# Example of running the seven_boom function:
# >>> print(seven_boom(17))
# ['BOOM', 1, 2, 3, 4, 5, 6, 'BOOM', 8, 9, 10, 11, 12, 13, 'BOOM', 15, 16, 'BOOM']

# My solution
def seven_boom(end_number):
    test_list= []
    for num in range(0, end_number+1):
        ref_list=[]
        if num%7 == 0:
            print('yes', num)
            test_list.append('BOOM')
            continue
        else:
            for index in str(num):
                ref_list.append(index)
            if '7' in ref_list:
                test_list.append('BOOM')
            else:
                test_list.append(num)
    return test_list
# Write a function called who_is_missing defined as follows:
# def who_is_missing(file_name):

# The function accepts as a parameter a path to a text file (string).
# The file we return is passed as an argument and contains a list of integers from 1 to some n, 
# which are not sorted, separated by commas, when one of the numbers in the sequence disappears (that is, missing from the sorted list).

# The operation of the who_is_missing function:
# A. The function returns the missing number in the sequence (int).
# B. The function writes the missing number in sequence to a new file called found.txt.

# An example of an input file and the execution of the who_is_missing function
# A file called findMe.txt:

# 8,1,9,7,4,6,3,2
# Running the who_is_missing function on the findMe.txt file:

# >>> who_is_missing("c:\findMe.txt")
# 5

# After the above run of the who_is_missing function, a new file called found.txt is created:
# 5

# My solution
def who_is_missing(file_name):
    with open(file_name, 'r') as sequance:
        main_list= sequance.read().split(',')
        num_list= [int(elem) for elem in main_list]
        if max(num_list) == min(num_list):
            new_file= open("c:\found.txt",'w')
            new_file.write(str(1))
            new_file.close()
            return 1
        else:
            missing_num= ''
            for number in range(min(num_list),max(num_list)):
                if number not in num_list:
                    missing_num= str(number)
                    break
                else:
                    continue
            new_file= open("c:\found.txt",'w')
            new_file.write(missing_num)
            new_file.close()
            return int(missing_num)
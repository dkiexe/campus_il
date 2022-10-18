# Write a function called are_files_equal defined as follows:
# def are_files_equal(file1, file2):

# The function accepts as parameters paths of two text files (strings).

# The function returns true (True) if the files are identical in content, otherwise returns false (False).

# An example of running the are_files_equal function with different files
# >>> are_files_equal("c:\vacation.txt", "c:\work.txt")
# False

# My solution
def are_files_equal(file1, file2):
    fl1= open(file1)
    fl2= open(file2)
    line1 = fl1.readlines()
    line2= fl2.readlines()
    if line1 == line2:
        fl1.close()
        fl2.close()
        return True
    else:
        fl1.close()
        fl2.close()
        return False
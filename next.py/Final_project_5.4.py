# You have been asked to help the Population Authority write a program that generates numbers for identity cards - a program that assigns a new identity card number to every Israeli resident or citizen upon registration of birth, or upon immigration to Israel.

# An ID number consists of nine digits. Of course, not every nine-digit number is a valid social security number.

# Below is a description of the process of checking the correctness of an identity card. For the purpose of the example, we will check the validity of the following ID card: 123456782.

# First step: Multiply each digit in the ID by 1 or 2 depending on its position in the number. A digit in an odd position is multiplied by 1 and a digit in an even position is multiplied by 2. for example:

# id char:        |1     2     3     4      5       6        7       8      2|
# multiplyied by: |1     2     1     2      1       2        1       2      1|
# result          |1     4     3     8      5       12       7       16     2|

# Second step: We will go through each number obtained as a result of the multiplication operation and check if it is greater than 9. If so, we will add its two digits. Otherwise, we will leave it as is. For example, 16 is greater than 9, so we will add its two digits (1+6) and get 7.

# Third step: We will add up all the numbers that came out in the result.

# Fourth step: We will check whether the number obtained as a result of the third step is divisible by 10 without a remainder. If so, the ID number is correct, 
# otherwise - incorrect.

# An example of each process of checking the correctness of an identity card:
# id char:                                             |1     2     3     4      5       6        7       8      2|
# multiplyied by:                                      |1     2     1     2      1       2        1       2      1|
# result                                               |1     4     3     8      5       12       7       16     2|
# combining the 2 digits of a number bigger than 9:    |1     4     3     8      5       3        7       7      2|
# Sum of all numbers:                                                              40

# Is 40 divisible by 10 without a remainder? Yes. The ID number is correct!

# Write a Boolean function called check_id_valid that is defined as follows:
# def check_id_valid(id_number):

# The function accepts as a parameter an ID number (whole number) and returns a true value (True) if it is correct, 
# otherwise it returns a false value (False). The correctness of the identity card will be checked in the manner described in the introduction of the exercise (recommendation: you can use the code in one line - One Liners as we learned in the first chapter).

# Examples of running the check_id_valid function:
# print(check_id_valid(123456780))
# print(check_id_valid(123456782))
# False
# True

# Actually a class that represents an iterator called IDIterator.

# Add an attribute named id_ to the class that represents an ID number in the range between 100000000 and 999999999 (this attribute is initialized when creating an iterator instance of the class).

# Right in the class is a __iter__ method that returns the iterator instance.

# Right in the department there is a method __next__ that returns every time the next valid ID number in the range between id_ (inclusive) and 999999999.

# Attention: don't forget to set a stopping condition for the iterator. If you have reached the end of the range (ie ID card with the number 999999999) throw a StopIteration exception.

# Guidelines:

# Do not use generators.

# Check that the code works as follows:

# Write a main program that receives an ID number from the user (assume that the input is correct. That is, it consists of 9 characters representing digits and is greater than 100000000).
# for example:
# The input "1234567" is incorrect because it does not consist of 9 digits.
# The input "a123b5678" is invalid because it includes non-numeric characters.
# The input "001234567" is incorrect because it represents a number whose value is less than 100000000.
# Create an iterator from the class you created. Start the iterator with the ID number you received from the user and use it to generate 10 new ID numbers, which you will print to the screen.
# For example, when a user enters the ID number 123456780 as input, the following output is obtained.

# Enter ID: 123456780
# 123456782
# 123456790
# 123456808
# 123456816
# 123456824
# 123456832
# 123456840
# 123456857
# 123456865
# 123456873
# Please note: generation of 10 numbers starts with the ID number that comes after the number received. That is, the first ID number received is not included in the 10 numbers that the iterator produces even if it is a valid number.

# Write a generator function called id_generator that behaves similarly to the IDIterator iterator.
# The generator function accepts an ID number as a parameter. Every time it is asked to generate a value, it generates the next valid ID number in the range (up to the number - 999999999).

# In the main program you wrote earlier, create a generator using the generator function you created. Start the generator with the identity card number you have already received from the user and use it to generate 10 numbers of new identity cards, which you will print to the screen (as it was done in the previous section).

# Upgrade the main program so that it receives two values ​​from the user:

# ID number
# A string indicating whether to use an iterator or a generator - if the user enters "it" as input, create an iterator and use it to generate 10 IDs. If the user enters "gen" as input, create a generator function and use it to create a generator that produces 10 IDs. Assume the input is correct.
# An example of running the program:

# Enter ID: 123456780
# Generator or Iterator? (gen/it)? it
# 123456782
# 123456790
# 123456808
# 123456816
# 123456824
# 123456832
# 123456840
# 123456857
# 123456865
# 123456873

# Just before the end of the exercise, please make sure you have completed all of the following sections:

# You have received an ID number from the user.
# You have implemented the check_id_valid function.
# You received a string from the user that indicates whether to use an iterator or a generator (it or gen).
# If the string the user enters as input is "it", the program creates an iterator and initializes it with the entered ID number. The iterator uses it to generate 10 numbers of new IDs. If the string that the user enters as input is "gen", the program creates a generator using the generator function, initializes it with the entered ID number and uses it to generate 10 new ID numbers.


# Your score is 100 / 100
# Examiner's comments Hi David, well done for submitting the final assignment! The score is: 100 in terms of functionality: the code you wrote runs properly and 
# matches the requirements of the assignment - it is evident that you understood the material well! In terms of readability and 
# style: an excellent understanding of the studied material was achieved. magnificent! :) You made sure to document all functions according to the docstring guidelines. 
# Documentation is an integral part of quality and professional code.
# Well done! It is important to pay attention to always give significant names to the variables because
#  it really makes it easier to read/understand the code, for example, the variable x in line 32 is not so significant. In terms of code design: 
#  the code is designed in a clear and logical way and is logically divided into classes, methods and functions according to the exercise instructions:)
#   In conclusion, there is no doubt that you have acquired many tools in Python programming! Good luck in the future! :)

# My solution
import os
import time
from functools import reduce


MAX_VALUE_FOR_ID = 999999999


def check_id_valid(id_number):
    """
    This function checks if the id_number argument is a valid ID number. If it is a valid ID number this function returns True
    else it would return False.

    The return value of the function which determines if a ID number is valid is achieved by:
    1) Separating each digit in the 'id_number' argument and placing each digit inside a list called 'list_of_digits'.
    2) Using the enumerate() function to add a position counter to each digit inside 'list_of_digits', This creates a tuple which we then
    unpack using a for loop this grants us the abillity to check if the index of a digit is a even or odd number. 
    3) If the index of a digit inside 'list_of_digits' is an odd number,
    we multiply the digit by 1 and add it to 'list_of_multiplied_digits' which stores the digits after they have
    been multiplied, If the index of a digit is a even number we multiply the digit at that index by 2.
    4) If the number we got from multiplying the digit by 2 is bigger than 9 we combine the 2 digits of that number using the reduce function
    and adding the result to 'list_of_multiplied_digits'.
    5) finally we combine all digits inside the 'list_of_multiplied_digits' by using the sum() function and return a condition(True/False) which 
    checks if the total sum of 'list_of_multiplied_digits' divides by 10 with no remainder.

    Parameter: A number between 100000000 and MAX_VALUE_FOR_ID(999999999) 
    Parameter-Type: Int
    Returns: True/False
    Return-Type: bool 
    """
    # Creating a list of digits using list comprehension.
    list_of_digits = [int(x) for x in str(id_number)]
    list_of_multiplied_digits = []
    # Using the enumerate() function to create a tuple with a index counter(starting at 1), and a digit from 'list_of_digits'.
    for index, number in enumerate(list_of_digits, start=1):
        # Checking if the index of a digit is a even number.
        if index % 2 == 0:
            new_num = number * 2
            if new_num > 9:
                #using the reduce() function to add the 2 digits of a number bigger than 9.
                new_num = reduce(lambda digit1, digit2: int(digit1)+int(digit2), str(new_num))
            list_of_multiplied_digits.append(new_num)
            continue
        else:
            list_of_multiplied_digits.append(number)
    # returning a boolean value created by the condition.
    return sum(list_of_multiplied_digits) % 10 == 0


class IDIterator:
    """
    This class represents a Iterator which creates valid ID numbers limited to 10, The limitation is done by the 'self.result_count' 
    variable inside the __init__() function which gets incremented by one each time a valid ID is found in the __next__() function.
    the 'self._id' argument in the __init__() function represents a ID number inputed by the user( Defaults value is 123456780 ), the __next__() function
    would use this number to create 10 more valid ID's upwards of the given ID.
    The __next__() function is responsible for the whole iteration process and uses both 'self._id' and 'self.result_count'.
    """
    def __init__(self, _id=123456780) -> None:
        self._id = _id
        self.result_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        """
        The __next__() function is responsible for creating valid ID numbers and returning the next one each iteration.
        This is done by incrementing the 'self._id' variable each iteration and checking if the value is valid by calling the
        check_id_valid() function inside the while loop, the while loop is combined with the not operator which reverses the outcome of the 
        check_id_valid() function, this allows the loop to run when check_id_valid() returns False and increment 'self.id' until check_id_valid()
        returns True then the loop would stop, 'self.result_count' would be incremented because we found a answer if 'self.result_count' would be bigger
        than 10 or 'self.id' would be bigger than MAX_VALUE_FOR_ID(999999999) an exception named StopIteration would be raised and the iteration
        process would be stopped.

        Returns: A valid ID number found.
        Return-type: Int  
        """
        self._id += 1
        # while loop paired with a not operator so the loop could run when check_id_valid() returns False and increment 'self._id' until check_id_valid()
        # returns True.
        while not check_id_valid(self._id):
            self._id += 1
        # Adding one to result count so we could limit our results count and stop the iteration
        self.result_count += 1
        # Checking if 'self._id' exceeded the maximum value of 999999999 or more than 10 results have been returned if yes breakes iteration with StopIteration
        if self._id > MAX_VALUE_FOR_ID or self.result_count > 10:
            raise StopIteration
        return self._id


def id_generator(ID_number=123456780):
    """
    This function is a generator that generates valid ID numbers after the 'ID_number' argument recived from the user. 
    this is done by incrementing the 'ID_number' argument by one each time and checking if the ID is a valid ID using the
    check_id_valid() function if it is valid the generator yields it. If 'ID_number' is bigger than The max value a ID could be(999999999) the while loop breaks,
    the while loop would also break if the 'result_count' variable would be bigger than 10.
    """
    # Creating a variable that would limit the results.
    result_count = 0
    while True:
        ID_number += 1
        # Checking if the ID_number is bigger than 999999999 or result_count is bigger than 10
        if ID_number > MAX_VALUE_FOR_ID or result_count > 10:
            break
        # Checks if the ID num created is a valid ID
        if check_id_valid(ID_number):
            # Adds one to the result count and yields answer
            result_count += 1
            yield ID_number
        else:
            # Continues to the next iteration of the while loop if the ID number created isnt a valid ID
            continue


def main():
    """
    This is the main function it collects essential input from the user like an ID which the program would use
    to create 10 more valid ID's upwards of the given ID, and a prefered method of creation (gen = generator/ it = iterator).
    Then this function creates a iteraor object / generator object (depending on the prefered method by the user) and prints out the results using 
    a for loop.

    Parameters: None
    Returns: None
    """
    # Collecting ID number from user.
    ID_from_user = int(input('Enter ID: '))
    # Collecting a method from the user.
    Selected_method = input('Generator or Iterator? (gen / it)? ')
    try:
        if Selected_method == 'gen':
            # Creating a generator object named 'ID_gen' and iterating over it using a for loop and next() function 10 times.
            ID_gen = id_generator(ID_from_user)
            for _ in range(10):
                print(next(ID_gen))
        elif Selected_method == 'it':
            # Creating a Iterator object named 'ID_iter' and iterating over it using a for loop and next() function 10 times.
            ID_iter = IDIterator(ID_from_user)
            for _ in range(10):
                print(next(ID_iter))
        else:
            # This else block executes when the user didn't input a valid method of creation.
            print('Please use iterator or generator')
            time.sleep(2)
            main()
    # The generator and iterator are limited to 10 ID's in case we change the range() value in the for loops to more than 10 the
    # except block would catch it and print a message.
    except StopIteration:
        print(f"\nSTOP! Reached The final limit of 10 IDs or Value of ID got bigger than {MAX_VALUE_FOR_ID}")
    finally:
        print(f'\nFinished Creating IDs Method used: {"iterator" if Selected_method == "it" else "generator"}')

if __name__ == '__main__':
    main()
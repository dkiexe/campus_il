# Ido maintains a baking blog online for food lovers. Every surfer who wants to connect to the blog is obliged to choose a username and password as follows.

# Username:
# Must consist of the following legal characters: English letters, numbers and an underscore.
# It must be between 3 and 16 characters long.

# The password:
# Must consist of at least 8 characters, and up to a maximum of 40 characters in length.
# Must contain at least one of the following mandatory characters: one uppercase English letter, one lowercase English letter, one number and one special sign such as an exclamation mark (to perform the task you can use string.punctuation).
# You must help Ido write a code that checks whether the username and password entered by surfers meet the conditions.

# Write a function called check_input defined as follows:
# def check_input(username, password):
# The function accepts two parameters of type string: username and password. The function prints "OK" to the screen if the username and password are correct (that is, meet the conditions presented earlier).

# If the username or password (or both) do not meet the defined conditions we would like to throw a detailed exception describing what went wrong. 
# For this purpose, fulfill the following exceptions:
# Exception named UsernameContainsIllegalCharacter - describes a username that contains illegal characters.
# Exception named UsernameTooShort - describes a username consisting of less than 3 characters.
# Exception named UsernameTooLong - describes a username consisting of more than 16 characters.
# An exception named PasswordMissingCharacter - describes a password that does not contain at least one of the mandatory characters.
# Exception named PasswordTooShort - describes a password consisting of less than 8 characters.
# Exception named PasswordTooLong - describes a password consisting of more than 40 characters.

# Please note: each exception is implemented in a separate class that inherits from the Exception superclass.

# We have updated the code of the check_input function so that in a situation where it receives as input an invalid username or password, an appropriate exception will be thrown.

# If everything is correct, the function will print OK as usual.

# For your convenience, we have compiled for you inputs with which you can test the code you wrote.

# check_input("1", "2")
# check_input("0123456789ABCDEFG", "2")
# check_input("A_a1.", "12345678")
# check_input("A_1", "2")
# check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
# check_input("A_1", "abcdefghijklmnop")
# check_input("A_1", "ABCDEFGHIJLKMNOP")
# check_input("A_1", "ABCDEFGhijklmnop")
# check_input("A_1", "4BCD3F6h1jk1mn0p")
# check_input("A_1", "4BCD3F6.1jk1mn0p")
# All inputs except the last one are incorrect. Make sure that for each of the inputs one exception is thrown that describes the problem with it. The order of priority of the thrown exception is determined according to the order of the clauses in the question.

# Write a main main function that receives the user's username and password for the blog. Incorporate in the main function block a call to the check_input function to check whether the input meets the conditions.

# If the input is not correct, ensure that a detailed message describing the problem with the input is printed to the user. Then ask for more input until you get proper input.

# Below is a sample run:
# check_input("1", "2")
# check_input("0123456789ABCDEFG", "2")
# check_input("A_a1.", "12345678")
# check_input("A_1", "2")
# check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
# check_input("A_1", "abcdefghijklmnop")
# check_input("A_1", "ABCDEFGHIJLKMNOP")
# check_input("A_1", "ABCDEFGhijklmnop")
# check_input("A_1", "4BCD3F6h1jk1mn0p")
# check_input("A_1", "4BCD3F6.1jk1mn0p")
# The username is too short
# The username is too long
# The username contains an illegal character
# The password is too short
# The password is too long
# The password is missing a character
# The password is missing a character
# The password is missing a character
# The password is missing a character
# OK
# Hint
# Click here to reveal the clue


# Improved the UsernameContainsIllegalCharacter and PasswordMissingCharacter exceptions to contain a more accurate description of the problem.

# So far the UsernameContainsIllegalCharacter exception class has printed a generic message:

# The username contains an illegal character

# Now, add a description of the illegal character and its position in the string to the UsernameContainsIllegalCharacter class.

# Below is a sample run:

# check_input("A_a1.", "12345678")
# The username contains an illegal character "." at index 4
# So far the PasswordMissingCharacter exception class has printed a generic message:

# The password is missing a character

# Now, create 4 subclasses that inherit from the PasswordMissingCharacter class, where each class will describe a missing character in the password.

# Note, the classes must extend the use of the __str__ method of the superclass, so that when printing it will only add in parentheses additional detail about the missing character. That is, it must use the method of the superclass and add to it.

# Here are additions for certain characters:

# For a missing capital letter add (Uppercase).
# For a missing small letter add (Lowercase).
# For a missing number add (Digit).
# For a missing special character add (Special).
# check_input("A_1", "abcdefghijklmnop")
# check_input("A_1", "ABCDEFGHIJLKMNOP")
# check_input("A_1", "ABCDEFGhijklmnop")
# check_input("A_1", "4BCD3F6h1jk1mn0p")
# The password is missing a character (Uppercase)
# The password is missing a character (lower case)
# The password is missing a character (Digit)
# The password is missing a character (Special)



# My solution
import os,time
clear= lambda: os.system('cls')
clear()
class UsernameContainsIllegalCharacter(Exception):
    __module__= 'Input ERR'
    def __init__(self, *args: object, word) -> None:
        super().__init__(*args)
        self.word= word
    def __str__(self) -> str:
        wrong_index= 0
        wrong_letter= ''
        for index,letter in zip(range(len(self.word)),self.word):
            if letter.isidentifier():
                pass
            else:
                wrong_index= index
                wrong_letter= letter
                return f'The username contains an illegal character "{wrong_letter}" at index {wrong_index}'

class UsernameTooShort(Exception):
    __module__= 'Input ERR'
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    def __str__(self) -> str:
        return "The username is too short"

class UsernameTooLong(Exception):
    __module__= 'Input ERR'
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    def __str__(self) -> str:
        return "The username is too long"

class PasswordTooShort(Exception):
    __module__= 'Input ERR'
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    def __str__(self) -> str:
        return "The password is too short"

class PasswordTooLong(Exception):
    __module__= 'Input ERR'
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    def __str__(self) -> str:
        return "The password is too long"

class PasswordMissingCharacter(Exception):
    __module__= 'Input ERR'
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    def __str__(self) -> str:
        return "The password is missing a character"
class PasswordMissingUpper(PasswordMissingCharacter):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    def __str__(self) -> str:
        return super().__str__()+'(UpperCase)'
class PasswordMissingLower(PasswordMissingCharacter):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    def __str__(self) -> str:
        return super().__str__()+'(LowerCase)'
class PasswordMissingDigit(PasswordMissingCharacter):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    def __str__(self) -> str:
        return super().__str__()+'(Digit)'
class PasswordMissingSpecial(PasswordMissingCharacter):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    def __str__(self) -> str:
        return super().__str__()+'(Special)'

def check_input(username, password):
    username_to_str= str(username)
    username_ok= False
    Password_ok= False
    #username_check
    if len(username_to_str)>=3:
        if len(username_to_str)<=16:
            if username_to_str.isidentifier():
                username_ok= True
            else:
                raise UsernameContainsIllegalCharacter(word= username)
        else:
            raise UsernameTooLong()
    else:
        raise UsernameTooShort()
    #password_check
    if len(password)>=8:
        if len(password)<=40:
            if len(list(filter(lambda x: str.isupper(x),password)))>=1:
                if len(list(filter(lambda y: str.islower(y),password)))>=1:
                    if len(list(filter(lambda z: not str.isalpha(z),password)))>=1:
                        if len(list(filter(lambda d: str.isdigit(d),password)))>=1:
                            Password_ok= True
                        else:
                            raise PasswordMissingDigit()
                    else:
                        raise PasswordMissingSpecial()
                else:
                    raise PasswordMissingLower()
            else:
                raise PasswordMissingUpper()
        else:
            raise PasswordTooLong()
    else:
        raise PasswordTooShort()
    #all ok checker
    if Password_ok and username_ok:
        print('OK')

def main():
    request_username= input('>Input username: ')
    request_password= input('>Input Password: ')
    try:
        return check_input(request_username, request_password)
    except Exception as err:
        print(err)
        time.sleep(3)
        clear()
        main()

if __name__ == '__main__':
    main()
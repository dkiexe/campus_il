# Ido's birthday is coming up, and in honor of the occasion he wants to invite his friends to the birthday. 
# Ido is interested in inviting only the people who are 18 years old or older. For this purpose, implement the following function.
# def send_invitation(name, age):
#     if int(age) < 18:
#         print("under age")
#     otherwise:
#         print("You should send an invite to " + name)
# The function send_invitations accepts two parameters: name and age. If the age is less than 18, it prints an appropriate message on the screen.

# Actually a custom exception called UnderAge.
# Right in the exception class the __str__ method. The method will return a string that tells the user that their age is less than 18. Add the present age of the invitee to the string, and in a few years he will be able to reach Ido's birthday.
# Throw away the exception you created in the code - for this purpose, replace code line number 3.
# Catch the exception in the code when it is thrown.
# To test, run the function with arguments 17 and 20.

# My solution
class UnderAge(Exception):
    def __init__(self, current_age,*args: object) -> None:
        super().__init__(*args)
        self.current_age= current_age

    def __str__(self) -> str:
        return f"Minor detected current age: {self.current_age} could enter party in: {18-self.current_age} {'year' if 18-self.current_age==1 else 'years'}"

def send_invitation(name, age):
    try:
        assert age>=18,UnderAge(age)
    except UnderAge:
        print('underage detected! ')
    else:
        print("You should send an invite to " + name)

send_invitation(
    'tommy',17
)
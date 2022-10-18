# Remember Octavio the Octopus?

# For those who don't remember, in the previous unit you were asked to write a class that represents your favorite animal (for example Octopus).
# Octavio Octopus
# Now, after you have purchased additional tools in the unit, upgrade the department you created.

# Hide the animal's name and age attributes (reminder: _).
# Allow the animal name to be determined during instance creation.
# If no name was set for the animal during the creation of the instance, make sure to initialize its name with the default value "Octavio".
# Write a method called set_name that allows you to change the name of the animal.
# It actually has a method called get_name that returns the name of the animal.
# Create a variable called count_animals designed to count how many animals were created from the class. Think: what type of variable is this, 
# and where in the code should the counting operation be placed?
# Write a main program in which you create two animal shows (one with a name of your choice, the other without).
# Print the name of each of the instances - check that for one of them the name you gave was printed and for the other the default value Octavio was printed.
# Change the name of one of the instances and print its new name after the change using the get_name method.
# Print the variable count_animals and check that the value 2 is indeed obtained (because only two animals were created from the class).

# My solution
class Octopus:
    count_animals= 0
    def __init__(self,age,name='Octavio') -> None:
        Octopus.count_animals+=1
        self._name= name
        self._age= age
    def set_name(self,new_name):
        self._name= new_name
    def get_name(self):
        return self._name

def main():
    #class instance making
    oct1= Octopus(25,'George')
    oct2= Octopus(35)
    #printing instance names
    print(oct1.get_name())
    print(oct2.get_name())
    # name changing + printing new name
    oct2.set_name('Leon')
    print(oct2.get_name())
    # printing class instance count
    print(Octopus.count_animals)
main()
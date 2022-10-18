# Write a class that represents your favorite animal (for example Octopus).
# Octavio Octopus
# Add an initialization method that will include the following attributes: the animal's name (eg Octavio) and its age.
# Add a method called birthday that will increase the animal's age by 1.
# Add a method called get_age that will return the animal's age.
# Write a main program and create two animals (that is, instances) in it.
# Run the birthday method on one live instance.
# Print the age of the two animals to the screen.
# Please note: at this stage all the animals you create using the template of the class will receive the same name that appears in the initialization method. 
# In the next unit we will learn how to give each animal a different name in the initialization phase.

# My solution
class animal:
    def __init__(self,name,age) -> None:
        self.name= name
        self.age= age

    def birthday(self):
        self.age +=1

    def get_age(self):
        print(self.age)
    
def main():
    octupos= animal('octavio',15)
    cow= animal('moshe',25)
    octupos.birthday()
    cow.get_age()
    octupos.get_age()
main()
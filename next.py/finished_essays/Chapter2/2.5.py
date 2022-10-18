# Dear learners, if you have come this far, it indicates persistence and high abilities of time management and self-learning, which goes far beyond learning Python. Don't forget that in programming, the way and repeated attempts are at least as important as the result. Successfully!

# We have created a checklist for you for exercise 2.5 through which you can test the knowledge you have acquired so far on the subject of object-oriented programming. The checklist is made up of different sections to check. Go through each section and make sure your code does meet the requirements. If you are not sure that you understood what some of the concepts in the checklist mean (for example: class attribute, initialization method, etc.) feel free to go back to the videos and/or the written content and remember. This is exactly the goal!

# The checklist is divided into three different categories of code quality: functionality, design-coding and documentation.

# First part - functionality of the code
# The code you wrote runs properly and functionally corresponds to the requirements of the assignment.
# Attached are test points for functionality testing:

# Checklist - Section 1

# (Done!) I created a class called Animal

# (Done!) I created an initialization method (__init__) in the Animal class that receives as parameters attributes: name and degree of hunger.

# (Done!) I gave a default value of 0 to the hunger_ attribute

# (Done!) I initialized the feature name_

# Checklist - Section 2 (Done!) 

# (Done!)  I created a subclass called Dog that inherits from the Animal class

# (Done!)  I created a subclass called Cat that inherits from the Animal class

# (Done!)  I created a subclass called Skunk that inherits from the Animal class

# (Done!)  I created a subclass named Unicorn that inherits from the Animal class

# (Done!)  I created a subclass called Dragon that inherits from the Animal class

# Checklist - Section 3

# (Done!)  I implemented a get_name method in the Animal class that returns the name of the animal

# (Done!)  I implemented a method is_hungry in the Animal class that returns a boolean value (is the animal hungry?)

# (Done!)  I implemented a feed method that subtracts one point from the animal's degree of hunger

# Checklist - Section 4

# (Done!)  I implemented a main function named main

# (Done!)  I created a list called zoo_lst

# (Done!)  I created a Dog instance with the values ​​Brownie and 10

# (Done!)  I created a Cat instance with the values ​​Zelda and 3

# (Done!)  I created a Skunk instance with the values ​​Stinky and 0

# (Done!)  I created a Unicorn instance with the values ​​Keith and 7

# (Done!)  I created a Dragon instance with the values ​​Lizzy and 1450

# (Done!)  I added 5 created instances to the zoo_lst list

# (Done!) I looped through the zoo_lst list

# (Done!)  I printed a type of each animal (type)

# (Done!)  I printed the name of each animal (name_)

# (Done!)  I fed each animal using the feed method until it was no longer hungry

# Checklist - Section 5

# (Done!)  I implemented a talk method in the Animal class that does nothing (pass)

# (Done!)  I implemented a talk method in the Dog class that prints woof woof

# (Done!)  I implemented a talk method in the Cat class that prints meow

# (Done!)  I implemented a talk method in the Skunk class that prints tsssss

# (Done!)  I implemented a talk method in the Unicorn class that prints Good day, darling

# (Done!)  I implemented a talk method in the Dragon class that prints Raaaawr

# (Done!)  I called the talk method for all instances inside zoo_list

# Checklist - Section 6

# (Done!)  I implemented the fetch_stick method in the Dog class that prints !There you go, sir

# (Done!)  I implemented the chase_laser method in the Cat class that prints Meeeeow

# (Done!)  I implemented the stink method in the Skunk class that prints Dear Lord!

# (Done!)  I implemented the sing method in the Unicorn class that prints i'm not your toy...

# (Done!)  I implemented the breath_fire method in the Dragon class that prints $@#$#@$

# (Done!)  I called each of the above methods for all instances inside zoo_list

# Checklist - Section 8

# (Done!)  I created an instance of the Dog class with the values ​​Doggo and 80

# (Done!)  I created an instance of the Cat class with the values ​​Kitty and 80

# (Done!)  I created an instance of the Skunk class with the values ​​Stinky Jr. and 80

# (Done!)  I created an instance of the Unicorn class with the values ​​Clair and 80

# (Done!)  I created an instance of the Dragon class with the values ​​McFly and 80

# (Done!)  I added the 5 instances created above to the list zoo_list

# (Done!)  Checklist - Section 9

# (Done!)  I added an attribute of class-attribute type zoo_name in the Animal class with the value "Hayaton"

# (Done!)  I added the color_ attribute to the Dragon class and initialized a default value = "'Green"


# Part two - design and coding
# Attached are points for self-testing for design and coding testing:

# Checklist - design - and coding

# (Done!)  The code you wrote is modular, well divided and there is no unnecessary duplication of code

# (Done!)  The code is designed in a clear and logical way, the use of control structures is correct


# Part three - documentation
# Attached are self-check points for document check:

# Check-list - documentation

# (Done!)  The classes in the code are well documented in a qualitative and precise manner.

# (Done!)  The methods and functions in the code are well documented in a qualitative and precise manner.

# We wish you continued fruitful and enjoyable studies.
# Successfully,
# Course staff 'next.py - your next step in Python'.


# My soltuon
class animal:
    zoo= "Hayaton"
    def __init__(self,name,hunger=0) -> None:
        self._name= name
        self._hunger= hunger
    def reset(self):
        self._hunger= 0
    def get_name(self):
        return self._name
    def is_hungry(self):
        if self._hunger > 0:
            return True
        else:
            return False
    def feed(self):
        self._hunger-=1
    def talk(self):
        pass

class mammal(animal):
    def __init__(self, name, hunger, type) -> None:
        super().__init__(name, hunger)
        self.type= type
        if self.type== 'Skunk':
            self._stink_count=6
    def talk(self):
        match self.type:
            case 'Dog':
                return 'woof woof'
            case 'Cat':
                return 'meow'
            case "Skunk":
                return 'tsssss'
    def fetch_stick(self):
        print('There you go, sir!')
    def chase_laser(self):
        print('Meeeeow')
    def stink(self):
        print('Dear lord!')

class fictional(animal):
    def __init__(self, name, hunger, type) -> None:
        super().__init__(name, hunger)
        self.type= type
        if self.type== 'Dragon':
            self._color= 'Green'
    def talk(self):
        match self.type:
            case "Unicorn":
                return 'Good day, darling'
            case "Dragon":
                return "Raaaawr"
    def sing(self):
        print('Im not your toy...')
    def breath_fire(self):
        print('$@#$#@$')

def main():
    Dog_1= mammal('Brownie',10,'Dog')
    Cat_1= mammal('Zelda',3,'Cat')
    Skunk_1= mammal('Stinky',0,'Skunk')
    Unicorn_1= fictional('Keith',7,'Unicorn')
    Dragon_1= fictional('Lizzy',1450,'Dragon')
    Dog_2= mammal('Doggo',80,'Dog')
    Cat_2= mammal('Kitty',80,'Cat')
    Skunk_2= mammal('Stinky Jr.',80,'Skunk')
    Unicorn_2= fictional('Clair',80,'Unicorn')
    Dragon_2= fictional('McFly',80,'Dragon')
    zoo_lst= [Dog_1,Cat_1, Skunk_1, Unicorn_1, Dragon_1, Dog_2, Cat_2, Skunk_2, Unicorn_2, Dragon_2]
    for animal in zoo_lst:
        if animal.is_hungry():
            print(animal.type ,animal.get_name())
            while animal.is_hungry():
                animal.feed()
            else:
                print(animal.talk())
                if isinstance(animal, mammal):
                    if animal.type == 'Dog':
                        animal.fetch_stick()
                    elif animal.type == 'Cat':
                        animal.chase_laser()
                    else:
                        animal.stink()
                else:
                    if animal.type == 'Unicorn':
                        animal.sing()
                    else:
                        animal.breath_fire()
        else:
            continue
    print(Dragon_2.zoo)

main()
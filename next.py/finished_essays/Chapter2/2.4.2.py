# Define a class called BigThing which receives as a parameter during creation a variable of a certain type (can be anything: string, list, number, etc.).

# Add a method called size to the class that works as follows:

# If the variable is a number - the method returns the number
# If the variable is a list/dictionary/string - the method returns the length of the variable (len).
# Below is a sample run:

# my_thing = BigThing("balloon")
# print(my_thing.size())
# 7
# Define another class called BigCat which inherits from the BigThing class and also receives a weight during creation:

# If the weight is greater than 15, the size method will return "Fat"
# If the weight is greater than 20, the size method will return "Very Fat"
# Otherwise, the method returns OK.
# Below is a sample run:

# cutie = BigCat("mitzy", 22)
# print(cutie.size())
# Very Fat

# My solution
class BigThing:
    def __init__(self,type) -> None:
        self._type= type
    def size(self):
        if isinstance(self._type, int):
            return self._type
        else:
            return len(self._type)

class BigCat(BigThing):
    def __init__(self, type, weight) -> None:
        super().__init__(type)
        self._weight= weight
    def size(self):
        if self._weight>15:
            if self._weight>20:
                return "Very Fat"
            else:
                return "Fat"
        else:
            return "OK"

my_thing = BigThing("balloon")
print(my_thing.size())

cutie = BigCat("mitzy", 22)
print(cutie.size())
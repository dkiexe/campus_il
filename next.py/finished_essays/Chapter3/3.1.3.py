# In this unit we learned about the hierarchy tree of exceptions. Now we will consciously try to write code that will throw exceptions of various types.

# Write eight functions, each of which will throw a different exception, from the following exceptions:
# StopIteration
# ZeroDivisionError
# AssertionError
# ImportError
# KeyError
# SyntaxError
# IndentationError
# TypeError
# Call each of the functions you wrote and check that the expected exception was indeed thrown.

# My solution
def StopIteration_err():
    raise StopIteration('')
def ZeroDivisionErr():
    x= 5/0 
def AssertionErr():
    assert 1==3, "not equal"
def import_err():
    raise ImportError('NOPE!')
def KeyError_():
    raise KeyError('key_error')
def Syntax():
    raise SyntaxError('syntax error')
def IndentationError_():
    raise IndentationError('unexpected indent')
def TypeError_():
    raise TypeError('type err')
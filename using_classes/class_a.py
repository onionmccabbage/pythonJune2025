# Here we will write a class for a 'Person'
# Name will be validated as a non-empty string
# Age will be validated as a positive number

# There are three ideas we need to grasp:
# property decorators
# mangled property names
# __slots__

class Person:
    # note: all functions within a class take 'self' as a property
    def __init__(self, name, age): # we may choose to pass in any proerties
        self.name = name # this line actually calls teh name setter function
        self.age  = age
    @property # the accessor or getter function
    def name(self):
    # using __ creates a 'mangled' name 
    # which cannot be easily accessed outside the class
        return self.__name 
    @name.setter # the mutator or setter function
    def name(self, new_name):
        # validate it is a string but not an empty string
        if type(new_name) == str and new_name != '':
            self.__name = new_name # accept the new value
        else:
            raise TypeError # raise an exception

# question: how is garbage collection managed in Python

if __name__ == '__main__':
    gert = Person('Gertrude', 52) # here we create an instance of our class
    fred = Person('Freda', 42)
    # we may assign any arbitrary data to this instance
    # gert.name = 'Gertrude'
    # gert.age = -52
    print(f'{gert.name} is aged {gert.age}')

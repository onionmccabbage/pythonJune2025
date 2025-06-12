# Here we will write a class for a 'Person'
# Name will be validated as a non-empty string
# Age will be validated as a positive number

# There are three ideas we need to grasp:
# property decorators
# mangled property names
# __slots__

class Person:
    # if we wish we may restrict the mangled properties that are permitted
    __slots__ = ['__name', '__age']
    # note: all functions within a class take 'self' as a property
    def __init__(self, name, age): # we may choose to pass in any proerties
        self.name = name # this line actually calls the name setter function
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
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, new_age):
        # validate age to be a positive number
        if type(new_age) in (int, float) and new_age >=0:
            self.__age = new_age
        else:
            self.__age = 32 # we choose to set a sensible default
    def aniversary(self):
        '''call this method when someones age increases by one'''
        self.__age += 1
    def __str__(self):
        return f'{self.name} is {self.age} years old'
# question: how is garbage collection managed in Python

if __name__ == '__main__':
    gert = Person('Gertrude', 52) # here we create an instance of our class
    gert.aniversary() # call the method of the class
    fred = Person('Freda', -99)
    # we may assign any arbitrary data to this instance
    # One reason for writing setter methods is to validate changes to our data
    gert.name = 'Gerty' # mutate the value by calling the nae setter function
    # gert.__name = 'oops' # this does NOT alter the mutate property within the class
    # gert.age = -52
    print(f'{gert.name} is aged {gert.age}') # here we call teh getter functions to access the data
    print(f'{fred.name} is aged {fred.age}')
    # make use of the __str__ method
    print(fred, gert)

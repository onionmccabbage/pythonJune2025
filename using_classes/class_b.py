# we need a class to encapsulate data related to a photo

class Photo(): # we may choose to include ()
    '''Every Photo will have 
    - a positive integer id 
    - a non-empty string title'''
    def __init__(self, id, title):
        self.id    = id    # remember - this will invoke the function to validate id
        self.title = title
    @property
    def id(self):
        return self.__id # __id is the mangled name
    @id.setter
    def id(self, new_id):
        if type(new_id)==int and new_id >=0:
            self.__id = new_id
        else:
            raise TypeError('ID must be a positive integer')
    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, new_title):
        if type(new_title)==str and new_title != '':
            self.__title= new_title
        else:
            raise TypeError('title must be a non-empty string')

# extend our snapshot class, examine Python inheritance chains, see __str__ method     

# class inheritance. If we wish we can use one class to build another class
class Snapshot(Photo):
    '''Snapshot inherits everything from the Photo class
    We can then add our own additional features
    - flash indicator True or False'''
    def __init__(self, id, title, flash): # __init__ is called every time we make an instance
        super().__init__(id, title)
        self.flash = flash
    @property
    def flash(self):
        return self.__flash
    @flash.setter
    def flash(self, new_flash):
        # validateh flash is a boolean (True or False)
        if type(new_flash) == bool:
            self.__flash = new_flash
        else:
            raise TypeError('Flash must be boolean True or False')
    def __str__(self):
        '''__str__ will override the default 'print' mechanism'''
        return f'{self.title} has id {self.id} flash: {self.flash}'
        
if __name__ == '__main__':
    p1 = Photo(2, 'view of Genoa')
    # p2 = Photo(-2, 'view of Galway Bay') # should throw a type error
    s1 = Snapshot(4, 'Beutiful Hemel', True) # remember -this calls the __init__ method
    print(s1) # this will use the __str__ method
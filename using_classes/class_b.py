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
        if type(new_id)==int and int >=0:
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

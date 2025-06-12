# We are often faced with data we need to handle
# Maybe we need to deal with information about a person
# we could use simple data storage
n = 'Gertrude'
a = 52
r = 'admin'
# or we can gather related data into a structure
gert = ['Gertrude', 52, 'admin'] # a list or a tuple
# alternatively we may use a dict
gert_dict = {'n':'Gertrude', 'age':52, 'role':'admin'}

# All the built in structures have one problem in common 
# They cannot validate their own contents
# we are left writing our own validation 

# One major reason to write a class is to enforce automatic validation on a data structure

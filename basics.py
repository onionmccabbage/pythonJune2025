# this is a comment. It is always a good idea to comment your code
# We always declare variables
a = 3    # an integer (whole number)
b = 7.2  # float (includes decimal part)
# there are also other data types
c = True # or False (boolean)
d = None # whenever we need to represent the absence of anything else

# we may print values like this
print(a, b, c, d)
print( type(a), type(b) )
# we can try to assign a value to a different data type
e = int(b) # store just the integer part of a floating point number
print(e, type(e))
# there is a data-type called 'string'
# string is an immutable ordinal collection of characters
# ordinal means in order: 0, 1, 2, 3, 4, etc.
#    0123456789........
s = 'here is some text'
# We can grab any member of an ordinal collection using 'slicing'
print( s[6] ) # 's'
print( s[2:9] ) # [start:stop-before]

# challenge....
h=s[0:4]
t=s[13:] # defaults to the end
print( f'{h} {t}' ) # we may inject variables into a formatted string using {}

# Quotation marks
x = 'we may use single quotes'
y = "or we may use double - (Python istelf does not care)"
# we often use the triple quortes for docstring (__doc__)
z = '''we can even use triple quotes
which alow new lines witbin a string'''
zz= """or triple double quotes 
- really Python does not care"""

# code structures
# for-loop, and conditions 'if'
# we use colon : to indicate the start of a code block
# for i in s: # the iterator is commonly called 'i' or '_'
for i in s[2:12:2]: # we can use slicing to start:stop-before:step through the collection
    print(i)
# the code block ends when we no longer indent the code

# there are two further collections in regular use in Python
# list and tuple
# a list is an ordinal mutable collection of any data type
l = [5,4,3,'hello', True, x, 8.23242] # the square brackets indicate we are dealing with a list
print(l, type(l))
# we may use slicing
print(l[3:6])
# we may alter the list (mutate the list)
l[0] = 99
l.append(-6.5)
l.insert(4, False)
print(l)

# tuple is the same as list except we may not mutate the members of the collection
# the round brackets indicate a tuple
t = (6,5,4,2,55.5, x, l, True) # an immutable ordinal collection of any data type
print( t, type(t), t[3:6] )

# we may iterate over any ordinal collection
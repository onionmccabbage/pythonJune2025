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

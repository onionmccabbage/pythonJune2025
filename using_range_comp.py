# Python range and comprehension are useful features

# we may generate a range of values using start, stop-before, step like this

r = range(-1000, 1001, 3) # this is a range object
print(r, type(r))

# in this case, all the data members must exist in memory
for i in (-10, -7, -5, -1, 2, 5, 8):
    print(i)

# here, only the range object exists in memory - the values are generated as needed
for i in r:
    print(i/1000) # range can only take numeric values

def test(x):
    if x<5:
        return x
    else:
        return 5

# Comprehension is a related concept
s = range(0,11) # numers 0-10
squares = (i*i for i in s) # as with a range, the calculated values do NOT exist in memory
wow     = (test(i) for i in s) # we may call a function within the generator
print(type(squares)) # we have a generator
cubes   = [i**3 for i in range(0,100)] # square brackets will populate a list im memory
print(cubes, type(cubes))

for i in squares:
    print(i)


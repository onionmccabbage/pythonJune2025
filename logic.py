# Every file containing Python code is known as a module
# we may ask the user to enter a value
# CAREFUL - input ALWAYS returns a string
u = input('Please enter a number: ')
print(u, type(u))
# we may choose to convert the string to a number
n = int(float(u))
print(n, type(n))
# Python offers many mathermatical operators
# + - / *     obvious
# ** raise to a power
# // integer division
# %  remainder division
p = n**2 # raie eto power 2
d = n//2 # modulo division
r = n%2  # remainder after division
print(p,d, r)
# we may use == to compare values
if n == 2:
    print('you entered two')
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
r=n%2  # remainder after division
print(p, d, r)
# we may use == to compare values
if n == 2:
    print('you entered two')
elif n>10:
    print(f'{n} is bigger than ten')
elif n<0:
    print(f'{n} is a negative number')
else:
    print('Some other value was entered')

# using logical operators including and or in
primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
if n in primes:
    print(f'{n} is a prime number between 0 and 100')

# using and/or
# challenge is it both an odd number AND a prime number
if n//2 != n/2 and n in primes:
    print(f'{n} is an odd prime number')

# we also have <= and >=
# we may use or...
if n==5 or n==-5:
    print('FIVE!!!')
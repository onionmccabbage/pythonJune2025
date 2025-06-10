# we can collect code into functions for re-use
def checkOddEven(n): # we define a function, optionally pass in arguments
    '''This function will return the word 'odd' or 'even' 
    based on the number n. If n is not a number, return 'NaN' '''
    if type(n)==int or type(n)==float:
        '''we know this is a number'''
        if n//2 == n/2: # even number
            return 'Even'
        else:
            return 'Odd'
    else:
        return 'NaN' # functions do have to return anything but you may
    
# we may exercise the code
print( checkOddEven(4) )   # Even
print( checkOddEven(3) )   # Odd
print( checkOddEven('4') ) # NaN


# another function: validate user input as an integer
def checkInt(): # we may choose to take no arguments intp the function
    '''ask the user to enter a value (which will be a string)
    If the value can be cast as an integer, return the integer.
    Otherwise, return zero'''
    u = input('Please enter an integer: ')
    if u.isnumeric(): # isnumeric checks to see if the string contains ONLY digits (not . etc)
        i = int(u)
        return i
    else:
        return 0
    
# exercise the code
result = checkInt()
print( result )
    

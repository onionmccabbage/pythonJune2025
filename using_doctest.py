# we may need to write simple tests for our code
import doctest

def showPowers(n):
    '''return the square and cube of n
    >>> showPowers(5)
    [25, 125]
    >>> showPowers(3)
    [9, 27]
    '''
    s = n**2
    c = n**3
    result = [s, c]
    return result

if __name__ == '__main__':
    doctest.testmod(verbose=True)
    # r = showPowers(5)
    # print(r) # [25, 125]
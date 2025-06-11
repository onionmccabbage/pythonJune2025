# we will import our util file

import util

def doStuff():
    '''the main application'''
    result = util.simple(5,6)
    return result

# when we run a module directly, Python will assign __name__ to '__main__'
if __name__ == '__main__':
    print(__name__) # __main__
    r = doStuff()
    print(r) # 11
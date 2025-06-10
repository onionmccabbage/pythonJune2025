# this might be the main application. We can import our own modules
from using_func import checkInt
# we may import modules from package
# i.e. import files from a folder
from utility.maths import addThem

def stateTemperature():
    '''ask user for int then write as a temperature'''
    t = checkInt()
    return f'The temperature is {t} degrees'

if __name__ == '__main__':
    s = stateTemperature()
    print(s)
    # use our imported function
    n = addThem(3,4)
    print(n) # 7
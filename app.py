# this might be the main application. We can import our own modules
from using_func import checkInt

def stateTemperature():
    '''ask user for int then write as a temperature'''
    t = checkInt()
    return f'The temperature is {t} degrees'

if __name__ == '__main__':
    stateTemperature()
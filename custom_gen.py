import datetime
import time

# range, comprehension, generator and yield

r = range(0,10)

# a generator object
temperatures = (f'{i}C' for i in range(-70, 91))

for _ in temperatures:
    print(_)

# we may need to create our own custom generator do yield up valies we may need
def makeDateTimeStamp():
    '''Generate a date-time stamp as a nicely formatted string'''
    while True: # this nmeans continue endlessly - a never ending loop
        now = datetime.datetime.now()
        date_string = now.strftime('%d-%m-%Y %H:%M:%S')
        yield date_string # any function which implements 'yield' becomes a generator


if __name__ == '__main__':
    # we need an instance of our custom generator
    ts = makeDateTimeStamp()
    print(type(ts)) # generator
    # we can always access the next available member from a generator using __next__()
    print( ts.__next__() )
    time.sleep(5) # the machine will wait for 5 seconds
    print( ts.__next__() )
    time.sleep(5)
    print( ts.__next__() )

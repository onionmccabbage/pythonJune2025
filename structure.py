# we may choose to make use of other modules
import random # random is one of many modules in the Python Standard library

r = random.randint(0,10) # a random number between 0 and 10 inclusive

# we might want a never-ending routine
while True: # this is often called a 'run-loop' - where we need to run endlessly
    '''the while operator lets us specify a condition for the loop'''
    g = input('Guess the number: ')
    g_int = int(float(g))
    if g_int == r:
        print(f'You guessed {r} corretly')
        break # this will break out of our endless loop
    else:
        print('Nope...')
        # continue

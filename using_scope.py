# Everything that is not inside a code block is in the 'global' scope

g = 'this is in the global scope'

def fn():
    # we may choose to bnring a global scope variable into a local function
    global g # now any reference ot g within this scope will acces the global variable
    g = 'this is within a local scope (i.e. a code block)'
    print(g) # this will print the local version of g

if __name__ == '__main__':
    print(g)
    fn()
    print(g)


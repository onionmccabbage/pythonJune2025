# we may choose any Python data structure to store data
# Sometimes we need to collect data values together into a structure (pack)
# Other times we need to pick out the individual members of a structure (unpack)

def packData(a, b, c):
    '''combine the separate arguments a b and c into a single list'''
    s = [a, b, c]
    return s

def unpackData(struct):
    '''separate the structure into three parts
    (NB we assume there are three parts in this structure!!)'''
    a, b, c = struct
    return f'we have {a} {b} and {c}'

if __name__ == '__main__':
    r = packData(32, 'ok', True)
    print(r, type(r))
    s = unpackData(r)
    print(s)
    # we may also unpack a tuple
    t = (45, 'problem', False)
    s = unpackData(t)
    print(s)


# we may read a text file using a file access object

def readFileData():
    '''Use a file access object to read ext back from a persistent local file'''
    fin = open('my_log.txt', 'r') # 'r' will read from the file. Default is text
    with fin:
        retrieved = fin.read() # read the entire file
    return retrieved

if __name__ == '__main__':
    r = readFileData()
    print(r, type(r))
# we may read a text file using a file access object

def readFileData():
    '''Use a file access object to read ext back from a persistent local file'''
    fin = open('my_log.txt', 'r') # 'r' will read from the file. Default is text
    with fin: # the 'with' operation will close the file when we are done
        # retrieved = fin.read() # read the entire file
        # retrieved = fin.readline() # read just one line from the file
        retrieved = fin.readlines() # read all lines into a list of strings
    return retrieved

if __name__ == '__main__':
    r = readFileData()
    print(r, type(r))
# we may choose to output our print to a persistent text file

def printOutput(s):
    '''Persist the incoming sting of text into a text file
    we will append to file with each new piece of text'''
    # we need a file access object
    # NB we may use a relative path or an absolute path
    fout = open('my_log.txt', 'at') # 'a' will append to the file 't' is for text
    # every time we use 'print' it defaults to adding a new line at the end
    print(s, file=fout) # send the print output to our file access object

if __name__ == '__main__':
    string = 'Here is some text'
    printOutput(string)
# we may choose to be a bit nmore in control, and use write rather than print


def writeOutput(s):
    '''Create a file acess object and use it to write our text into a persistent file'''
    # we need a file access object
    fout = open('my_log.txt', 'at')
    # with fout: # with will close the file access when done (saves us remembering to do it)
    #     # write does NOT add a new-line character
    #     fout.write(s)
    #     # writelines will write every member of an iterable collection
    #     fout.writelines(s) # we send the entire text o the file access object
    #     # we MAY choose to add a new line
    #     fout.write('\n') # we encode the new line with \n
    # old way
    fout.write(f'{s}\n') # or writelines
    fout.close() # we need to remember ot close the file access object

if __name__ == '__main__':
    t = 'something useful we need to remember.'
    writeOutput(t)
    l = ['eeny', 'meeny', 'miny', 'moe']
    writeOutput(l)
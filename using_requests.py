# the requests library lets us access API data over HTTP(s)
# NB we may need to pip install requests
import requests #  this can retrieve JSON, xml, text, html.....
import sys # this gives us acess to the system on which Python is running

# we aim to use exception handling around any input or output (i/o)


# if we choose to, we can provide sensible defaults for function arguments
def getData(n=1): # whichever value is passed in will be 'n'
    '''use the requests library to make a call to an API end-point
    When the JSON data is retrieved, show it in the console'''
    try:
        # first make a request to an API end-point
        response = requests.get(f'https://jsonplaceholder.typicode.com/users/{n}')
        # next we grab the data from the response
        data = response.json() # this will extract any JSON from the response object
        return data # NB the requests library will automatically convert the JSON into a Python structure
    except Exception as err:
        return f'Problem: {err}'

def prettyData(struct):
    '''receive a 'user' dictionary and create a pretty string to print
    we will pick out name, city, phone and website'''
    n = struct['name']
    c = struct['address']['city'] # access the city within the address
    p = struct['phone']
    w = struct['website']
    result = f'{n} lives in {c} contact: {p} {w}'
    return result

def askUser():
    '''ask the user for which ID
    or use a system argument'''
    if len(sys.argv) > 1:
        id = int(float(sys.argv[1])) # all system argument variables are strings
    else:
        id_str = input('Which user? ')
        if id_str.isnumeric(): # check it is a number
            id = int(float(id_str))
        else:
            id=1 # choose a sensible default
    return id

if __name__ == '__main__':
    # we may exercise our code here
    whichUser = askUser() # CAREFUL - there will rarely be a user sitting at a terminal to type anything!!!!
    d = getData(whichUser) # here we pass 1 as an argument
    p = prettyData(d) # pass the entire structure into the function
    print(p)
    print(d, type(d))
# the requests library lets us access API data over HTTP(s)
# NB we may need to pip install requests
import requests #  this can retrieve JSON, xml, text, html.....

def getData(n): # whichever value is passed in will be 'n'
    '''use the requests library to make a call to an API end-point
    When the JSON data is retrieved, show it in the console'''
    # first make a request to an API end-point
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{n}')
    # next we grab the data from the response
    data = response.json() # this will extract any JSON from the response object
    return data # NB the requests library will automatically convert the JSON into a Python structure

def askUser():
    pass

if __name__ == '__main__':
    # we may exercise our code here
    d = getData(1) # here we pass 1 as an argument
    print(d, type(d))
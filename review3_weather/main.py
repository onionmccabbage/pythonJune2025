from weather import Weather
import requests
from datetime import datetime

def getWeather(city='Athlone'):
    key='48f2d5e18b0d2bc50519b58cce6409f1'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={key}'
    try:
        resp = requests.get(url)
        resp_dict = resp.json()
        return resp_dict
    except Exception as err:
        print(err)

def buildWeatherInstance(city='Athlone'):
    weather_dict = getWeather(city)
    desc = weather_dict['weather'][0]['description']
    temp = weather_dict['main']['temp']
    weather_report = Weather(city, desc, temp)
    return weather_report
    
def writeWeatherfile(w):
    # get a date-stamp
    dt = datetime.today()
    # write the weather instance to a text file
    fout = open('weather.txt', 'at') # append text
    with fout:
        fout.write(f'On {dt} ') 
        print(w, file=fout)

if __name__ == '__main__':
    w = buildWeatherInstance()
    print(w)
    writeWeatherfile(w)


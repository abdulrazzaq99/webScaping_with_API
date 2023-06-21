
import requests

def getWeather(location):
     url = f"http://api.weatherapi.com/v1/current.json?key=49d241bc242143edb28183223232006&q={location}&aqi=yes"
     response = requests.get(url)
     data = response.json()  #As the data from web is in JSON
     City=data['location']['name']
     temprature=data['current']['temp_c']
     forecast={'City':City,'temperature':temprature}
     return forecast




i=True
while i==True:
    location=input("Enter the location")
    print(getWeather(location))
    continueVariable=input("do you want to continue?[Y/N]")
    if continueVariable=='Y':
         i=True
    elif continueVariable=='N':
         i=False
    else:
         break

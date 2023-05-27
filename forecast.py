import requests
from .config import * 

def forecast(city):
    #TODO: if the spelling of city is wrong, identify the nearest city using difflib 
    # and ask the user if he/she meant that city
    url= f'api.openweathermap.org/data/2.5/weather?q={city},uk&APPID={TOKEN}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()  # Assuming the API response is in JSON format
        return data
    except requests.exceptions.HTTPError as e:
        print('Error: ' + str(e)) # Response code error



print("Enter the city name for weather forecasting: ")
city = input()
temp= forecast(city)
print("The temperature in ",city," is ",temp," degree celsius")


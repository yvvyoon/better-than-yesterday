import os
import requests
import json

from dotenv import load_dotenv

import location_getter

load_dotenv(verbose=True)

API_KEY = os.getenv('WEATHER_API_KEY')
API_URL = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&APPID={API_KEY}&units=metric'

latitude = location_getter.get_coordinate()[0]
longitude = location_getter.get_coordinate()[1]


def get_weather_data():
    api_call_result = requests.get(url=API_URL)
    weather_data = json.loads(api_call_result.text)

    temperature = weather_data['main']['temp']
    sensible_temperature = weather_data['main']['feels_like']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    measurement_datetime = weather_data['timezone']

    print(temperature)
    print(sensible_temperature)
    print(humidity)
    print(wind_speed)
    print(measurement_datetime)

    return weather_data

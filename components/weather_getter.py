import os
import requests
import json

from dotenv import load_dotenv

import location_getter

load_dotenv(verbose=True)

latitude = location_getter.latitude
longitude = location_getter.longitude

API_KEY = os.getenv('WEATHER_API_KEY')
API_URL = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&APPID={API_KEY}&units=metric'

api_call_result = requests.get(url=API_URL)
weather_data = json.loads(api_call_result.text)

print(weather_data)

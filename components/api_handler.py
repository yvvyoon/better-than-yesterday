import os
import requests
from dotenv import load_dotenv

load_dotenv(verbose=True)

API_KEY = os.getenv('WEATHER_APP_KEY')
API_URL = f'http://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&APPID=${API_KEY}&units=metric'

requests.get()

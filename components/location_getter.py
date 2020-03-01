import os
import requests
import json

from dotenv import load_dotenv

load_dotenv(verbose=True)

API_KEY = os.getenv('LOCATION_API_KEY')
API_URL = f'https://www.googleapis.com/geolocation/v1/geolocate?key={API_KEY}'

request_data = {
    'considerIp': True,
}

api_call_result = requests.post(url=API_URL, data=request_data)
location_data = json.loads(api_call_result.text)
latitude = location_data['location']['lat']
longitude = location_data['location']['lng']

# print(latitude, longitude)

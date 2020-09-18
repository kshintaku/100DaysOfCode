'''
RESULTS FROM WEATHER QUERY
{'coord': {'lon': -118.31, 'lat': 33.89}, 'weather': [{'id': 711, 'main': 'Smoke', 'description': 'smoke', 'icon': '50n'}], 'base': 'stations', 'main': {'temp': 71.04, 'feels_like': 68.5, 'temp_min': 66.99, 'temp_max': 77, 'pressure': 1012, 'humidity': 64}, 'visibility': 10000, 'wind': {'speed': 9.17, 'deg': 280}, 'clouds': {'all': 1}, 'dt': 1600397893, 'sys': {'type': 1, 'id': 4361, 'country': 'US', 'sunrise': 1600349900, 'sunset': 1600394211}, 'timezone': -25200, 'id': 5351549, 'name': 'Gardena', 'cod': 200}
'''

import config
import requests
import json

weather_url = 'https://api.openweathermap.org/data/2.5/'

api_type = ['weather?', 'onecall?']
api_picker = 1

lat, lon = 33.840763, -118.345413

city = ['Gardena', 'Torrance']
units = ['standard', 'metric', 'imperial']


if api_picker == 0:
  request_url = weather_url + api_type[api_picker] + 'q=' + city[0] + '&appid=' + config.OPEN_WEATHER_API + '&units=' + units[2]
elif api_picker == 1:
  request_url = weather_url + api_type[api_picker] + 'lat=' + str(lat) + '&lon=' + str(lon) + '&appid=' + config.OPEN_WEATHER_API

weather_data = requests.get(request_url).json()
print(weather_data)
import config
import requests
# import json

weather_url = "https://api.openweathermap.org/data/2.5/"

api_type = ["weather?", "onecall?"]
api_picker = 1

lat, lon = 33.840763, -118.345413

city = ["Gardena", "Torrance"]
units = ["standard", "metric", "imperial"]


if api_picker == 0:
    request_url = (
        weather_url
        + api_type[api_picker]
        + "q="
        + city[0]
        + "&appid="
        + config.OPEN_WEATHER_API
        + "&units="
        + units[2]
    )
elif api_picker == 1:
    request_url = (
        weather_url
        + api_type[api_picker]
        + "lat="
        + str(lat)
        + "&lon="
        + str(lon)
        + "&appid="
        + config.OPEN_WEATHER_API
    )

weather_data = requests.get(request_url).json()
print(weather_data)

import requests
import json


#url = "https://api.openweathermap.org/data/3.0/onecall?lat=59.33&lon=18.06&units=metric&exclude=current,minutely,daily,alerts&appid=INSERTKEY}"
response = requests.get(url)

data = response.json()

with open("Weather_data.json", "w") as outfile:
    json.dump(data, outfile)

import json
import pandas as pd

# reading the database
data = pd.read_json("Weather_data.json", orient="columns")

timestamps = []
temperatures = []
air_pressure = []
precipitation = []

for hourly_data in data["hourly"].apply(pd.Series).iterrows():
    timestamps.append(hourly_data[1]["dt"])
    temperatures.append(hourly_data[1]["temp"])
    air_pressure.append(hourly_data[1]["pressure"])
    precipitation.append(hourly_data[1]["pop"])


weather_dict = {"date-time": timestamps,
                "temp": temperatures,
                "pressure": air_pressure,
                "precipitation": precipitation}

# converting dictionary to JSON
weather_json = json.dumps(weather_dict)

# writing JSON to file
with open("Refined_data.json", "w") as f:
    f.write(weather_json)
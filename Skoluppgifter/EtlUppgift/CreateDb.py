import sqlite3
import pandas as pd
import datetime

data = pd.read_json("Refined_data.json", orient="columns")

time = data["date-time"]
temp = data["temp"]
air = data["pressure"]
rain = data["precipitation"]


dates = []

for timestamp in time:
    date = datetime.datetime.fromtimestamp(timestamp)
    dates.append(date)



# creating a connection object
conn = sqlite3.connect('weather.db')

# creating a cursor object
cursor = conn.cursor()

# creating a table
cursor.execute('''CREATE TABLE weather
                (date text, temperature real, air real, precipitation real)''')

# inserting data into the table
for i in range(len(dates)):
    cursor.execute("INSERT INTO weather VALUES (?, ?, ?, ?)", (dates[i], temp[i], air[i], rain[i]))

# commiting the changes
conn.commit()

# closing the connection
conn.close()

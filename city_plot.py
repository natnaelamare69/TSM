import matplotlib.pyplot as plt 
import numpy as np
import json
import os

with open("city_list.json", "r") as data:
    fromjson = json.load(data)

fromjson = json.load(data)
cities = fromjson["cities"]

lats = [float(city[1]) for city in cities]
longs = [float(city[2]) for city in cities]
names = [city[0] for city in cities]

#normalizing 
min_lat, max_lat = min(lats), max(lats)
min_lon, max_lon = min(longs), max(longs)

norm_lats = [(lat - min_lat) / (max_lat - min_lat) for lat in lats]
norm_longs = [(lon - min_lon) / (max_lon - min_lon) for lon in longs]


plt.figure(figsize=(10, 10))
for i, name in enumerate(names):
    plt.text(norm_longs[i], norm_lats[i], name, fontsize=7)

plt.scatter(norm_longs, norm_lats, color='red')
plt.title("travelling sales man probelem: ethiopian cities")
plt.show()

data.close()
import math
import numpy as np
import os
import json

with open("city_list.json", "r") as data:
    fromjson = json.load(data)
#load and populate from json
cities = fromjson["cities"]

#first element contains city names in the first json
city_names = [city[0] for city in cities]
coordinates = [(float(city[1]), float(city[2] )) for city in cities]
               #lat                long

#this calculates c**2                
def calculator(p1, p2):
    x1, y1 = p1 
    x2, y2 = p2 
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def euclidean_distance(coords): 
    n = len(coords)
    matrix = np.zeros((n, n)) #np(numpy) initalizing an array of the size coords(list of cities(70)) with 0 (u cant declare an empty array, matrix is a 2D array)

    #calculate the distance from each city from eachother 
    for i in range(n):
        for j in range(n):
            if i!=j: 
                matrix[i][j] = calculator(coords[i], coords[j])
    return matrix
#array tha holds the distance between two cities 
distance_matrix = euclidean_distance(coordinates)

# a dictionary (key, value)
distance_dict = {}
for i, city_from in enumerate(city_names): #city from contains i 
    distance_dict[city_from] = {}       # populating the dictonary with the city from name 
    for j, city_to in enumerate(city_names):    #city to contains the value of j
        if i != j:
            distance_dict[city_from][city_to] = distance_matrix[i][j]

with open("city_distance.json", "w") as f: 
    json.dump(distance_dict, f, indent=4)
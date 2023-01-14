import math as m
from numpy import array

coord1 = array([
    lat:=float(input("latitude_1: ")),
    lon:=float(input("longitude_1: ")),
    alt:=float(input("altitude_1: "))
])
coord2 = array([
    lat:=float(input("latitude_2: ")),
    lon:=float(input("longitude_2: ")),
    alt:=float(input("altitude_2: "))
])

print("Coordinate 1:\n",coord1)
print("Coordinate 2:\n",coord2)

def hav(lat1, lat2, lon1, lon2):
    RAD = 6335.439
    return 2*RAD*m.asin(m.sqrt((m.sin((lat2-lat1)/2)**2)+m.cos(lat1)*m.cos(lat2)*(m.sin((lon2-lon1)/2)**2)))

def dist(coor1, coor2):
    lat1, lon1, alt1 = coord1
    lat2, lon2, alt2 = coord2
    deg_diff = hav(lat1, lat2, lon1, lon2)
    r_diff = abs(lat1 - lat2)
    return m.sqrt(deg_diff**2 + r_diff**2)

distance = dist(coord1, coord2)
print("Distance between the two coordinates is: ", distance)
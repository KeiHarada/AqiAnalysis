def temp_range(data):
    data = float(data)
    if data > -60 and data < 60:
        return True
    else:
        return False

def hum_range(data):
    data = float(data)
    if data > -0.1 and data < 100.1:
        return True
    else:
        return False

def rain_range(data):
    data = float(data)
    if data > -0.1 and data < 100.1:
        return True
    else:
        return False

def apr_range(data):
    data = float(data)
    if data > -0.1 and data < 2000:
        return True
    else:
        return False

def wspd_range(data):
    data = float(data)
    if data > -0.1 and data < 100:
        return True
    else:
        return False

def prepro(temp):

    temp = str(temp)

    if temp == "NULL":
        return "9999.0"

    if temp[0] == ".":
        return "0" + temp

    if temp[0] == "-":
        if temp[1] == ".":
            return "{0}{1}{2}".format(temp[0:1], "0", temp[1:])

    return temp

def colorSelect(aqi):

    if aqi == "NULL":
        return "lightgrey"

    aqi = float(aqi)

    if aqi >= 0 and aqi < 50:
        return "green"
    if aqi >= 50 and aqi < 100:
        return "yellow"
    if aqi >= 100 and aqi < 150:
        return "orange"
    if aqi >= 150 and aqi < 200:
        return "red"
    if aqi >= 200 and aqi < 300:
        return "purple"
    if aqi >= 300:
        return "maroon"

def status(color):

    if color == "green":
        return "good"
    if color == "yellow":
        return "moderate"
    if color == "orange":
        return "unhealthy for sensitive group"
    if color == "red":
        return "unhealthy"
    if color == "purple":
        return "very unhealty"
    if color == "maroon":
        return "hazardous"

import math

R = 6378.137 #[m]
P = 6356.752314 #[m]

def dist_point(l1, l2):
    lat1, lon1 = l1
    lat2, lon2 = l2

    lat1, lon1 = deg2km(lat1, lon1)
    lat2, lon2 = deg2km(lat2, lon2)

    lat = abs(lat1 - lat2)
    lon = abs(lon1 - lon2)

    return math.sqrt(lat * lat + lon * lon)

def deg2km(lat_deg, lon_deg):

    # latitude
    kmParLat = (2 * math.pi * P) / 360
    lat_km = lat_deg * kmParLat

    # longitude
    r = R * math.cos(math.radians(lat_deg))
    kmParLon = (2 * math.pi * r) / 360
    lon_km = lon_deg * kmParLon

    return (lat_km, lon_km)

def km2deg(lat_km, lon_km):

    # latitude
    latParKm = 360 / (2 * math.pi * P)
    lat_deg = lat_km * latParKm

    # longitude
    r = R * math.cos(math.radians(lat_deg))
    lonParKm = 360 / (2 * math.pi * r)
    lon_deg = lon_km * lonParKm

    return (lat_deg, lon_deg)
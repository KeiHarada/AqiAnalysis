# using: utf-8

import matplotlib.pyplot as plt
import datetime as dt

begin = dt.datetime(2017, 9, 1, 00)
end = dt.datetime(2017, 11, 30, 23)

def colorSelect(aqi):

    if aqi == "NaN":
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

def getHist():
    infile = open("infile/full_time.csv", "r").readlines()
    plt.title("9 - 11")

    cls = {"green": 0,
           "yellow": 0,
           "orange": 0,
           "red": 0,
           "purple": 0,
           "maroon": 0}

    for line in infile:

        if line[0] == "#":
            continue

        data = line[:-1].split("\t")
        time = dt.datetime.strptime(data[1], "%Y-%m-%d %H:%M:%S")

        if time < begin:
            continue
        if time > end:
            break

        color = colorSelect(data[2])
        cls[color] += 1

    mx = max(list(cls.values()))
    tmp = list(map(lambda x: x/mx, list(cls.values())))
    plt.bar(list(cls.keys()), tmp)
    plt.xticks(rotation=-90)
    plt.savefig("results/9-11/dev.png")
    plt.show()
# using:utf8
import matplotlib.pyplot as plt
import datetime as dt
from src import temporal as tp
from src import association as ass
from src import spatial as sp
from src import correlation

def correlation_(s_dict):
    begin = dt.datetime(2018, 4, 22, 20)
    end = dt.datetime(2018, 4, 22, 23)
    freq = 1 # hour

    time = begin
    while time <= end:
        plt.title(time)
        cls = {"green": list(),
               "yellow": list(),
               "orange": list(),
               "red": list(),
               "purple": list(),
               "maroon": list(),
               "lightgrey": list()}

        for item in list(s_dict.values()):
            cls[colorSelect(item["data"][timeFormat(time)])].append((item["location"][1], item["location"][0]))

        for color in list(cls.keys()):
            x = list(map(lambda p: p[0], cls[color]))
            y = list(map(lambda p: p[1], cls[color]))
            plt.scatter(x, y, c=color)

        plt.show()

        time = time + dt.timedelta(hours=freq)

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

def timeFormat(t):

    if type(t) == str:
        t = dt.datetime.strptime(t, '%Y-%m-%d %H:%M:%S')

    year = str(t.year)
    month = str(t.month)
    day = str(t.day)
    hour = str(t.hour)

    if len(month) == 1:
        month = "0" + month

    if len(day) == 1:
        day = "0" + day

    if len(hour) == 1:
        hour = "0" + hour

    return year[2:] + month + day + hour

def makedictionaly():
    location = open("infile/location.csv").readlines()

    s_dict = dict()
    for item in location:
        lid, lat, lon = item[:-1].split(",")
        s_dict[str(lid)] = {"location": (float(lat), float(lon)), "data": dict()}

    measurement = open("infile/aq.csv").readlines()

    for item in measurement:

        if item[0] == "#":
            continue

        lid, time, aqi, pm25, pm10, co, so2, no2, o3 = item[:-1].split(",")
        s_dict[str(lid)]["data"][timeFormat(time)] = aqi

    return s_dict

def histgram(s_dict):
    date = dt.datetime(2018, 4, 22, 14)

    x = list()
    for location in s_dict.keys():
        x.append(s_dict[location]["data"][timeFormat(date)])

    print(max(x), min(x))
    plt.hist(x, bins=6, density=True, rwidth=0.8, range=(0, 300))
    plt.show()

if __name__ == "__main__":

    #preprocessing()

    # spatial
    # sp.clustering()

    # temporal
    #s_dict = makedictionaly()
    #correlation(s_dict)
    #histgram(s_dict)

    # ass.temp2hum()
    # ass.temp2air()
    # ass.temp2rain()
    # ass.temp2wdsp()
    # ass.hum2air()
    # ass.hum2rain()
    # ass.hum2wdsp()
    # ass.air2rain()
    # ass.air2wdsp()
    # ass.rain2wdsp()

    #sp.locationList()
    #sp.cityList()
    #tp.getHist()


    #sp.mapplot()

    correlation.run()

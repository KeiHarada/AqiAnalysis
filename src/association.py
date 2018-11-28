# aqi.append(data[2])
# pm25.append(data[3])
# pm10.append(data[4])
# co.append(data[5])
# so2.append(data[6])
# no2.append(data[7])
# o3.append(data[8])
# temp.append(data[9])
# hum.append(data[10])
# air.append(data[11])
# rain.append(data[12])
# wdsp.append(data[13])

# using:utf-8
import matplotlib.pyplot as plt
import datetime as dt

begin = dt.datetime(2017, 12, 1, 00)
end = dt.datetime(2018, 2, 28, 23)

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

def temp2hum():
    infile = open("infile/full_time.csv", "r").readlines()
    plt.title("temp - hum")

    cls = {"green": list(),
           "yellow": list(),
           "orange": list(),
           "red": list(),
           "purple": list(),
           "maroon": list(),
           "lightgrey": list()}

    for line in infile:

        if line[0] == "#":
            continue

        data = line[:-1].split("\t")
        time = dt.datetime.strptime(data[1], "%Y-%m-%d %H:%M:%S")

        if time < begin:
            continue
        if time > end:
            break

        if float(data[9]) > 50.0:
            continue
        if float(data[10]) > 100.0:
            continue

        color = colorSelect(data[2])
        cls[color].append((float(data[9]), float(data[10])))

    for color in list(cls.keys()):
        x = list(map(lambda p: p[0], cls[color]))
        y = list(map(lambda p: p[1], cls[color]))
        plt.scatter(x, y, c=color, label=status(color), alpha=0.5)

    plt.xlim([-40, 40])
    plt.ylim([-10, 110])
    plt.legend()
    plt.savefig("results/temp2hum.png")
    plt.show()

def temp2air():
    infile = open("infile/full_time.csv", "r").readlines()
    plt.title("temp - air pressure")

    cls = {"green": list(),
           "yellow": list(),
           "orange": list(),
           "red": list(),
           "purple": list(),
           "maroon": list(),
           "lightgrey": list()}

    for line in infile:

        if line[0] == "#":
            continue

        data = line[:-1].split("\t")
        time = dt.datetime.strptime(data[1], "%Y-%m-%d %H:%M:%S")

        if time < begin:
            continue
        if time > end:
            break

        if float(data[9]) > 50.0:
            continue
        if float(data[11]) > 2000.0:
            continue

        color = colorSelect(data[2])
        cls[color].append((float(data[9]), float(data[11])))

    for color in list(cls.keys()):
        x = list(map(lambda p: p[0], cls[color]))
        y = list(map(lambda p: p[1], cls[color]))
        plt.scatter(x, y, c=color, label=status(color), alpha=0.5)

    plt.xlim([-40, 40])
    plt.ylim([-10, 1200])
    plt.legend()
    plt.savefig("results/temp2air.png")
    plt.show()

def temp2rain():
    infile = open("infile/full_time.csv", "r").readlines()
    plt.title("temp - rain fall")

    cls = {"green": list(),
           "yellow": list(),
           "orange": list(),
           "red": list(),
           "purple": list(),
           "maroon": list(),
           "lightgrey": list()}

    for line in infile:

        if line[0] == "#":
            continue

        data = line[:-1].split("\t")
        time = dt.datetime.strptime(data[1], "%Y-%m-%d %H:%M:%S")

        if time < begin:
            continue
        if time > end:
            break

        if float(data[9]) > 50.0:
            continue
        if float(data[12]) > 500.0:
            continue
        color = colorSelect(data[2])
        cls[color].append((float(data[9]), float(data[12])))

    for color in list(cls.keys()):
        x = list(map(lambda p: p[0], cls[color]))
        y = list(map(lambda p: p[1], cls[color]))
        plt.scatter(x, y, c=color, label=status(color), alpha=0.5)

    plt.xlim([-40, 40])
    plt.ylim([-10, 40])
    plt.legend()
    plt.savefig("results/tmp2rain.png")
    plt.show()

def temp2wdsp():
    infile = open("infile/full_time.csv", "r").readlines()
    plt.title("temp - wind speed")

    cls = {"green": list(),
           "yellow": list(),
           "orange": list(),
           "red": list(),
           "purple": list(),
           "maroon": list(),
           "lightgrey": list()}

    for line in infile:

        if line[0] == "#":
            continue

        data = line[:-1].split("\t")
        time = dt.datetime.strptime(data[1], "%Y-%m-%d %H:%M:%S")

        if time < begin:
            continue
        if time > end:
            break

        if float(data[9]) > 50.0:
            continue

        if float(data[13]) > 100.0:
            continue

        color = colorSelect(data[2])
        cls[color].append((float(data[9]), float(data[13])))

    for color in list(cls.keys()):
        x = list(map(lambda p: p[0], cls[color]))
        y = list(map(lambda p: p[1], cls[color]))
        plt.scatter(x, y, c=color, label=status(color), alpha=0.5)

    plt.xlim([-40, 40])
    plt.ylim([-10, 20])
    plt.legend()
    plt.savefig("results/temp2wdsp.png")
    plt.show()

def hum2air():
    infile = open("infile/full_time.csv", "r").readlines()
    plt.title("hum - air pressure")

    cls = {"green": list(),
           "yellow": list(),
           "orange": list(),
           "red": list(),
           "purple": list(),
           "maroon": list(),
           "lightgrey": list()}

    for line in infile:

        if line[0] == "#":
            continue

        data = line[:-1].split("\t")
        time = dt.datetime.strptime(data[1], "%Y-%m-%d %H:%M:%S")

        if time < begin:
            continue
        if time > end:
            break

        if float(data[10]) > 100.0:
            continue
        if float(data[11]) > 2000.0:
            continue

        color = colorSelect(data[2])
        cls[color].append((float(data[10]), float(data[11])))

    for color in list(cls.keys()):
        x = list(map(lambda p: p[0], cls[color]))
        y = list(map(lambda p: p[1], cls[color]))
        plt.scatter(x, y, c=color, label=status(color), alpha=0.5)

    plt.xlim([-10, 110])
    plt.ylim([-10, 1200])
    plt.legend()
    plt.savefig("results/hum2air.png")
    plt.show()

def hum2rain():
    infile = open("infile/full_time.csv", "r").readlines()
    plt.title("hum - rain fall")

    cls = {"green": list(),
           "yellow": list(),
           "orange": list(),
           "red": list(),
           "purple": list(),
           "maroon": list(),
           "lightgrey": list()}

    for line in infile:

        if line[0] == "#":
            continue

        data = line[:-1].split("\t")
        time = dt.datetime.strptime(data[1], "%Y-%m-%d %H:%M:%S")

        if time < begin:
            continue
        if time > end:
            break

        if float(data[10]) > 100.0:
            continue
        if float(data[12]) > 500.0:
            continue

        color = colorSelect(data[2])
        cls[color].append((float(data[10]), float(data[12])))

    for color in list(cls.keys()):
        x = list(map(lambda p: p[0], cls[color]))
        y = list(map(lambda p: p[1], cls[color]))
        plt.scatter(x, y, c=color, label=status(color), alpha=0.5)

    plt.xlim([-10, 110])
    plt.ylim([-10, 40])
    plt.legend()
    plt.savefig("results/hum2rain.png")
    plt.show()

def hum2wdsp():
    infile = open("infile/full_time.csv", "r").readlines()
    plt.title("hum - wind speed")

    cls = {"green": list(),
           "yellow": list(),
           "orange": list(),
           "red": list(),
           "purple": list(),
           "maroon": list(),
           "lightgrey": list()}

    for line in infile:

        if line[0] == "#":
            continue

        data = line[:-1].split("\t")
        time = dt.datetime.strptime(data[1], "%Y-%m-%d %H:%M:%S")

        if time < begin:
            continue
        if time > end:
            break

        if float(data[10]) > 100.0:
            continue
        if float(data[13]) > 100.0:
            continue

        color = colorSelect(data[2])
        cls[color].append((float(data[10]), float(data[13])))

    for color in list(cls.keys()):
        x = list(map(lambda p: p[0], cls[color]))
        y = list(map(lambda p: p[1], cls[color]))
        plt.scatter(x, y, c=color, label=status(color), alpha=0.5)

    plt.xlim([-10, 110])
    plt.ylim([-10, 20])
    plt.legend()
    plt.savefig("results/hum2wdsp.png")
    plt.show()

def air2rain():
    infile = open("infile/full_time.csv", "r").readlines()
    plt.title("air - rain fall")

    cls = {"green": list(),
           "yellow": list(),
           "orange": list(),
           "red": list(),
           "purple": list(),
           "maroon": list(),
           "lightgrey": list()}

    for line in infile:

        if line[0] == "#":
            continue

        data = line[:-1].split("\t")
        time = dt.datetime.strptime(data[1], "%Y-%m-%d %H:%M:%S")

        if time < begin:
            continue
        if time > end:
            break

        if float(data[11]) > 2000.0:
            continue
        if float(data[12]) > 500.0:
            continue

        color = colorSelect(data[2])
        cls[color].append((float(data[11]), float(data[12])))

    for color in list(cls.keys()):
        x = list(map(lambda p: p[0], cls[color]))
        y = list(map(lambda p: p[1], cls[color]))
        plt.scatter(x, y, c=color, label=status(color), alpha=0.5)

    plt.xlim([-10, 1200])
    plt.ylim([-10, 40])
    plt.legend()
    plt.savefig("results/air2rain.png")
    plt.show()

def air2wdsp():
    infile = open("infile/full_time.csv", "r").readlines()
    plt.title("air - wind speed")

    cls = {"green": list(),
           "yellow": list(),
           "orange": list(),
           "red": list(),
           "purple": list(),
           "maroon": list(),
           "lightgrey": list()}

    for line in infile:

        if line[0] == "#":
            continue

        data = line[:-1].split("\t")
        time = dt.datetime.strptime(data[1], "%Y-%m-%d %H:%M:%S")

        if time < begin:
            continue
        if time > end:
            break

        if float(data[11]) > 2000.0:
            continue
        if float(data[13]) > 100.0:
            continue

        color = colorSelect(data[2])
        cls[color].append((float(data[11]), float(data[13])))

    for color in list(cls.keys()):
        x = list(map(lambda p: p[0], cls[color]))
        y = list(map(lambda p: p[1], cls[color]))
        plt.scatter(x, y, c=color, label=status(color), alpha=0.5)

    plt.xlim([-10, 1200])
    plt.ylim([-10, 20])
    plt.legend()
    plt.savefig("results/air2wdsp.png")
    plt.show()

def rain2wdsp():
    infile = open("infile/full_time.csv", "r").readlines()
    plt.title("rain fall - wind speed")

    cls = {"green": list(),
           "yellow": list(),
           "orange": list(),
           "red": list(),
           "purple": list(),
           "maroon": list(),
           "lightgrey": list()}

    for line in infile:

        if line[0] == "#":
            continue

        data = line[:-1].split("\t")
        time = dt.datetime.strptime(data[1], "%Y-%m-%d %H:%M:%S")

        if time < begin:
            continue
        if time > end:
            break

        if float(data[12]) > 500.0:
            continue
        if float(data[13]) > 100.0:
            continue

        color = colorSelect(data[2])
        cls[color].append((float(data[12]), float(data[13])))

    for color in list(cls.keys()):
        x = list(map(lambda p: p[0], cls[color]))
        y = list(map(lambda p: p[1], cls[color]))
        plt.scatter(x, y, c=color, label=status(color), alpha=0.5)

    plt.ylim([-10, 40])
    plt.ylim([-10, 20])
    plt.legend()
    plt.savefig("results/rain2wdsp.png")
    plt.show()
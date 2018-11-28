# using:utf-8
import matplotlib.pyplot as plt
import datetime as dt
from src import myutil
import numpy as np
from pandas import *
from scipy.stats import gaussian_kde


def run():

    begin = dt.datetime(2016, 9, 1, 00)
    end = dt.datetime(2016, 9, 2, 00)

    aqi = dict()
    for line in open("inFile/aq_location_daily.txt", "r"):
        tmp = line[:-1].split("\t")
        time = dt.datetime.strptime(tmp[1], "%Y-%m-%d %H:%M:%S")
        if time < begin:
            continue
        if time > end:
            break
        aqi[tmp[0]+tmp[1].split(" ")[0]] = myutil.colorSelect(tmp[2])

    #sunny = dict()
    #rainy = dict()
    rain = dict()
    temp = dict()
    apr = dict()
    hum = dict()
    wspd = dict()
    #wdir = dict()

    for line in open("inFile/weather_location_daily.txt", "r"):
        tmp = line[:-1].split("\t")
        time = dt.datetime.strptime(tmp[1], "%Y-%m-%d %H:%M:%S")
        if time < begin:
            continue
        if time > end:
            break
        # sunny[tmp[0]+tmp[1].split(" ")[0]] = myutil.prepro(tmp[2])
        # rainy[tmp[0]+tmp[1].split(" ")[0]] = myutil.prepro(tmp[3])
        #rain[tmp[0] + tmp[1].split(" ")[0]] = myutil.prepro(tmp[4])
        temp[tmp[0] + tmp[1].split(" ")[0]] = myutil.prepro(tmp[5])
        #apr[tmp[0] + tmp[1].split(" ")[0]] = myutil.prepro(tmp[6])
        hum[tmp[0] + tmp[1].split(" ")[0]] = myutil.prepro(tmp[7])
        #wspd[tmp[0] + tmp[1].split(" ")[0]] = myutil.prepro(tmp[8])
        # wdir[tmp[0]+tmp[1].split(" ")[0]] = myutil.prepro(tmp[9])

    fig, axes = plt.subplots(nrows=5, ncols=5, figsize=(100, 100))

    print("test")

    # temperature
    data = np.array(list(temp.values()), dtype="float")
    data = data[data < 60]
    data = data [data > -60]
    limmin = min(data)
    limmax = max(data)
    ls = np.linspace(limmin, limmax, 100)
    kde = gaussian_kde(data)
    axes[0, 0].plot(ls, kde(ls), color="k", linewidth=3)
    #axes[0, 0].set_xlim(limmin, limmax)
    #
    # # humidity
    # data = np.array(list(hum.values()), dtype="float")
    # data = data[data < 100.1]
    # data = data [data > -0.1]
    # limmin = min(data)
    # limmax = max(data)
    # ls = np.linspace(limmin, limmax, 100)
    # kde = gaussian_kde(data)
    # axes[1, 1].plot(ls, kde(ls), color="k", linewidth=3)
    # #axes[0, 0].set_xlim(limmin, limmax)
    #
    # # rain
    # data = np.array(list(rain.values()), dtype="float")
    # data = data[data < 1000]
    # data = data [data > -0.1]
    # limmin = min(data)
    # limmax = max(data)
    # ls = np.linspace(limmin, limmax, 100)
    # kde = gaussian_kde(data)
    # axes[2, 2].plot(ls, kde(ls), color="k", linewidth=3)
    # #axes[0, 0].set_xlim(limmin, limmax)
    #
    # # air pressure
    # data = np.array(list(apr.values()), dtype="float")
    # data = data[data < 2000]
    # data = data [data > -0.1]
    # limmin = min(data)
    # limmax = max(data)
    # ls = np.linspace(limmin, limmax, 100)
    # kde = gaussian_kde(data)
    # axes[3, 3].plot(ls, kde(ls), color="k", linewidth=3)
    # #axes[0, 0].set_xlim(limmin, limmax)
    #
    # # wind speed
    # data = np.array(list(wspd.values()), dtype="float")
    # data = data[data < 100]
    # data = data [data > -0.1]
    # limmin = min(data)
    # limmax = max(data)
    # ls = np.linspace(limmin, limmax, 100)
    # kde = gaussian_kde(data)
    # axes[4, 4].plot(ls, kde(ls), color="k", linewidth=3)
    # #axes[0, 0].set_xlim(limmin, limmax)
    print("test")
    # temperature : humidity
    cls = {"green": list(),
           "yellow": list(),
           "orange": list(),
           "red": list(),
           "purple": list(),
           "maroon": list(),
           "lightgrey": list()}

    for k, v in list(aqi.items()):
        if myutil.temp_range(temp[k]) and myutil.hum_range(hum[k]):
            cls[v].append((temp[k], hum[k]))

    for color in list(cls.keys()):
        x = list(map(lambda p: p[0], cls[color]))
        y = list(map(lambda p: p[1], cls[color]))
        axes[0, 1].scatter(x, y, c=color, label=myutil.status(color), alpha=0.5)

    print("test")

    # # temperature : rain
    # cls = {"green": list(),
    #        "yellow": list(),
    #        "orange": list(),
    #        "red": list(),
    #        "purple": list(),
    #        "maroon": list(),
    #        "lightgrey": list()}
    #
    # for k, v in list(aqi.items()):
    #     if myutil.temp_range(temp[k]) and myutil.rain_range(rain[k]):
    #         cls[v].append((temp[k], rain[k]))
    #
    # for color in list(cls.keys()):
    #     x = list(map(lambda p: p[0], cls[color]))
    #     y = list(map(lambda p: p[1], cls[color]))
    #     axes[0, 2].scatter(x, y, c=color, label=myutil.status(color), alpha=0.5)
    #
    # # temperature : air pressure
    # cls = {"green": list(),
    #        "yellow": list(),
    #        "orange": list(),
    #        "red": list(),
    #        "purple": list(),
    #        "maroon": list(),
    #        "lightgrey": list()}
    #
    # for k, v in list(aqi.items()):
    #     if myutil.temp_range(temp[k]) and myutil.apr_range(apr[k]):
    #         cls[v].append((temp[k], apr[k]))
    #
    # for color in list(cls.keys()):
    #     x = list(map(lambda p: p[0], cls[color]))
    #     y = list(map(lambda p: p[1], cls[color]))
    #     axes[0, 3].scatter(x, y, c=color, label=myutil.status(color), alpha=0.5)
    #
    # # temperature : wind speed
    # cls = {"green": list(),
    #        "yellow": list(),
    #        "orange": list(),
    #        "red": list(),
    #        "purple": list(),
    #        "maroon": list(),
    #        "lightgrey": list()}
    #
    # for k, v in list(aqi.items()):
    #     if myutil.temp_range(temp[k]) and myutil.wspd_range(wspd[k]):
    #         cls[v].append((temp[k], wspd[k]))
    #
    # for color in list(cls.keys()):
    #     x = list(map(lambda p: p[0], cls[color]))
    #     y = list(map(lambda p: p[1], cls[color]))
    #     axes[0, 4].scatter(x, y, c=color, label=myutil.status(color), alpha=0.5)
    #
    # # humidity : rain
    # cls = {"green": list(),
    #        "yellow": list(),
    #        "orange": list(),
    #        "red": list(),
    #        "purple": list(),
    #        "maroon": list(),
    #        "lightgrey": list()}
    #
    # for k, v in list(aqi.items()):
    #     if myutil.hum_range(hum[k]) and myutil.rain_range(rain[k]):
    #         cls[v].append((hum[k], rain[k]))
    #
    # for color in list(cls.keys()):
    #     x = list(map(lambda p: p[0], cls[color]))
    #     y = list(map(lambda p: p[1], cls[color]))
    #     axes[1, 2].scatter(x, y, c=color, label=myutil.status(color), alpha=0.5)
    #
    # # humidity : air pressure
    # cls = {"green": list(),
    #        "yellow": list(),
    #        "orange": list(),
    #        "red": list(),
    #        "purple": list(),
    #        "maroon": list(),
    #        "lightgrey": list()}
    #
    # for k, v in list(aqi.items()):
    #     if myutil.hum_range(hum[k]) and myutil.apr_range(apr[k]):
    #         cls[v].append((hum[k], apr[k]))
    #
    # for color in list(cls.keys()):
    #     x = list(map(lambda p: p[0], cls[color]))
    #     y = list(map(lambda p: p[1], cls[color]))
    #     axes[1, 3].scatter(x, y, c=color, label=myutil.status(color), alpha=0.5)
    #
    # # humidity : wind speed
    # cls = {"green": list(),
    #        "yellow": list(),
    #        "orange": list(),
    #        "red": list(),
    #        "purple": list(),
    #        "maroon": list(),
    #        "lightgrey": list()}
    #
    # for k, v in list(aqi.items()):
    #     if myutil.hum_range(hum[k]) and myutil.wspd_range(wspd[k]):
    #         cls[v].append((hum[k], wspd[k]))
    #
    # for color in list(cls.keys()):
    #     x = list(map(lambda p: p[0], cls[color]))
    #     y = list(map(lambda p: p[1], cls[color]))
    #     axes[1, 4].scatter(x, y, c=color, label=myutil.status(color), alpha=0.5)
    #
    # # rain : air pressure
    # cls = {"green": list(),
    #        "yellow": list(),
    #        "orange": list(),
    #        "red": list(),
    #        "purple": list(),
    #        "maroon": list(),
    #        "lightgrey": list()}
    #
    # for k, v in list(aqi.items()):
    #     if myutil.rain_range(rain[k]) and myutil.apr_range(apr[k]):
    #         cls[v].append((rain[k], apr[k]))
    #
    # for color in list(cls.keys()):
    #     x = list(map(lambda p: p[0], cls[color]))
    #     y = list(map(lambda p: p[1], cls[color]))
    #     axes[2, 3].scatter(x, y, c=color, label=myutil.status(color), alpha=0.5)
    #
    # # rain : wind speed
    # cls = {"green": list(),
    #        "yellow": list(),
    #        "orange": list(),
    #        "red": list(),
    #        "purple": list(),
    #        "maroon": list(),
    #        "lightgrey": list()}
    #
    # for k, v in list(aqi.items()):
    #     if myutil.rain_range(rain[k]) and myutil.wspd_range(wspd[k]):
    #         cls[v].append((rain[k], wspd[k]))
    #
    # for color in list(cls.keys()):
    #     x = list(map(lambda p: p[0], cls[color]))
    #     y = list(map(lambda p: p[1], cls[color]))
    #     axes[2, 4].scatter(x, y, c=color, label=myutil.status(color), alpha=0.5)
    #
    # # air pressure : wind speed
    # cls = {"green": list(),
    #        "yellow": list(),
    #        "orange": list(),
    #        "red": list(),
    #        "purple": list(),
    #        "maroon": list(),
    #        "lightgrey": list()}
    #
    # for k, v in list(aqi.items()):
    #     if myutil.apr_range(apr[k]) and myutil.wspd_range(wspd[k]):
    #         cls[v].append((apr[k], wspd[k]))
    #
    # for color in list(cls.keys()):
    #     x = list(map(lambda p: p[0], cls[color]))
    #     y = list(map(lambda p: p[1], cls[color]))
    #     axes[2, 3].scatter(x, y, c=color, label=myutil.status(color), alpha=0.5)

    axes[1, 0].axis('off')
    axes[2, 0].axis('off')
    axes[3, 0].axis('off')
    axes[4, 0].axis('off')
    axes[2, 1].axis('off')
    axes[3, 1].axis('off')
    axes[4, 1].axis('off')
    axes[3, 2].axis('off')
    axes[4, 2].axis('off')
    axes[4, 3].axis('off')
    axes[0, 2].axis('off')
    axes[0, 3].axis('off')
    axes[0, 4].axis('off')
    axes[1, 2].axis('off')
    axes[1, 3].axis('off')
    axes[1, 4].axis('off')
    axes[2, 3].axis('off')
    axes[2, 4].axis('off')
    axes[3, 4].axis('off')
    axes[1, 1].axis('off')
    axes[2, 2].axis('off')
    axes[3, 3].axis('off')
    axes[4, 4].axis('off')

    plt.savefig("results/correlation.png")



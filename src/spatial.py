# using: utf-8
import matplotlib.colors as mc
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from src import geo

def clustering():
    inFile = open("infile/location.csv").readlines()
    feature = list()
    tmp = list()
    for line in inFile:
        name, lat, lon = line[:-1].split(",")
        tmp.append(lat)
        feature.append(geo.deg2km(float(lat), float(lon)))

    eps = 500 #[km]
    minPoints = 2
    pred = list(DBSCAN(eps=eps, min_samples=minPoints).fit(feature).labels_)

    # plot nodes
    plt.title("dbscan(h=" + str(eps) + "[km])")
    x = []
    y = []
    for i in range(len(set(pred))):
        x.append([])
        y.append([])
    for i in range(len(pred)):
        x[pred[i]].append(feature[i][0])
        y[pred[i]].append(feature[i][1])

    color_list = list(mc.cnames.keys())
    for i in range(len(x)):

        x_tmp = []
        y_tmp = []

        for j in range(len(x[i])):
            x_ij, y_ij = geo.km2deg(x[i][j], y[i][j])
            x_tmp.append(x_ij)
            y_tmp.append(y_ij)

        plt.scatter(y_tmp, x_tmp, label=i, cmap=color_list[i])

    plt.legend()
    plt.show()

def locationList():
    station = open("files/station_list.csv").readlines()

    l_dict = dict()
    for line in station:

        if line[0] == "#":
            continue

        sid, lat, lon, location_en, location_cn, lid = line[:-1].split(",")
        if location_en in l_dict:
            l_dict[location_en] += 1
        else:
            l_dict[location_en] = 0

    tmp = sorted(l_dict.items(), key=lambda x: x[0], reverse=True)
    k = list(map(lambda x: x[0], tmp))
    v = list(map(lambda x: x[1], tmp))
    plt.title("# of aqi stations")
    plt.bar(k, v, color="blue")
    plt.xticks(rotation=-90)
    plt.tick_params(axis='x', which='major', labelsize=1)
    plt.savefig("results/district.pdf")
    plt.show()

def cityList():
    location = open("files/location_list.csv").readlines()
    station = open("files/station_list.csv").readlines()

    l_dict = dict()
    for line in station:

        if line[0] == "#":
            continue

        sid, lat, lon, location_en, location_cn, lid = line[:-1].split(",")
        if location_en in l_dict:
            l_dict[location_en] += 1
        else:
            l_dict[location_en] = 1

    c_dict_station = dict()
    c_dict_location = dict()
    p_dict_station = dict()
    p_dict_location = dict()
    for line in location:

        if line[0] == "#":
            continue

        lid, location_en, location_cn, city_en, city_cn, province_en, province_cn, lat, lon, alt, city_level = line[:-1].split(",")

        if city_en in c_dict_location:
            c_dict_location[city_en] += 1
            c_dict_station[city_en] += l_dict[location_en]
        else:
            c_dict_location[city_en] = 1
            c_dict_station[city_en] = l_dict[location_en]

        if province_en in p_dict_location:
            p_dict_location[province_en] += 1
            p_dict_station[province_en] += l_dict[location_en]
        else:
            p_dict_location[province_en] = 1
            p_dict_station[province_en] = l_dict[location_en]


    tmp = sorted(c_dict_location.items(), key=lambda x: x[0], reverse=True)
    k = list(map(lambda x: x[0], tmp))
    v = list(map(lambda x: x[1], tmp))
    plt.bar(k, v)
    plt.title("# of districts")
    plt.bar(k, v, color="blue")
    plt.xticks(rotation=-90)
    plt.tick_params(axis='x', which='major', labelsize=1)
    plt.savefig("results/city_dist.pdf")
    plt.show()

def mapplot():

    outFile = open("results/spatial/location.txt", "w")
    tmp = set()
    for line in open("inFile/location.txt", "r"):
        idt, le, lc, ce, cc, pe, pc, lat, lon, alt, rank = line.strip().split("\t")
        outFile.write(lat+"\t"+lon+"\t"+pe+"\t"+"circle-red"+"\n")


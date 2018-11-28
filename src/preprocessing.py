# using: utf-8

def preprocessing():
    # locations = open("files/station_list.csv").readlines()
    # output = open("infile/s2l.csv", 'w')
    # for line in locations:
    #
    #     if line[0] == "#":
    #         continue
    #
    #     #id, l_en, l_cn, c_en, c_cn, p_en, p_cn, lat, lon, alt, level = line[:-1].split(",")
    #     id, lat, lon, en, cn, lid = line[:-1].split(",")
    #     output.write(id + "," + lat + "," + lon + "\n")

    input = open("files/full_time2.csv", "r").readlines()
    output = open("infile/full_time.csv", "w")
    output.write("# lid,date,aqi,pm25,pm10,co,so2,no2,o3,temp,hum,airpress,rain,wdsp\n")
    for item in input:
        data = item[:-1].split("\t")
        output.write(data[2] + "\t" + data[21] + " " + data[20] + "\t" + data[12] + "\t" + data[13] + "\t" +
                     data[14] + "\t" + data[15] + "\t" + data[16] + "\t" + data[17] + "\t" + data[18] + "\t" +
                     data[4] + "\t" + data[7] + "\t" + data[6] + "\t" + data[8] + "\t" + data[11] + "\n")
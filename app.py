from influxdb import InfluxDBClient
import time
import os

def checkDB():
    makeDB = True
    client = InfluxDBClient('influxdb', 8086, 'admin', 'admin')
    dbList = client.get_list_database()
    for x in dbList:
        for y in x:
            if x[y] == "loadAvg":
                makeDB = False

    if makeDB == True:
        client.create_database('loadAvg')

def writeToFile(measure, valueN):
    f = open("test.txt", "a")
    current_time = time.time_ns()
    measurement = "load" + measure
    value = valueN
    newdata = measurement + ",host=server01,region=us value=" + str(value) + " " + str(current_time) + " \n"
    f.write(newdata)
    f.close

def readFromFile():
    client = InfluxDBClient('influxdb', 8086, 'admin', 'admin', 'loadAvg')
    f = open("test.txt", "r")
    Lines = f.read().splitlines()
    client.write_points(Lines, time_precision='n', batch_size=1000, protocol='line')
    f = open("test.txt", "w")
    f.close


def main(count):
    load1, load5, load15 = os.getloadavg()
    load = {}
    load["1"] = load1
    load["5"] = load5
    load["15"] = load15
    for x,y in load.items():
        writeToFile(x,y)
        count = count + 1
    return count

checkDB()
count = 0
while True:
    count = main(count)
    time.sleep(60)
    if count % 9 == 0:
        readFromFile()
    

from db_station_create_table import stations, measure, engine
import csv


def load_clean_stations_csv():
    with open("clean_stations.csv", newline="") as csvfile:
        data=[]
        csvreader = csv.DictReader(csvfile)
        for i in csvreader:
            data.append ({"station" : i["station"], "latitude" : (i["latitude"]), "longitude" : (i["longitude"]), "elevation" : (i["elevation"]), "name" : i["name"], "country" : i["country"], "state" : i["state"]})
    return data


ins = stations.insert().values()
conn = engine.connect()
conn.execute(ins, load_clean_stations_csv())



def load_measure_stations_csv():
    data =[]
    with open("clean_measure.csv", newline="") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for i in csvreader:
            data.append ({"station" : i["station"], "date" : (i["date"]), "precip" : (i["precip"]), "tobs" : (i["tobs"])})
    return data


ins = measure.insert().values()
conn = engine.connect()
conn.execute(ins, load_measure_stations_csv())


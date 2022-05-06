from db_station_create_table import stations, measure, engine, Date
import csv


def load_clean_stations_csv():
    data =[]
    with open("clean_stations.csv", newline="") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for i in csvreader:
            data.append ({"station" : i["station"], "latitude" : float(i["latitude"]), "longitude" : float(i["longitude"]), "elevation" : float(i["elevation"]), "name" : i["name"], "country" : i["country"], "state" : i["state"]})
    return data

ins = stations.insert()
ins = stations.insert().values(station ="", latitude = 0, longitude =0, elevation = 0, name = "", country ="", state = "")
conn = engine.connect()
result = conn.execute(ins)
conn.execute(ins, load_clean_stations_csv())


def load_measure_stations_csv():
    data =[]
    with open("clean_measure.csv", newline="") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for i in csvreader:
            data.append ({"station" : i["station"], "date" : (i["date"]), "precip" : float(i["precip"]), "tobs" : int(i["tobs"])})
    return data


ins = measure.insert()
ins = measure.insert().values(station ="", date = "", precip = 0, tobs = 0)
conn = engine.connect()
result = conn.execute(ins)
conn.execute(ins, load_measure_stations_csv())
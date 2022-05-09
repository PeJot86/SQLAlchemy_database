from sqlalchemy import Table, Column, Integer, String, MetaData, Float
from sqlalchemy import create_engine, inspect

engine = create_engine("sqlite:///clean_stations.db")
insp = inspect(engine)


meta = MetaData()

stations = Table(
   "stations", meta,
   Column("station", String),
   Column("latitude", Float),
   Column("longitude", Float),
   Column("elevation", Integer),
   Column("name", String),
   Column("country", String),
   Column("state", String),
)

measure = Table(
   "measure", meta,
   Column("station", String),
   Column("date", String),
   Column("precip", Float),
   Column("tobs", Integer),
)

meta.create_all(engine)
print(insp.get_table_names())
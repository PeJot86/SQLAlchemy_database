
from db_station_create_table import engine


conn = engine.connect()
result = conn.execute("SELECT * FROM measure LIMIT 10").fetchall()

for row in result:
   print(row)
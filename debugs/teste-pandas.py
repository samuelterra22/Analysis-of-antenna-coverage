# Load the Pandas libraries with alias 'pd'
import pandas as pd

# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
from database.DAO.BaseStationDAO import BaseStationDAO

data = pd.read_csv("csv_licenciamento_ecb6f784.csv", encoding='ISO-8859-1')
# Preview the first 5 lines of the loaded data

rows = data.get_values()

i = 0
total = len(rows)

base_station_dao = BaseStationDAO()
base_station_dao.delete_all()

for row in rows:
    data = {
        "status": row[0],
        "entity": row[1],
        "num_fistel": row[2],
        "num_service": row[3],
        "num_ato": row[4],
        "num_station": row[5],
        "address": row[6],
        "uf": row[7],
        "cod_country": row[8],
        "emission": row[9],
        "initial_frequency": row[10],
        "final_frequency": row[11],
        "azimute": 'nan',
        "cod_station_type": row[13],
        "cod_antenna_type": row[14],
        "cod_equipment_antenna": row[15],
        "gain_antenna": row[16],
        "gain_coast_front_antenna": row[17],
        "lifting_angle_antenna": row[18],
        "half_power_angle": row[19],
        "polarization": row[20],
        "height": row[21],
        "cod_equipment_transmitter": row[22],
        "transmission_power": row[23],
        "latitude": row[24],
        "longitude": row[25],
        "first_license_date": row[26]
    }

    base_station_dao.insert(data)
    print(round(((i / total) * 100), 2), '%')
    i += 1
    # break

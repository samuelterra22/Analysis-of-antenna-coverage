import sqlite3

# connecting...
conn = sqlite3.connect('application.db')

# define a cursor
cursor = conn.cursor()

# creating a table (schema)
cursor.execute("""
CREATE TABLE base_station (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        status TEXT NOT NULL,
        entity TEXT NOT NULL,
        num_fistel INTEGER DEFAULT 0 NOT NULL,
        num_service INTEGER DEFAULT 0 NOT NULL,
        num_ato INTEGER DEFAULT 0 NOT NULL,
        num_station INTEGER DEFAULT 0 NOT NULL,
        address TEXT NOT NULL,
        uf TEXT NOT NULL,
        cod_country INTEGER DEFAULT 0 NOT NULL,
        emission TEXT NOT NULL,
        initial_frequency TEXT NOT NULL,
        final_frequency TEXT NOT NULL,
        azimute FLOAT DEFAULT 0.0 NOT NULL,
        cod_station_type TEXT NOT NULL,
        cod_antenna_type INTEGER DEFAULT 0 NOT NULL,
        cod_equipment_antenna TEXT DEFAULT '-' NOT NULL,
        gain_antenna FLOAT DEFAULT 0.0  NOT NULL,
        gain_coast_front_antenna FLOAT DEFAULT 0.0 NOT NULL,
        lifting_angle_antenna FLOAT DEFAULT 0.0  NOT NULL,
        half_power_angle FLOAT DEFAULT 0.0 NOT NULL,
        polarization TEXT NOT NULL,
        height FLOAT DEFAULT 0.0 NOT NULL,
        cod_equipment_transmitter TEXT NOT NULL,
        transmission_power TEXT NOT NULL,
        latitude TEXT NOT NULL,
        longitude TEXT NOT NULL,
        first_license_date TIMESTAMP NOT NULL,
        created_at TIMESTAMP NOT NULL,
        updated_at TIMESTAMP NOT NULL
);
""")

print('Tables created successful!')

# close connection...
conn.close()

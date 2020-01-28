#!/usr/bin/env python

import sqlite3

# connecting...
conn = sqlite3.connect("application.db")

# define a cursor
cursor = conn.cursor()

# creating a table (schema)
cursor.execute(
    """
CREATE TABLE base_station (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        status TEXT DEFAULT '-' NOT NULL,
        entity TEXT DEFAULT '-' NOT NULL,
        num_fistel TEXT DEFAULT '-' NOT NULL,
        num_service TEXT DEFAULT '-' NOT NULL,
        num_ato TEXT DEFAULT '-' NOT NULL,
        num_station TEXT DEFAULT '-' NOT NULL,
        address TEXT DEFAULT '-' NOT NULL,
        uf TEXT DEFAULT '-' NOT NULL,
        cod_country TEXT DEFAULT '-' NOT NULL,
        emission TEXT DEFAULT '-' NOT NULL,
        initial_frequency TEXT DEFAULT '-' NOT NULL,
        final_frequency TEXT DEFAULT '-' NOT NULL,
        azimute TEXT DEFAULT '-' NOT NULL,
        cod_station_type TEXT DEFAULT '-' NOT NULL,
        cod_antenna_type TEXT DEFAULT '-' NOT NULL,
        cod_equipment_antenna TEXT DEFAULT '-' NOT NULL,
        gain_antenna TEXT DEFAULT '-' NOT NULL,
        gain_coast_front_antenna TEXT DEFAULT '-' NOT NULL,
        lifting_angle_antenna TEXT DEFAULT '-' NOT NULL,
        half_power_angle TEXT DEFAULT '-' NOT NULL,
        polarization TEXT DEFAULT '-' NOT NULL,
        height TEXT DEFAULT '-' NOT NULL,
        cod_equipment_transmitter TEXT DEFAULT '-' NOT NULL,
        transmission_power TEXT DEFAULT '-' NOT NULL,
        latitude TEXT DEFAULT '-' NOT NULL,
        longitude TEXT DEFAULT '-' NOT NULL,
        first_license_date TEXT DEFAULT '-' NOT NULL,
        created_at TIMESTAMP NOT NULL,
        updated_at TIMESTAMP NOT NULL
);
"""
)

print("Tables created successful!")

# close connection...
conn.close()

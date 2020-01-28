#!/usr/bin/env python

import datetime
import sqlite3

from src.main.python.models import base_station


class BaseStationDAO:
    def __init__(self):
        self.database_url = "../database/migrations/application.db"

    def insert(self, base_station):
        conn = sqlite3.connect(self.database_url)
        try:
            c = conn.cursor()
            sql_query = """INSERT INTO 'base_station'
                                      ('status', 'entity', 'num_fistel', 'num_service', 'num_ato', 'num_station', 'address', 'uf', 
                                      'cod_country', 'emission', 'initial_frequency', 'final_frequency', 'azimute',
                                      'cod_station_type', 'cod_antenna_type', 'cod_equipment_antenna', 'gain_antenna',
                                      'gain_coast_front_antenna', 'lifting_angle_antenna', 'polarization', 'height',
                                      'cod_equipment_transmitter', 'transmission_power', 'latitude', 'longitude',
                                      'first_license_date', 'created_at', 'updated_at') 
                                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                                       ?, ?, ?);"""
            data_tuple = (
                base_station["status"],
                base_station["entity"],
                base_station["num_fistel"],
                base_station["num_service"],
                base_station["num_ato"],
                base_station["num_station"],
                base_station["address"],
                base_station["uf"],
                base_station["cod_country"],
                base_station["emission"],
                base_station["initial_frequency"],
                base_station["final_frequency"],
                base_station["azimute"],
                base_station["cod_station_type"],
                base_station["cod_antenna_type"],
                base_station["cod_equipment_antenna"],
                base_station["gain_antenna"],
                base_station["gain_coast_front_antenna"],
                base_station["lifting_angle_antenna"],
                base_station["polarization"],
                base_station["height"],
                base_station["cod_equipment_transmitter"],
                base_station["transmission_power"],
                base_station["latitude"],
                base_station["longitude"],
                self.__to_datetime(base_station["first_license_date"]),
                datetime.datetime.now(),
                datetime.datetime.now(),
            )
            c.execute(sql_query, data_tuple)
            conn.commit()
            c.close()
        except sqlite3.Error as error:
            print("Error while working with SQLite", error, base_station)
        finally:
            if conn:
                conn.close()

    def delete(self, base_station_id):
        conn = sqlite3.connect(self.database_url)
        try:
            c = conn.cursor()
            sql_query = """DELETE FROM base_station WHERE id = ? ;"""
            c.execute(sql_query, (base_station_id,))
            conn.commit()
            c.close()
        except sqlite3.Error as error:
            print("Error while working with SQLite: ", error)
        finally:
            if conn:
                conn.close()

    def delete_all(self):
        conn = sqlite3.connect(self.database_url)
        try:
            c = conn.cursor()
            sql_query = """DELETE FROM base_station;"""
            c.execute(sql_query)
            conn.commit()
            c.close()
        except sqlite3.Error as error:
            print("Error while working with SQLite: ", error)
        finally:
            if conn:
                conn.close()

    def update(self, base_station_id, base_station):
        conn = sqlite3.connect(self.database_url)
        try:
            c = conn.cursor()
            sql_query = """UPDATE base_station set (status, entity, num_fistel, num_service, num_ato, num_station,
                address, uf, cod_country, emission, initial_frequency, final_frequency, azimute, cod_station_type,
                cod_antenna_type, cod_equipment_antenna, gain_antenna, gain_coast_front_antenna, lifting_angle_antenna,
                polarization, height, cod_equipment_transmitter, transmission_power, latitude, longitude,
                first_license_date, created_at, updated_at)=(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?, ?, ?)
                WHERE id = ?;"""
            data_tuple = (
                base_station["status"],
                base_station["entity"],
                base_station["num_fistel"],
                base_station["num_service"],
                base_station["num_ato"],
                base_station["num_station"],
                base_station["address"],
                base_station["uf"],
                base_station["cod_country"],
                base_station["emission"],
                base_station["initial_frequency"],
                base_station["final_frequency"],
                base_station["azimute"],
                base_station["cod_station_type"],
                base_station["cod_antenna_type"],
                base_station["cod_equipment_antenna"],
                base_station["gain_antenna"],
                base_station["gain_coast_front_antenna"],
                base_station["lifting_angle_antenna"],
                base_station["polarization"],
                base_station["height"],
                base_station["cod_equipment_transmitter"],
                base_station["transmission_power"],
                base_station["latitude"],
                base_station["longitude"],
                base_station["first_license_date"],
                base_station["created_at"],
                datetime.datetime.now(),
                base_station_id,
            )
            c.execute(sql_query, data_tuple)
            conn.commit()
            c.close()
        except sqlite3.Error as error:
            print("Error while working with SQLite: ", error)
        finally:
            if conn:
                conn.close()

    def get_all(self):
        conn = sqlite3.connect(self.database_url)
        base_stations_list = []

        try:
            c = conn.cursor()
            sql_query = """SELECT * FROM base_station"""
            c.execute(sql_query)
            conn.commit()

            records = c.fetchall()
            for row in records:
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
                    "azimute": row[12],
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
                    "first_license_date": row[26],
                    "created_at": row[27],
                    "updated_at": row[28],
                }
                base_stations_list.append(base_station(data))
            c.close()
        except sqlite3.Error as error:
            print("Error while working with SQLite", error)
        finally:
            if conn:
                conn.close()
        return base_stations_list

    @staticmethod
    def __to_datetime(date_str):
        return datetime.datetime.strptime(date_str, "%d/%m/%Y")

#!/usr/bin/env python
import datetime

from src.main.python.models.base_model import BaseModel
from peewee import *

"""
Link to peewee documentation
http://docs.peewee-orm.com/en/latest/peewee/models.html
"""


class BaseStation(BaseModel):
    status = CharField()
    entity = CharField()
    num_fistel = CharField()
    num_service = CharField()
    num_ato = CharField()
    num_station = CharField()
    address = CharField()
    uf = CharField()
    cod_country = CharField()
    emission = CharField()
    initial_frequency = CharField()
    final_frequency = CharField()
    azimute = CharField()
    cod_station_type = CharField()
    cod_antenna_type = CharField()
    cod_equipment_antenna = CharField()
    gain_antenna = CharField()
    gain_coast_front_antenna = CharField()
    lifting_angle_antenna = CharField()
    half_power_angle = CharField()
    polarization = CharField()
    height = CharField()
    cod_equipment_transmitter = CharField()
    transmission_power = CharField()
    latitude = CharField()
    longitude = CharField()
    first_license_date = CharField()

    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField()

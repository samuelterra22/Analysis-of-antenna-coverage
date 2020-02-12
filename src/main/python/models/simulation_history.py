#!/usr/bin/env python
import datetime

from src.main.python.models.base_model import BaseModel
from peewee import *

"""
Link to peewee documentation
http://docs.peewee-orm.com/en/latest/peewee/models.html
"""


class SimulationHistory(BaseModel):
    """
    This class is the simulation history model for storage data in database
    """
    type = CharField()
    transmitter = CharField()
    antenna = CharField()
    propagation_model = CharField()
    environment = CharField()
    knife_edge_diffraction = CharField()
    color_scheme = CharField()
    radius = CharField()
    receiver_height = CharField()
    receiver_gain = CharField()
    receiver_sensitivity = CharField()
    antenna_polarisation = CharField()
    antenna_azimuth = CharField()
    antenna_down_tilt = CharField()
    antenna_horizontal_beamwidth = CharField()
    antenna_vertical_beamwidth = CharField()
    antenna_gain = CharField()
    antenna_front_to_back_ratio = CharField()
    antenna_feeder_line_loss = CharField()

    created_at = DateTimeField(default=datetime.datetime.now)

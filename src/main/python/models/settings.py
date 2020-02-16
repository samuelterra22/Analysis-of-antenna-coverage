#!/usr/bin/env python
import datetime

from src.main.python.models.base_model import BaseModel
from peewee import *


class Settings(BaseModel):
    """
    This class is the settings model for storage data in database
    """
    current_uf_id = IntegerField()
    current_county_id = IntegerField()

    updated_at = DateTimeField(default=datetime.datetime.now)

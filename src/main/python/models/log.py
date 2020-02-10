#!/usr/bin/env python
import datetime

from src.main.python.models.base_model import BaseModel
from peewee import *


class Log(BaseModel):
    level = CharField()
    type = CharField()
    message = TextField()
    stack_trace = TextField()

    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField()

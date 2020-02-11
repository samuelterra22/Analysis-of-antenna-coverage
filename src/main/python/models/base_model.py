from peewee import *


# Create a database instance that will manage the connection and
# execute queries
from src.main.python.utils.database import get_database_url

database = SqliteDatabase(get_database_url())


# Create a base-class all our models will inherit, which defines
# the database we'll be using.
class BaseModel(Model):

    class Meta:
        database = database

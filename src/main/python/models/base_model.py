from peewee import *

DATABASE = 'analysis-of-coverage-antenna'

# Create a database instance that will manage the connection and
# execute queries
database = SqliteDatabase(DATABASE)


# Create a base-class all our models will inherit, which defines
# the database we'll be using.
class BaseModel(Model):

    class Meta:
        database = database

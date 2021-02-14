from peewee import SqliteDatabase

from settings import DATABASE_NAME
from src.main.python.support.path import get_project_root


def get_database_url() -> str:
    """
    This method return the path of database according to database name
    in .env file
    :return:
    """
    return str(get_project_root()) + '/database/' + str(DATABASE_NAME)


def get_sqlite_database_instance() -> SqliteDatabase:
    """
    This method return the sql database instance
    :return:
    """
    return SqliteDatabase(get_database_url())


def create_tables() -> None:
    """
    In this method creates all the tables in the database
    according to the application models
    :return:
    """

    # Import models locally
    from src.main.python.models.base_station import BaseStation
    from src.main.python.models.city import City
    from src.main.python.models.log import Log
    from src.main.python.models.simulation_history import SimulationHistory
    from src.main.python.models.settings import Settings
    from src.main.python.models.state import State

    database = get_sqlite_database_instance()
    with database:
        database.create_tables([
            BaseStation, City, Log, SimulationHistory, Settings, State
        ])

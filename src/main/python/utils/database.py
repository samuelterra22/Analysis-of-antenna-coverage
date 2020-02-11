from peewee import SqliteDatabase

from src.main.python.utils.path import get_project_root


def get_database_url():
    return str(get_project_root()) + '/database/analysis_of_coverage_antenna.db'


def get_sqlite_database_instance():
    return SqliteDatabase(get_database_url())


def create_tables():
    from src.main.python.models.base_station import BaseStation
    from src.main.python.models.log import Log

    database = get_sqlite_database_instance()
    with database:
        database.create_tables([BaseStation, Log])

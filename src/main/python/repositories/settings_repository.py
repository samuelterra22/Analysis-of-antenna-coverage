#!/usr/bin/env python
from src.main.python.exceptions.application_exception import ApplicationException
from src.main.python.repositories.contracts.settings_repository_interface import (
    SettingsRepositoryInterface,
)
from src.main.python.models.settings import Settings
from src.main.python.support.logs import to_log_error


class SettingsRepository(SettingsRepositoryInterface):
    """

    """

    @staticmethod
    def get_all():
        """
        Return all Settings elements
        :return:
        """
        try:
            return Settings.get()
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return []

    @staticmethod
    def find_one_by_id(id):
        """
        This function return a settings row filtered by id.
        :param id: Id of settings in database
        :return: Return a Settings element
        """
        try:
            return Settings.get_by_id(id)
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None

    def find_one_by(self, criteria):
        """
        This method find a settings in database by criteria
        :param criteria:
        :return:
        """
        # Implementation here
        pass

    @staticmethod
    def store(data):
        """
        This method store a settings in database
        :param data:
        :return:
        """
        settings = Settings(
            cod_uf=data['cod_uf'],
            sigla_uf=data['sigla_uf'],
        )
        try:
            return settings.save()
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None

    @staticmethod
    def update(data, id):
        """
        This method update a settings in database
        :param data:
        :param id:
        :return:
        """
        settings = Settings.get_by_id(id)

        settings.cod_uf = data['cod_uf'],
        settings.sigla_uf = data['sigla_uf'],

        try:
            return settings.save()
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None

    @staticmethod
    def delete(id):
        """
        This method delete a settings in database
        :param id:
        :return:
        """
        try:
            return Settings.delete_by_id(id)
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None

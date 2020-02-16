#!/usr/bin/env python
from src.main.python.exceptions.application_exception import ApplicationException
from src.main.python.models.settings import Settings
from src.main.python.repositories.settings_repository import SettingsRepository
from src.main.python.support.logs import to_log_error


class SettingsService:
    """
    This class implement the settings service
    """

    def __init__(self):
        """
        SettingsService constructor
        """
        self.__repository = SettingsRepository()

    def store(self, data):
        """
        This method store a settings in database using settings repository
        :param data:
        :return:
        """
        try:
            return self.__repository.store(data)
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None

    def update(self, data, setting_name):
        """
        This method update a settings in database using settings repository
        :param setting_name:
        :param data:
        :return:
        """
        try:
            model = self.__repository.find_one_by(
                Settings
                    .select()
                    .where(Settings.option == setting_name)
            )

            return self.__repository.update(data, model.id)
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None

    def destroy(self, id):
        """
        This method destroy a settings in database using settings repository
        :param id:
        :return:
        """
        try:
            self.__repository.find_one_by_id(id)

            return self.__repository.delete(id)
        except Exception as e:
            print(e)

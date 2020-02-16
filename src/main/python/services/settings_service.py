#!/usr/bin/env python
from src.main.python.repositories.settings_repository import SettingsRepository


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
            self.__repository.store(data)
        except Exception as e:
            print(e)

    def update(self, data, id):
        """
        This method update a settings in database using settings repository
        :param data:
        :param id:
        :return:
        """
        self.__repository.find_one_by_id(id)

        try:
            self.__repository.update(data, id)
        except Exception as e:
            print(e)

    def destroy(self, id):
        """
        This method destroy a settings in database using settings repository
        :param id:
        :return:
        """
        self.__repository.find_one_by_id(id)

        try:
            self.__repository.delete(id)
        except Exception as e:
            print(e)

#!/usr/bin/env python
from src.main.python.controllers.base_controller import BaseController
from src.main.python.exceptions.application_exception import ApplicationException
from src.main.python.models.settings import Settings
from src.main.python.repositories.settings_repository import SettingsRepository
from src.main.python.services.settings_service import SettingsService
from src.main.python.support.logs import to_log_error


class SettingsController(BaseController):
    """
    This class implement the setting controller
    """

    def __init__(self):
        """
        Settings controller constructor using service and repository
        """
        self.__service = SettingsService()
        self.__repository = SettingsRepository()

    def store(self, data):
        """
        This method store a setting using the service
        :param data:
        :return:
        """
        self.__service.store(data)

    def get(self, data):
        """
        This method show details for a specific setting
        :param data:
        :return:
        """
        try:
            model = self.__repository.find_one_by(
                Settings
                    .select()
                    .where(Settings.option == data['option'])
            )

            return model.get()
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None

    def update(self, data, id):
        """
        This method update a setting using a service
        :param data:
        :param id:
        :return:
        """
        model = self.__repository.find_one_by(
            Settings.select().where(Settings.option == data['option'])
        )

        return self.__repository.update(data, model.id)

    def destroy(self, id):
        """
        This method delete a setting using a service
        :param id:
        :return:
        """
        pass

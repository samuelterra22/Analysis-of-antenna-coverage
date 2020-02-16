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

    def index(self):
        """
        This method return for view, all settings in the database
        :return:
        """
        pass

    def create(self):
        """
        This method return the view to add a new setting
        :return:
        """
        pass

    def store(self):
        """
        This method store a setting using the service
        :return:
        """
        pass

    def get(self, id):
        """
        This method show details for a specific setting
        :param id:
        :return:
        """
        try:
            model = self.__repository.find_one_by(
                Settings
                    .select()
                    .where(Settings.option == id)
            )

            return model.get()
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None

    def edit(self, id):
        """
        This method return the view to edit a setting
        :param id:
        :return:
        """
        pass

    def update(self, setting_name, id):
        """
        This method update a setting using a service
        :param setting_name:
        :param id:
        :return:
        """
        model = self.__repository.find_one_by(
            Settings.select().where(Settings.option == setting_name)
        )

        return self.__repository.update(setting_name, model.id)

    def destroy(self, id):
        """
        This method delete a setting using a service
        :param id:
        :return:
        """
        pass

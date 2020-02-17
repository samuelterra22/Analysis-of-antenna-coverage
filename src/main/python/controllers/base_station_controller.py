#!/usr/bin/env python
from src.main.python.controllers.base_controller import BaseController
from src.main.python.repositories.base_station_repository import BaseStationRepository
from src.main.python.services.base_station_service import BaseStationService


class BaseStationController(BaseController):
    """
    This class implement the base station controller
    """

    def __init__(self):
        """
        Base station controller constructor using service and repository
        """
        self.__service = BaseStationService()
        self.__repository = BaseStationRepository()

    def store(self):
        """
        This method store a base station using the service
        :return:
        """
        pass

    def get(self, data):
        """
        This method show details for a specific base station
        :param data:
        :return:
        """
        return self.__repository.find_one_by_id(id)

    def update(self, data, id):
        """
        This method update a base station using a service
        :param data:
        :param id:
        :return:
        """
        pass

    def destroy(self, id):
        """
        This method delete a base station using a service
        :param id:
        :return:
        """
        pass

#!/usr/bin/env python
from src.main.python.repositories.base_station_repository import BaseStationRepository


class BaseStationService:
    """
    This class implement the base station service
    """
    def __init__(self):
        """
        CityService constructor
        """
        self.__repository = BaseStationRepository()

    def store(self, data):
        """
        This method store a base station in database using base station repository
        :param data:
        :return:
        """
        try:
            self.__repository.store(data)
        except Exception as e:
            print(e)

    def update(self, data, id):
        """
        This method update a base station in database using base station repository
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
        This method destroy a base station in database using base station repository
        :param id:
        :return:
        """
        self.__repository.find_one_by_id(id)

        try:
            self.__repository.delete(id)
        except Exception as e:
            print(e)

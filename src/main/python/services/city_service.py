#!/usr/bin/env python
from src.main.python.repositories.city_repository import CityRepository


class CityService:
    """
    This class implement the city service
    """

    def __init__(self):
        """
        CityService constructor
        """
        self.__repository = CityRepository()

    def store(self, data):
        """
        This method store a city in database using city repository
        :param data:
        :return:
        """
        try:
            self.__repository.store(data)
        except Exception as e:
            print(e)

    def update(self, data, id):
        """
        This method update a city in database using city repository
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
        This method destroy a city in database using city repository
        :param id:
        :return:
        """
        self.__repository.find_one_by_id(id)

        try:
            self.__repository.delete(id)
        except Exception as e:
            print(e)

#!/usr/bin/env python
from src.main.python.exceptions.application_exception import ApplicationException
from src.main.python.repositories.contracts.city_repository_interface import (
    CityRepositoryInterface,
)
from src.main.python.models.city import City
from src.main.python.support.logs import to_log_error


class CityRepository(CityRepositoryInterface):
    """
    This class implement the state repository
    """

    @staticmethod
    def get_all():
        """
        Return all City elements
        :return:
        """
        try:
            return City.get()
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return []

    @staticmethod
    def find_one_by_id(id):
        """
        This function return a city row filtered by id.
        :param id: Id of city in database
        :return: Return a City element
        """
        try:
            return City.get_by_id(id)
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None

    @staticmethod
    def find_one_by(criteria):
        """
        This method find a city in database by criteria
        :param criteria:
        :return:
        """
        return criteria

    @staticmethod
    def store(data):
        """
        This method store a city in database
        :param data:
        :return:
        """
        city = City(
            name=data['name'],
            city_cod=data['city_cod'],
            state=data['state'],
        )

        try:
            return city.save()
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None

    @staticmethod
    def update(data, id):
        """
        This method update a city in database
        :param data:
        :param id:
        :return:
        """
        city = City.get_by_id(id)

        city.name = data['name'],
        city.city_cod = data['city_cod'],
        city.state = data['state'],

        try:
            return city.save()
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None

    @staticmethod
    def delete(id):
        """
        This method delete a city in database
        :param id:
        :return:
        """
        try:
            return City.delete_by_id(id)
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None

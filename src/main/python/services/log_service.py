#!/usr/bin/env python
from src.main.python.repositories.log_repository import LogRepository


class LogService:
    """
    This class implement the log service
    """

    def __init__(self):
        """
        LogService constructor
        """
        self.__repository = LogRepository()

    def store(self, data):
        """
        This method store a log in database using log repository
        :param data:
        :return:
        """
        try:
            self.__repository.store(data)
        except Exception as e:
            print(e)

    def update(self, data, id):
        """
        This method update a log in database using log repository
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
        This method destroy a log in database using log repository
        :param id:
        :return:
        """
        self.__repository.find_one_by_id(id)

        try:
            self.__repository.delete(id)
        except Exception as e:
            print(e)

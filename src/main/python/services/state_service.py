#!/usr/bin/env python
from src.main.python.repositories.state_repository import StateRepository


class StateService:
    """
    This class implement the state service
    """

    def __init__(self):
        """
        StateService constructor
        """
        self.__repository = StateRepository()

    def store(self, data):
        """
        This method store a state in database using state repository
        :param data:
        :return:
        """
        try:
            self.__repository.store(data)
        except Exception as e:
            print(e)

    def update(self, data, id):
        """
        This method update a state in database using state repository
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
        This method destroy a state in database using state repository
        :param id:
        :return:
        """
        self.__repository.find_one_by_id(id)

        try:
            self.__repository.delete(id)
        except Exception as e:
            print(e)

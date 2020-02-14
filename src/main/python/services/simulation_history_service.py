#!/usr/bin/env python
from src.main.python.repositories.simulation_history_repository import SimulationHistoryRepository


class SimulationHistoryService:
    """
    This class implement the simulation history service
    """

    def __init__(self):
        """
        SimulationHistoryService constructor
        """
        self.__repository = SimulationHistoryRepository()

    def store(self, data):
        """
        This method store a simulation history in database using
        simulation history repository
        :param data:
        :return:
        """
        try:
            self.__repository.store(data)
        except Exception as e:
            print(e)

    def update(self, data, id):
        """
        This method update a simulation history in database using
        simulation history repository
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
        This method destroy a simulation history in database using
        simulation history repository
        :param id:
        :return:
        """
        self.__repository.find_one_by_id(id)

        try:
            self.__repository.delete(id)
        except Exception as e:
            print(e)

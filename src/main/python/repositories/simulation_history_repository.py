#!/usr/bin/env python
from src.main.python.exceptions.application_exception import ApplicationException
from src.main.python.repositories.contracts.simulation_history_repository_interface import (
    SimulationHistoryRepositoryInterface,
)
from src.main.python.models.simulation_history import SimulationHistory
from src.main.python.support.logs import to_log_error


class SimulationHistoryRepository(SimulationHistoryRepositoryInterface):
    """
    This class implements the simulation history repository
    """

    @staticmethod
    def get_all():
        """
        Return all SimulationHistory elements
        :return:
        """
        try:
            return SimulationHistory.get()
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return []

    @staticmethod
    def find_one_by_id(id):
        """
        This function return a simulation history row filtered by id.
        :param id: Id of simulation history in database
        :return: Return a SimulationHistory element
        """
        try:
            return SimulationHistory.get_by_id(id)
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None

    @staticmethod
    def find_one_by(criteria):
        """
        This method find a simulation history in database by criteria
        :param criteria:
        :return:
        """
        return criteria

    @staticmethod
    def store(data):
        """
        This method store a simulation in database
        :param data:
        :return:
        """
        state = SimulationHistory(
            cod_uf=data['cod_uf'],
            sigla_uf=data['sigla_uf'],
        )
        try:
            return state.save()
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None

    @staticmethod
    def update(data, id):
        """
        This method update a simulation history in database
        :param data:
        :param id:
        :return:
        """
        state = SimulationHistory.get_by_id(id)

        state.cod_uf = data['cod_uf'],
        state.sigla_uf = data['sigla_uf'],

        try:
            return state.save()
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None

    @staticmethod
    def delete(id):
        """
        This method delete a simulation history in database
        :param id:
        :return:
        """
        try:
            return SimulationHistory.delete_by_id(id)
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None

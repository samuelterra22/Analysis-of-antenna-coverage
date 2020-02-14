#!/usr/bin/env python
from src.main.python.exceptions.application_exception import ApplicationException
from src.main.python.repositories.contracts.state_repository_interface import (
    StateRepositoryInterface,
)
from src.main.python.models.state import State
from src.main.python.utils.logs import to_log_error


class StateRepository(StateRepositoryInterface):
    """

    """

    @staticmethod
    def get_all():
        """
        Return all State elements
        :return:
        """
        try:
            return State.get()
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return []

    @staticmethod
    def find_one_by_id(id):
        """
        This function return a state row filtered by id.
        :param id: Id of state in database
        :return: Return a State element
        """
        try:
            return State.get_by_id(id)
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None

    def find_one_by(self, criteria):
        """
        This method find a state in database by criteria
        :param criteria:
        :return:
        """
        # Implementation here
        pass

    @staticmethod
    def store(data):
        """
        This method store a state in database
        :param data:
        :return:
        """
        state = State(
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
        This method update a state in database
        :param data:
        :param id:
        :return:
        """
        state = State.get_by_id(id)

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
        This method delete a state in database
        :param id:
        :return:
        """
        try:
            return State.delete_by_id(id)
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None

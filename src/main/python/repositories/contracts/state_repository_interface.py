#!/usr/bin/env python

from abc import ABC, abstractmethod
from src.main.python.repositories.contracts.base_repository import BaseRepository


class StateRepositoryInterface(ABC, BaseRepository):
    """
    This class contains the contract to implementation for
    StateRepository
    """
    @abstractmethod
    def get_all(self):
        """
        This method get all state stored in database
        :return:
        """
        pass

    @abstractmethod
    def find_one_by_id(self, id):
        """
        This method return a state based in an id
        :param id:
        :return:
        """
        pass

    @abstractmethod
    def find_one_by(self, criteria):
        """
        This method find on state repository using a
        specific criteria
        :param criteria:
        :return:
        """
        pass

    @abstractmethod
    def store(self, data):
        """
        This method store a state in database
        :param data:
        :return:
        """
        pass

    @abstractmethod
    def update(self, data, id):
        """
        This method update a state in database
        :param data:
        :param id:
        :return:
        """
        pass

    @abstractmethod
    def delete(self, id):
        """
        This method delete a state in database
        :param id:
        :return:
        """
        pass

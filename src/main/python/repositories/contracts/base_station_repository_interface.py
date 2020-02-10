#!/usr/bin/env python

from abc import ABC, abstractmethod
from src.main.python.repositories.contracts.base_repository import BaseRepository


class BaseStationRepositoryInterface(ABC, BaseRepository):
    """
    This class contains the contract to implementation for
    BaseStationRepository
    """
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def find_one_by_id(self, id):
        pass

    @abstractmethod
    def find_one_by(self, criteria):
        pass

    @abstractmethod
    def store(self, data):
        pass

    @abstractmethod
    def update(self, data, id):
        pass

    @abstractmethod
    def delete(self, id):
        pass

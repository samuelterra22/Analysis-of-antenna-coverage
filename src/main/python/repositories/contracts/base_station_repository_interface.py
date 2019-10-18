#!/usr/bin/env python

from abc import ABC
from src.main.python.repositories.contracts.base_repository import BaseRepository


class BaseStationRepositoryInterface(ABC, BaseRepository):

    def get_all(self):
        pass

    def find_one_by_id(self, id):
        pass

    def find_one_by(self, criteria):
        pass

    def store(self, data):
        pass

    def update(self, data, id):
        pass

    def delete(self, id):
        pass

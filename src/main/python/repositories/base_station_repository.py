#!/usr/bin/env python

from src.main.python.repositories.contracts.base_station_repository_interface import BaseStationRepositoryInterface


class BaseStationRepository(BaseStationRepositoryInterface):

    def get_all(self):
        # Implementation here
        pass

    def find_one_by_id(self, id):
        # Implementation here
        pass

    def find_one_by(self, criteria):
        # Implementation here
        pass

    def store(self, data):
        # Implementation here
        pass

    def update(self, data, id):
        # Implementation here
        pass

    def delete(self, id):
        # Implementation here
        pass

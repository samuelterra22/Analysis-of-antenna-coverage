#!/usr/bin/env python
from src.main.python.repositories.base_station_repository import BaseStationRepository


class BaseStationService:

    def __init__(self):
        self.__repository = BaseStationRepository()

    def store(self, data):
        try:
            self.__repository.store(data)
        except Exception as e:
            print(e)

    def update(self, data, id):
        self.__repository.find_one_by_id(id)

        try:
            self.__repository.update(data, id)
        except Exception as e:
            print(e)

    def destroy(self, id):
        self.__repository.find_one_by_id(id)

        try:
            self.__repository.delete(id)
        except Exception as e:
            print(e)

#!/usr/bin/env python
from src.main.python.controllers.base_controller import BaseController
from src.main.python.repositories.base_station_repository import BaseStationRepository
from src.main.python.services.base_station_service import BaseStationService


class BaseStationController(BaseController):
    def __init__(self):
        self.__service = BaseStationService()
        self.__repository = BaseStationRepository()

    def index(self):
        pass

    def add(self):
        pass

    def show(self, id):
        bs = self.__repository.find_one_by_id(id)
        # Return bs to view/dialog

    def edit(self, id):
        pass

    def update(self, data, id):
        pass

    def destroy(self, id):
        pass

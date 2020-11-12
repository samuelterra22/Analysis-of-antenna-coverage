#!/usr/bin/env python
from datetime import datetime

from src.main.python.controllers.base_controller import BaseController
from src.main.python.exceptions.application_exception import ApplicationException
from src.main.python.models.base_station import BaseStation
from src.main.python.support.logs import to_log_error


class BaseStationController(BaseController):
    """
    This class implement the base station controller
    """

    def __init__(self):
        """
        BaseStation controller constructor using service and repository
        """
        pass

    def store(self, data):
        """
        This method store a base station using the service
        :param data:
        :return:
        """
        try:
            return BaseStation.create(**data)

        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None

    def get(self, data):
        """
        This method show details for a specific base station
        :param data:
        :return:
        """
        print(data)

        try:
            return BaseStation.select().where(BaseStation.option == data['option']).get()
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None

    def get_all(self):
        """
        This method get all details for base stations
        :return:
        """
        try:
            return BaseStation.select()
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None

    def update(self, data, id):
        """
        This method update a base station using a service
        :param data:
        :param id:
        :return:
        """

        base_station = BaseStation.get_by_id(id)

        try:
            data['updated_at'] = datetime.now()
            return base_station.update(data).where(BaseStation.id == id).execute()
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None

    def destroy(self, id):
        """
        This method delete a base station using a service
        :param id:
        :return:
        """
        try:
            model = BaseStation.get_by_id(id)

            return BaseStation.delete_by_id(model.id)
        except Exception as e:
            print(e)

    def destroy_all(self):
        """
        This method delete all base station using a service
        :return:
        """
        try:
            return BaseStation.truncate_table()
        except Exception as e:
            print(e)

    def get_all_distinct(self):
        """
        This method get all details for base stations
        :return:
        """
        try:
            # select * from basestation group by endereco order by id;
            return BaseStation.select().group_by(BaseStation.endereco).order_by(BaseStation.id).execute()
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None
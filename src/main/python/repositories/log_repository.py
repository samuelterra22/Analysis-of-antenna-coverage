#!/usr/bin/env python
from src.main.python.exceptions.application_exception import ApplicationException
from src.main.python.repositories.contracts.log_repository_interface import (
    LogRepositoryInterface,
)
from src.main.python.models.log import Log
from src.main.python.utils.logs import to_log_error


class LogRepository(LogRepositoryInterface):
    """
    This class implement the log repository
    """
    @staticmethod
    def get_all():
        """
        Return all Log elements
        :return:
        """
        try:
            return Log.get()
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return []

    @staticmethod
    def find_one_by_id(id):
        """
        This function return a base station row filtered by id.
        :param id: Id of base station in database
        :return: Return a Log element
        """
        try:
            return Log.get_by_id(id)
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None

    def find_one_by(self, criteria):
        """
        This method find a log in database by criteria
        :param criteria:
        :return:
        """
        # Implementation here
        pass

    @staticmethod
    def store(data):
        """
        This method store a log in database
        :param data:
        :return:
        """
        log = Log(
            level=data['level'],
            type=data['type'],
            message=data['message'],
            stack_trace=data['stack_trace'],
        )
        try:
            return log.save()
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None

    @staticmethod
    def update(data, id):
        """
        This method update a log in database
        :param data:
        :param id:
        :return:
        """
        log = Log.get_by_id(id)

        log.level = data['level'],
        log.type = data['type'],
        log.message = data['message'],
        log.stack_trace = data['stack_trace'],

        try:
            return log.save()
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None

    @staticmethod
    def delete(id):
        """
        This method delete a log in database
        :param id:
        :return:
        """
        try:
            return Log.delete_by_id(id)
        except BaseException:
            e = ApplicationException()
            to_log_error(e.get_message())
            print(e)
            return None

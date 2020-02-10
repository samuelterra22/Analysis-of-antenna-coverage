#!/usr/bin/env python
from src.main.python.exceptions.application_exception import ApplicationException
from src.main.python.repositories.contracts.log_repository_interface import (
    LogRepositoryInterface,
)
from src.main.python.models.log import Log
from src.main.python.utils.logs import to_log_error


class LogRepository(LogRepositoryInterface):
    @staticmethod
    def get_all():
        """
        Return all BaseState elements
        :return:
        """
        try:
            return Log.get()
        except BaseException:
            e = ApplicationException()
            to_log_error(e)
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
            to_log_error(e)
            print(e)
            return None

    def find_one_by(self, criteria):
        # Implementation here
        pass

    @staticmethod
    def store(data):
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
            to_log_error(e)
            print(e)
            return None

    @staticmethod
    def update(data, id):
        log = Log.get_by_id(id)

        log.level = data['level'],
        log.type = data['type'],
        log.message = data['message'],
        log.stack_trace = data['stack_trace'],

        try:
            return log.save()
        except BaseException:
            e = ApplicationException()
            to_log_error(e)
            print(e)
            return None

    @staticmethod
    def delete(id):
        try:
            return Log.delete_by_id(id)
        except BaseException:
            e = ApplicationException()
            to_log_error(e)
            print(e)
            return None

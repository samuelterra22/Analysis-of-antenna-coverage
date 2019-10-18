#!/usr/bin/env python

from abc import ABC, abstractmethod


class BaseRepository(ABC):

    @abstractmethod
    def get_all(self):
        """
        Get all objects without criteria.
        :rtype: object
        """
        pass

    @abstractmethod
    def find_one_by_id(self, id):
        """
        Find a resource by id.
        :param id:
        :rtype: object
        """
        pass

    @abstractmethod
    def find_one_by(self, criteria):
        """
        Find a resource by criteria
        :param criteria:
        :rtype: object
        """
        pass

    @abstractmethod
    def store(self, data):
        """
        Save a resource.
        :param: data:
        :rtype: object
        """
        pass

    @abstractmethod
    def update(self, data, id):
        """
        Update a resource.
        :param: data:
        :param: id:
        :rtype: object
        """
        pass

    @abstractmethod
    def delete(self, id):
        """
        Delete a resource.
        :param: id:
        :rtype: object
        """
        pass

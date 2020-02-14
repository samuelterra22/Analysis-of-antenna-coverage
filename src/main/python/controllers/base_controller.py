from abc import ABC, abstractmethod


class BaseController(ABC):
    """
    This class represents the base controller interface to
    use in application models
    """

    @abstractmethod
    def index(self):
        """
        Index controller method
        :return:
        """
        pass

    @abstractmethod
    def create(self):
        """
        Create controller method
        :return:
        """
        pass

    @abstractmethod
    def store(self):
        """
        Store controller method
        :return:
        """
        pass

    @abstractmethod
    def show(self, id):
        """
        Show controller method
        :param id:
        :return:
        """
        pass

    @abstractmethod
    def edit(self, id):
        """
        Edit controller method
        :param id:
        :return:
        """
        pass

    @abstractmethod
    def update(self, data, id):
        """
        Update controller method
        :param data:
        :param id:
        :return:
        """
        pass

    @abstractmethod
    def destroy(self, id):
        """
        Destroy controller method
        :param id:
        :return:
        """
        pass

from abc import ABC, abstractmethod


class BaseController(ABC):
    @abstractmethod
    def index(self):
        """
        Index controller method
        """
        pass

    @abstractmethod
    def add(self):
        """
        Add controller method
        """
        pass

    @abstractmethod
    def show(self, id):
        """
        Show controller method
        """
        pass

    @abstractmethod
    def edit(self, id):
        """
        Edit controller method
        """
        pass

    @abstractmethod
    def update(self, data, id):
        """
        Update controller method
        """
        pass

    @abstractmethod
    def destroy(self, id):
        """
        Destroy controller method
        """
        pass

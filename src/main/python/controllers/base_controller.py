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
    def show(self):
        """
        Show controller method
        """
        pass

    @abstractmethod
    def edit(self):
        """
        Edit controller method
        """
        pass

    @abstractmethod
    def update(self):
        """
        Update controller method
        """
        pass

    @abstractmethod
    def destroy(self):
        """
        Destroy controller method
        """
        pass

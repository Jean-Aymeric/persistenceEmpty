from abc import ABCMeta, abstractmethod

from shared.imodel import IModel


class IView(metaclass=ABCMeta):
    @property
    @abstractmethod
    def controller(self):
        pass

    @controller.setter
    @abstractmethod
    def controller(self, view):
        pass

    @property
    @abstractmethod
    def model(self) -> IModel:
        pass

    @model.setter
    @abstractmethod
    def model(self, model: IModel):
        pass

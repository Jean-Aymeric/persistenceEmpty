from abc import ABCMeta, abstractmethod
from shared.iview import IView
from shared.imodel import IModel


class IController(metaclass=ABCMeta):
    @property
    @abstractmethod
    def view(self) -> IView:
        pass

    @view.setter
    @abstractmethod
    def view(self, view: IView):
        pass

    @property
    @abstractmethod
    def model(self) -> IModel:
        pass

    @model.setter
    @abstractmethod
    def model(self, model: IModel):
        pass

from shared.icontroller import IController
from shared.iview import IView
from shared.imodel import IModel


class Controller(IController):
    def __init__(self, view, model):
        self.__model: IModel = model
        self.__view: IView = view
        if view.controller != self:
            view.controller = self

    def start(self):
        pass

    @property
    def view(self) -> IView:
        return self.__view

    @view.setter
    def view(self, view: IView):
        if view.model != self.model:
            view.model = self.model
        if view.controller != self:
            view.controller = self
        self.__view = view

    @property
    def model(self) -> IModel:
        return self.__model

    @model.setter
    def model(self, model: IModel):
        self.__model = model

from shared.iview import IView
from shared.imodel import IModel


class View(IView):
    def __init__(self):
        self.__model: IModel | None = None
        self.__controller = None

    @property
    def controller(self):
        return self.__controller

    @property
    def model(self) -> IModel:
        return self.__model

    @controller.setter
    def controller(self, controller):
        self.__controller = controller
        if controller.view != self:
            controller.view = self
        self.model = controller.model

    @model.setter
    def model(self, model: IModel):
        self.__model = model

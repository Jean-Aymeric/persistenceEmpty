from abc import ABCMeta, abstractmethod


class IDataView(metaclass=ABCMeta):
    @abstractmethod
    def display(self):
        pass

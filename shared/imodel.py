from abc import ABCMeta, abstractmethod

from shared.data.data import Data


class IModel(metaclass=ABCMeta):
    @abstractmethod
    def getDataById(self, entityName: str, idData: int) -> Data:
        pass

    @abstractmethod
    def getAllData(self, entityName: str) -> [Data]:
        pass

    @abstractmethod
    def getAllData(self, entityName: str) -> [Data]:
        pass

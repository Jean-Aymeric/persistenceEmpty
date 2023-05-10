from abc import ABCMeta

from shared.data.idata import IData


class Data(IData, metaclass=ABCMeta):
    def __init__(self, __idData: int):
        self.__idData: int = __idData

    @property
    def idData(self) -> int:
        return self.__idData

    @idData.setter
    def idData(self, __idData: int):
        self.__idData = __idData

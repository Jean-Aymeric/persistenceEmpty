from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import Any


class IData(metaclass=ABCMeta):
    @property
    @abstractmethod
    def idData(self) -> int:
        pass

    @idData.setter
    @abstractmethod
    def idData(self, __idData: int):
        pass

    @abstractmethod
    def dataToJson(self) -> dict[str, Any]:
        pass

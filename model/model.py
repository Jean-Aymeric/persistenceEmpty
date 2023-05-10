from typing import Any

from model.dbconnector import DBConnector
from shared.data.data import Data
from shared.imodel import IModel


class Model(IModel):
    def __init__(self):
        self.__dbConnector: DBConnector = DBConnector("dbconf.json")

    def getDataById(self, entityName: str, __idData: int) -> Data:
        jsonData = self.__dbConnector.getJsonDataById(entityName, __idData)
        return Model.__dataConverter(entityName, jsonData)

    def getAllData(self, entityName: str) -> [Data]:
        jsonData: [dict[str, Any]] = self.__dbConnector.getAllJsonData(entityName)
        data: [Data] = []
        for json in jsonData:
            data.append(Model.__dataConverter(entityName, json))
        return data

    @staticmethod
    def __dataConverter(entityName: str, jsonData: dict[str, Any]) -> Data:
        raise Exception("Unknown entity name")

import json
from typing import Any

import mysql.connector
from mysql import connector
from mysql.connector.cursor import MySQLCursor

from shared.data.data import Data


class DBConnector:
    def __init__(self, dbConfigurationFileName: str):
        self.__db: connector = None
        self.__cursor: MySQLCursor | None = None
        self.__dbConfigurationFileName: str = dbConfigurationFileName
        self.__DBConnect()

    def __DBConnect(self):
        with open(self.__dbConfigurationFileName) as jsonFile:
            dbConf = json.load(jsonFile)
            self.__db = mysql.connector.connect(host=dbConf["host"],
                                                user=dbConf["user"],
                                                password=dbConf["password"],
                                                database=dbConf["database"])
            self.__cursor = self.__db.cursor()

    def __DBClose(self):
        self.__db.close()

    @staticmethod
    def __cursorResultsToJson(cursorResults: MySQLCursor) -> [dict[str, Any]]:
        columns = [column[0] for column in cursorResults.description]
        results = []
        for row in cursorResults.fetchall():
            results.append(dict(zip(columns, row)))
        return results

    def getJsonDataById(self, entityName: str, idData: int) -> dict[str, Any] | None:
        self.__cursor.execute("SELECT * FROM " + entityName + " WHERE id = " + str(idData))
        results = self.__cursorResultsToJson(self.__cursor)
        if len(results) == 0:
            return None
        return results[0]

    def getAllJsonData(self, entityName: str) -> [Data]:
        self.__cursor.execute("SELECT * FROM " + entityName)
        return self.__cursorResultsToJson(self.__cursor)

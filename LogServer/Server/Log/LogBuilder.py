import json
from . import Log

class LogBuilder:
    @staticmethod
    def buildLogObjectFromJsonMessage(JsonObject:map,ConnectionInfo:list,ServiceName:str)->Log:
        try:
            if(JsonObject["LOG_TYPE"]=="INFO"):
                return Log.InfoLog(ConnectionInfo[0],ConnectionInfo[1],ServiceName,JsonObject["MSG"])
            elif (JsonObject["LOG_TYPE"] == "DEBUG"):
                return Log.DebugLog(ConnectionInfo[0], ConnectionInfo[1], ServiceName, JsonObject["MSG"])
            elif (JsonObject["LOG_TYPE"] == "ERROR"):
                return Log.ErrorLog(ConnectionInfo[0], ConnectionInfo[1], ServiceName, JsonObject["MSG"])
            raise ValueError

        except KeyError as e:
            raise ValueError("Message is not formatted Properly")




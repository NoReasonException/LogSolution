import threading

import time
import socket
import select
import json
from ..Log.LogBuilder import LogBuilder
from ..Log.LogBuffer import LogBuffer

class LogsListener(threading.Thread):
    def __init__(self,ServerObject):
        threading.Thread.__init__(self)
        self.ServerObject=ServerObject

    def run(self)->None:
        self.ServerObject.LogObject.PrintLog(1, "Localhost", 0, "LogServlet", "LogListener Thread Engaged")
        while(True):
            self.getAllLogs()
            time.sleep(2)
    def getAllLogs(self):
        for i in range(len(self.ServerObject.ServiceConnectionList)):
            r, w, e = select.select([self.ServerObject.ServiceConnectionList[i]], [self.ServerObject.ServiceConnectionList[i]], [self.ServerObject.ServiceConnectionList[i]])
            if (r):

                try:
                    LogBuffer.submitLog(LogBuilder.buildLogObjectFromJsonMessage(json.loads(str(self.ServerObject.ServiceConnectionList[i].recv(4096), "utf-8")), self.ServerObject.ServiceConnectionListInfo[i],
                                                                     self.ServerObject.ServiceConnectionListName[i]))
                    self.ServerObject.ServiceConnectionList[i].sendall('{"STATUS":"RECEIVED"}'.encode("utf-8"))
                except (json.decoder.JSONDecodeError, ValueError) as e:
                    self.ServerObject.ServiceConnectionList[i].close()
                    self.ServerObject.ServiceConnectionList.remove(self.ServerObject.ServiceConnectionList[i])
                    self.ServerObject.ServiceConnectionListInfo.remove(self.ServerObject.ServiceConnectionListInfo[i])
                    self.ServerObject.ServiceConnectionListName.remove(self.ServerObject.ServiceConnectionListName[i])
                    del i


        #send to all listeners





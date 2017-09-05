import threading

import time
import socket
import select
import json
from ..Log.LogBuilder import LogBuilder

class PrintLogsThread(threading.Thread):
    def __init__(self,ServerObject):
        threading.Thread.__init__(self)
        self.ServerObject=ServerObject

    def run(self):
        self.ServerObject.LogObject.PrintLog(1, "Localhost", 0, "LogServlet", "LogSender Thread Engaged")
        while(True):
            for i in self.ServerObject.ServiceConnectionList:
                r,w,e=select.select([i],[i],[i])
                if(r):
                    try:
                        print(str(LogBuilder.buildLogObjectFromJsonMessage(json.loads(str(i.recv(4096),"utf-8")),["",12],"TestService")))
                    except json.decoder.JSONDecodeError as e:
                        pass

            time.sleep(2)
        #send to all listeners





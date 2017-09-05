import threading

import time
import socket
import select

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
                    p

            print("Scan OK")

            time.sleep(2)
        #send to all listeners





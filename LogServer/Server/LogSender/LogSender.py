import threading

from Server.Log.LogBuffer import *
import time
class LogSenderThread(threading.Thread):
    def __init__(self,ServerObject):
        threading.Thread.__init__(self)
        self.ServerObject=ServerObject
    def run(self):
        while(True):
            self.sendLogs()
    time.sleep(5)
    def sendLogs(self)->None:
        while(not LogBuffer.isBufferEmpty()):
            Log = LogBuffer.getLastLog()
            for i in self.ServerObject.ListenersConnectionList:
                i.sendall(str(LogBuffer.getLastLog()).encode("utf-8"))
            print(LogBuffer.getLastLog())
            LogBuffer.delLastLog()
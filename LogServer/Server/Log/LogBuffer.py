from ..Log.Log import *
import threading
LogBufferLock = threading.Lock()
class LogBuffer:
    __Buffer = list()
    @staticmethod
    def submitLog(LogObject:Log)->None:
        LogBufferLock.acquire(True)
        LogBuffer.__Buffer.append(LogObject)
        LogBufferLock.release()
    @staticmethod
    def getLastLog()->Log:
        try:
            return LogBuffer.__Buffer[-1]
        except IndexError as e:
            return None
    @staticmethod
    def delLastLog()->None:
        try:
            LogBufferLock.acquire(True)
            LogBuffer.__Buffer.remove(LogBuffer.__Buffer[-1])
            LogBufferLock.release()
        except IndexError as e:
            return None
    @staticmethod
    def isBufferEmpty():
        return len(LogBuffer.__Buffer)<1


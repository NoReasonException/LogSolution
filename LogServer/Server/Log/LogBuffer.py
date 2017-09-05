from LogServer.Server.Log.Log import *
class LogBuffer:
    
    def __init__(self):
        self.__Buffer = list()

    def submitLog(self,LogObject:Log)->None:
        self.__Buffer.append(LogObject)
    def getLastLog(self)->Log:
        try:
            return self.__Buffer[-1]
        except IndexError as e:
            return None
    def delLastLog(self)->None:
        try:
            self.__Buffer.remove(-1)
        except IndexError as e:
            return None

    def __iter__(self):
        return self
    def next(self):
        retval=self.getLastLog()
        self.delLastLog()
        return retval

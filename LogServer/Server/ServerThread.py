import threading
from Server.Connection.ProtocolVerify import AcceptConnectionThread
from Server.PrintLogsThread.PrintLogsThread import PrintLogsThread
import json
class ServerThread(threading.Thread):
    ServerThreadObject = None
    def __init__(self,LogObject):
        threading.Thread.__init__(self)
        self.LogObject = LogObject
        self.SocketObject = LogObject.SocketObject
        self.ArrayListLock = threading.Lock()
        self.ServiceConnectionList = list()
        self.ServiceConnectionListName=list()
        self.ServiceConnectionListInfo=list()
        self.ListenersConnectionList=list()
        self.ListenersConnectionNames=list()
        self.ListenersConnectionListInfo=list()

    def run(self):
        if(ServerThread.ServerThreadObject==None):
            ServerThread.ServerThreadObject=self
        else:
            return

        self.LogObject.PrintLog(1,"Localhost",0,"LogServlet","Ready to Accept Connections...")
        PrintLogsThread(self).start()
        while(True):

            conn,info=self.SocketObject.accept()
            self.LogObject.PrintLog(1,"Localhost",0,"LogServlet","Connection Requested "+info[0]+":"+str(info[1]))
            AcceptConnectionThread(conn,info,self).start()












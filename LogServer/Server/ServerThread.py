import threading
from Server.Connection.ProtocolVerify import AcceptConnectionThread
from Server.LogsListener.LogsListener import LogsListener
from Server.LogSender.LogSender import LogSenderThread
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
        LogsListener(self).start()
        LogSenderThread(self).start()
        while(True):

            conn,info=self.SocketObject.accept()
            self.LogObject.PrintLog(1,"Localhost",0,"LogServlet","Connection Requested "+info[0]+":"+str(info[1]))
            AcceptConnectionThread(conn,info,self).start()
    def netstat_s(self):
        print("Netstat for Services Only (-s)\n")
        for i in range(len(self.ServiceConnectionListInfo)):
            print(self.ServiceConnectionListInfo[i][0] + "\t\t\t" + str(self.ServiceConnectionListInfo[i][1]) + "\t\t\t" +
                  self.ServiceConnectionListName[i])

    def netstat_l(self):
        print("Netstat for Listeners Only (-s)\n")
        for i in range(len(self.ListenersConnectionListInfo)):
            print(self.ListenersConnectionListInfo[i][0] + "\t\t\t" + str(
                self.ListenersConnectionListInfo[i][1]) + "\t\t\t" +
                    self.ListenersConnectionNames[i])













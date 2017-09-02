
import json
import re
import socket
from datetime import datetime

from Server import ServerThread as ServerThread

from Server.Log.Log import *
class TypeOfLog:

    INFO=1
    ERROR=2
    EXCEPTION=3

class MainClass:
    def configLoader(self):
        with open("conf.json","r") as data_file:
            return json.load(data_file)

    def bindDataIsOk(self):
        if (not re.match(
                "^((([01][0-9]{2})|([2][0-5]{2})|([0-9]{1,2}))\.){3}((([01][0-9]{2})|([2][0-5]{2})|([0-9]{1,2})))$",self.configs["BIND_IP"]) \
                    and self.configs["BIND_IP"] != "ALL"):
            return False
        try:
            if (int(self.configs["BIND_PORT"]) < 1 or int(self.configs["BIND_PORT"]) > 65535 ):
                return False
        except ValueError:
            return False
        return True
    @staticmethod
    def toStandardBindParameter(config):
        if(config["BIND_IP"]=="ALL"):
            return ("",int(config["BIND_PORT"]))
        return (config["BIND_IP"],int(config["BIND_PORT"]))


    def PrintLog(self,TypeOfLogCode,FromAddr,FromPort,Service,Description):
        if(TypeOfLogCode==TypeOfLog.INFO):
            print("[INFO][%s][From %s %d][%s]%s" % (datetime.now(),FromAddr, FromPort, Service, Description))
        elif(TypeOfLogCode==TypeOfLog.ERROR):
            print("[ERR_FATAL][From %s %d][%s]%s" % (FromAddr, FromPort, Service, Description))

    def __init__(self):
        self.configs = self.configLoader()
        self.SocketObject = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        if(not self.bindDataIsOk()):
            self.PrintLog(TypeOfLog.ERROR,"Localhost",0,"LogServlet","Invalid IP in conf.json BIND_IP Value")
            return
        self.SocketObject.bind(MainClass.toStandardBindParameter(self.configs))
        self.SocketObject.listen(5)
        self.PrintLog(TypeOfLog.INFO,"Localhost",0,"LogServlet","LogServlet 0.1 Started at "+str(self.toStandardBindParameter(self.configs)))
        self.Shell()
        #s = ServerThread.ServerThread(self.SocketObject,self)
        #s.start()
    def Shell(self):
        s = ServerThread.ServerThread(self)
        print(str(ErrorLog("aaa",123,"ass","aaaa")))
        print(str(InfoLog("aaa",123,"ass","aaaa")))
        print(str(DebugLog("aaa",123,"ass","aaaa")))
        while(True):
            Com = input(">")
            if(Com=="Listen"):
            #if(True):
                s.start()
            elif(Com=="netstat"):
                for i in s.ServiceConnectionListInfo:print(i)

















MainClass()
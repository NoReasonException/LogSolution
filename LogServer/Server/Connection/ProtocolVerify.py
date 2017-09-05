
import threading
import json

class InvalidRequest(Exception):
    def __init__(self,info):
        self.connectionInfo = info
    def __repr__(self):
        return repr(self.connectionInfo[0]+":"+self.connectionInfo[1])

class AcceptConnectionThread(threading.Thread):
    def __init__(self,conn,info,ServerObject):
        threading.Thread.__init__(self)
        self.ConnectionObject = conn
        self.InfoObject = info
        self.ServerObject=ServerObject

    def run(self):
        if (self.verifyConnection()):
            self.ServerObject.LogObject.PrintLog(1, "Localhost", 0, "LogServlet",
                                    "Connection Accepted " + self.InfoObject[0] + ":" + str(self.InfoObject[1]))
        else:
            self.ServerObject.LogObject.PrintLog(1, "Localhost", 0, "LogServlet",
                                                 "Connection Dropped " + self.InfoObject[0] + ":" + str(
                                                     self.InfoObject[1]))
    def verifyConnection(self):
        s=str()
        while(True):
            s+=(self.ConnectionObject.recv(4096).decode("utf-8"))
            if("END" in s):
                break
        try :
            request=json.loads(s)
            if(not self.ProtocolVerify(request)):
                raise InvalidRequest(self.InfoObject)
            self.ServerObject.ArrayListLock.acquire()
            if (request["TYPE"] == "SERVICE"):
                self.ServerObject.ServiceConnectionList.append(self.ConnectionObject)
                self.ServerObject.ServiceConnectionListInfo.append(self.InfoObject)
                self.ServerObject.ServiceConnectionListName.append(request["NAME"])
            elif (request["TYPE"] == "LISTENER"):
                self.ServerObject.ListenersConnectionList.append(self.ConnectionObject)
                self.ServerObject.ListenersConnectionListInfo.append(self.InfoObject)
                self.ServerObject.ListenersConnectionNames.append(request["NAME"])
            self.ServerObject.ArrayListLock.release()
            for i in self.ServerObject.ServiceConnectionListInfo:print(i)
        except (json.JSONDecodeError,InvalidRequest) as e:
            self.ConnectionObject.sendall(bytes("{\"STATUS\":\"BAD\"}","utf-8"))#TODO:Secure this section ;)
            self.ConnectionObject.close()
            return False

        return True
    @staticmethod
    def ProtocolVerify(json):
        try:
            if ((json["TYPE"] == "SERVICE" or json["TYPE"] == "LISTENER")):
                if(json["NAME"]!=None):
                    if (json["END"] == "1"):
                        return True
                    return False
                return False

            return False
        except KeyError:
            return False


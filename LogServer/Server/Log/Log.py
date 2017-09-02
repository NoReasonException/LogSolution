
from datetime import *
class LogColors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
class Log:

    def __init__(self,FromAddr,FromPort,Service,Decription):
        self.FromAddr=FromAddr
        self.FromPort=FromPort
        self.Service=Service
        self.Description=Decription
    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        raise NotImplemented

    #Override __repr__ and __str__
class ErrorLog(Log):
    def __init__(self, FromAddr, FromPort, Service, Decription):
        Log.__init__(self,FromAddr,FromPort,Service,Decription)
        pass
    def __repr__(self):
        return (LogColors.FAIL+LogColors.UNDERLINE+"[FATAL_ERR][%s][From %s %d][%s]%s" % (datetime.now(), self.FromAddr, self.FromPort, self.Service, self.Description))

class InfoLog(Log):
    def __init__(self, FromAddr, FromPort, Service, Decription):
        Log.__init__(self,FromAddr,FromPort,Service,Decription)

    def __repr__(self):
        return (LogColors.WARNING+"[INFO][%s][From %s %d][%s]%s" % (datetime.now(), self.FromAddr, self.FromPort, self.Service, self.Description))


class DebugLog(Log):
    def __init__(self, FromAddr, FromPort, Service, Decription):
        Log.__init__(self, FromAddr, FromPort, Service, Decription)

    def __repr__(self):
        return (LogColors.GREEN+"[DEBUG][%s][From %s %d][%s]%s" % (datetime.now(), self.FromAddr, self.FromPort, self.Service, self.Description))


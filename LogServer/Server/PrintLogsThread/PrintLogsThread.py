import threading

class PrintLogsThread(threading.Thread):
    def __init__(self,LogObject):
        threading.Thread.__init__(self)
        self.LogObject=LogObject
    def run(self):
        self.LogObject.PrintLog(1, "Localhost", 0, "LogServlet", "LogSender Thread Engaged")





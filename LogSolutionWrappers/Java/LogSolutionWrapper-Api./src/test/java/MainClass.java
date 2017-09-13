import com.NoReasonException.LogSolutionWrapper.LogObjects.InfoLog;
import com.NoReasonException.LogSolutionWrapper.LogObjects.Log;
import com.NoReasonException.LogSolutionWrapper.LogSenderObjects.LogServerConnection;
import sun.applet.Main;

import java.io.IOException;
import java.net.Inet4Address;
import java.net.InetAddress;
import java.net.UnknownHostException;

/*
    A simple Example!
 */
public class MainClass {

    public static void main(String args[])throws UnknownHostException,IOException,InterruptedException{
        LogServerConnection MainConnectionObject = LogServerConnection.createInstance(Inet4Address.getByName("192.168.1.203"),9998,"TestLogBroadcast");
        MainConnectionObject.buildHandShakeRequest();
        MainConnectionObject.flushRequestBuffer();

        Log Event = new InfoLog("blah blah initialized");
        Event.buildLogRequest(MainConnectionObject);
        MainConnectionObject.flushRequestBuffer();
        //MainConnectionObject.close();
        Thread.sleep(200);
        Log Event2 = new InfoLog("blah blah initialized 2");
        Event.buildLogRequest(MainConnectionObject);
        MainConnectionObject.flushRequestBuffer();



    }
}

import com.NoReasonException.LogSolutionWrapper.LogObjects.InfoLog;
import com.NoReasonException.LogSolutionWrapper.LogObjects.Log;
import com.NoReasonException.LogSolutionWrapper.LogSenderObjects.LogServerConnection;

import java.io.IOException;
import java.net.InetAddress;
import java.net.UnknownHostException;

public class MainClass {
    public static void main(String args[])throws UnknownHostException,IOException,InterruptedException{
        LogServerConnection conn  = LogServerConnection.createInstance(InetAddress.getByName("192.168.1.203"),9998,"Test"); //Create server connection
        Log test = new InfoLog("TEST!!");
        test.buildLogRequest(conn);
        conn.flushRequestBuffer();
        //conn.flushRequestBuffer();//initial handshake
        //Thread.sleep(5);
        //Log r = new InfoLog("Warn");//new Log
        //r.buildLogRequest(conn);//build request for log
        //conn.flushRequestBuffer();



    }
}

package com.NoReasonException.LogSolutionWrapper.LogSenderObjects;

import java.io.BufferedOutputStream;
import java.io.Closeable;
import java.io.IOException;
import java.net.InetAddress;
import java.net.Socket;
import com.NoReasonException.LogSolutionWrapper.annons.ClassVersion;
import org.json.*;


/***
 * LogServerConnection Class
 * Represents a LogServer Connection to server
 *
 * @author Stefanos Stefanou (stefan1998xd@gmail.com)

 */
@ClassVersion(ClassVersion = "1.0",ServerVersionSupports = "1.0",SpecificationVersion = "0.0.1")
public class LogServerConnection implements Closeable{
    private  Socket SocketObject = null;                                                                    //Socket Object
    private  java.io.BufferedOutputStream SocketBuffer=null;                                                //Byte Buffer for output stream
    private boolean isHandshaked = false;
    private  java.util.Map<java.lang.String,java.lang.String> RequestMap =new java.util.HashMap<java.lang.String, java.lang.String>();
    private  JSONObject RequestJson= null;
    private  java.lang.String Name = null;



    private LogServerConnection(){}


    /***
     * .close() , Inherited from Closeable Interface
     */
    public void close() throws IOException{
        SocketBuffer.close();

    }

    /***
     * <h1>Factory-method for LogServerConnection Objects </h1>
     * .createInstance(Address,Port,Name);
     *
     * @param Address     = The Ip Address of LogServer Host(Tested on Ipv4)
     * @param Port        = The Hosts Port
     * @param ServiceName = The Service Name
     * @throws java.io.IOException , in case of invalid ip , invalid port , or request_devied
     * @return LogServerConnection
     *
     *

     */
    public static LogServerConnection createInstance(InetAddress Address , int Port, java.lang.String ServiceName)throws IOException{
        LogServerConnection LogSender = new LogServerConnection();                                          //Create RetInstance
        LogSender.SocketObject=new Socket(Address,Port);                                                    //Initialize Socket
        LogSender.SocketBuffer = new BufferedOutputStream(LogSender.SocketObject.getOutputStream());        //Initialize Buffer
        LogSender.Name=ServiceName;                                                                         //Service Name
        return LogSender;                                                                                   //Name
    }
    /***
     * <h1>flushRequestBuffer() , Sends a prebuild request in the server </h1>
     *
     * @throws java.io.IOException (broken_pipe)
     * @throws java.lang.RuntimeException (In case of send request without send Handshake first)
     *
     *

     */
    public void flushRequestBuffer()throws IOException{
        if(!this.isHandshaked && !this.isHandshakeRequest()){
            throw new RuntimeException("Must send handshake request first!");
        }
        else{
            this.isHandshaked=true;
        }
        //Send Request to server
        this.convertToJson();                                                                               //Debug Purposes
        byte Message[]=this.RequestJson.toString().getBytes();                                              //Convert Message to Unicode-8 Byte String
                                                                                                             //Send and flush()
        this.SocketBuffer.write(Message);
        this.SocketBuffer.flush();
        try{
            Thread.sleep(500);

        }catch (Exception e){}

    }

    /***
     *<h1> .buildHandShakeRequest</h1>
     * <h4>build the initialRequest in buffer ! You must call .buildHandShakeRequest and .flushRequestBuffer before send any logs!</h4>
     * <h3>If dont , .flushRequestBuffer will throw Runtime Exception</h3>
     *
     */
    public void buildHandShakeRequest(){                                                                    //Build initial handshake request

        this.RequestMap.put("TYPE","SERVICE");                                                       //Type of service (Purpose of this wrapper)
        this.RequestMap.put("NAME",this.Name);                                                          //Nane given in constructor
        this.RequestMap.put("END","1");                                                              //END of message

    }

    /***
     * <h1>.getRequestMap</h1>
     * <h3>Returns the map request buffer , this map , will convert to JSONObject when you call the .flushRequestBuffer! </h3>
     * @return java.util.Map<java.lang.String,java.lang.String>
     */
    private java.util.Map<java.lang.String,java.lang.String> getRequestMap(){                               //getter for request map
        return this.RequestMap;
    }
    public void setRequestMap(java.util.Map<java.lang.String,java.lang.String> newRequestMap){
        this.RequestMap=newRequestMap;
    }

    /***
     * <h1>.convertToJson()</h1>
     * <h3>Converts the Map to JSONObject so to send as json request to server</h3>
     */
    private void convertToJson(){                                                                           //Convert Request map to json object
        this.RequestJson=new JSONObject(this.RequestMap);
    }
    private boolean isHandshakeRequest(){
        if(this.RequestMap.containsKey("TYPE") &&
                this.RequestMap.get("TYPE").equals("SERVICE") &&
                this.RequestMap.containsKey("NAME") &&
                this.RequestMap.containsKey("END")){
            return true;
        }
        return false;
    }




}


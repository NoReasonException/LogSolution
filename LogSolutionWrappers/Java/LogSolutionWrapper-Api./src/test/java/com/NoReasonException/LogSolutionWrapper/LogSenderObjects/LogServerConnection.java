package com.NoReasonException.LogSolutionWrapper.LogSenderObjects;

import java.io.BufferedOutputStream;
import java.io.IOException;
import java.net.InetAddress;
import java.net.Socket;
import com.NoReasonException.LogSolutionWrapper.annons.ClassVersion;



import com.NoReasonException.LogSolutionWrapper.LogObjects.Log;
import org.json.*;
@ClassVersion(ClassVersion = "1.0",ServerVersionSupports = "1.0",SpecificationVersion = "0.0.1")
public class LogServerConnection{
    private  Socket SocketObject = null;
    private  java.io.BufferedOutputStream SocketBuffer=null;
    private boolean isHandshaked = false;
    private  java.util.Map<java.lang.String,java.lang.String> RequestMap =new java.util.HashMap<String, String>();
    private  JSONObject RequestJson= null;
    private  java.lang.String Name = null;

    private LogServerConnection(){}

    public static LogServerConnection createInstance(InetAddress Address , int Port, java.lang.String ServiceName)throws IOException,java.lang.RuntimeException{
        LogServerConnection LogSender = new LogServerConnection();                                          //Create RetInstance
        LogSender.SocketObject=new Socket(Address,Port);                                                    //Initialize Socket
        LogSender.SocketBuffer = new BufferedOutputStream(LogSender.SocketObject.getOutputStream());        //Initialize Buffer
        LogSender.Name=ServiceName;                                                                         //Service Name
        return LogSender;                                                                                   //Name
    }

    public void flushRequestBuffer()throws IOException{
        if(!this.isHandshaked && !this.isHandshakeRequest()){
            throw new RuntimeException("Must send handshake request first!");
        }
        //Send Request to server
        this.convertToJson();                                                                               //Convert RequestMap to JsonObject
        System.out.print(this.RequestJson.toString()+"\n");                                                 //Debug Purposes
        byte Message[]=this.RequestJson.toString().getBytes();                                              //Convert Message to Unicode-8 Byte String
        this.SocketObject.getOutputStream().write(Message);                                                 //Send and flush()
        //this.SocketBuffer.write(Message);
        //this.SocketBuffer.flush();

    }
    public void buildHandShakeRequest() throws java.lang.RuntimeException{                                  //Build initial handshake request

        this.RequestMap.put("TYPE","SERVICE");                                                       //Type of service (Purpose of this wrapper)
        this.RequestMap.put("NAME",this.Name);                                                          //Nane given in constructor
        this.RequestMap.put("END","1");                                                              //END of message

    }

    public java.net.Socket getSocketObject()                                                               //getter for socket object
    {
        return this.SocketObject;
    }
    public java.util.Map<java.lang.String,java.lang.String> getRequestMap(){                               //getter for request map
        return this.RequestMap;
    }
    public void setRequestMap(java.util.Map<java.lang.String,java.lang.String> newRequestMap){
        this.RequestMap=newRequestMap;
    }
    private void convertToJson(){                                                                           //Convert Request map to json object
        this.RequestJson=new JSONObject(this.RequestMap);
    }
    public boolean isHandshakeRequest(){
        if(this.RequestMap.containsKey("TYPE") &&
                this.RequestMap.get("TYPE").equals("SERVICE") &&
                this.RequestMap.containsKey("NAME") &&
                this.RequestMap.containsKey("END")){
            return true;
        }
        return false;
    }




}


package com.NoReasonException.LogSolutionWrapper.LogObjects;
import com.NoReasonException.LogSolutionWrapper.LogSenderObjects.LogServerConnection;

import java.io.IOException;
import java.util.ArrayList;

public class Log {

    private java.lang.String Msg =null;
    private java.lang.String Type=null;
    Log(java.lang.String Type,java.lang.String Msg){
        this.Type=Type;
        this.Msg=Msg;
    }
    public void buildLogRequest(LogServerConnection conn) throws IOException{
        java.util.Map<java.lang.String,java.lang.String> LogRequestMap  = new java.util.HashMap<String, String>();
        LogRequestMap.put("LOG_TYPE",this.Type);
        LogRequestMap.put("MSG",this.Msg);
        conn.setRequestMap(LogRequestMap);

    }


}

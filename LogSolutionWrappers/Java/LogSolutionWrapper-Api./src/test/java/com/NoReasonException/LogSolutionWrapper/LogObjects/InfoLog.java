package com.NoReasonException.LogSolutionWrapper.LogObjects;

import com.NoReasonException.LogSolutionWrapper.LogSenderObjects.LogServerConnection;

public class InfoLog extends Log {

    public InfoLog(java.lang.String Msg){
        super("INFO",Msg);
    }
}

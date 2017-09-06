# LogSolution

A lot of projects , one place for all events

Welcome to LogSolution Project , The following guide will explain you the basic stuff you need to know about LogSolution

The LogSolution Hierarhy ...
Every Connected device , is a LISTENER or a SERVICE . Services send data and logs to server , and server serves theese logs to LISTENERS . You can watch your multiple programms running , all in one place .The Services isnt nessessary must all belong to the same programm , LogSolution is just a way of watch every event from all of projects in one place!

The LogSolution exchange protocol (Spec 0.0.1) 
When you connection passes from .accept() method , waits for a specific time for a proper first handshake . The first handshake is a simple JSON message following this form 

{
“TYPE”:”LISTENER” of “TYPE”:”SERVICE”,
“NAME”:”....”,
“END”:”1”
}

After HandShake , The Service can send logs via the following JSON form
{
“LOG_TYPE”:”DEBUG” or “INFO” or “ERROR”,
“MSG”:”...”
}

Project under develepoment

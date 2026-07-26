---
doc_id: "mta-wiki:2782"
title: "GetServerPort"
source_title: "GetServerPort"
source_url: "https://wiki.multitheftauto.com/wiki/GetServerPort"
revision_id: 43316
language: "en"
categories: ["Server_functions"]
---

# GetServerPort

This function retrieves the server's port.

## Syntax

```
int getServerPort ( )
```

### Returns

An integer corresponding to the server's port.

## Example

This example Sends out the serverPort when you type: /serverport

```
function outputServerPort ( )
        local serverPort = getServerPort() 
	outputChatBox (" Server Port: "..serverPort.." ") --Output Serverport in Chatbox
end
addCommandHandler ( "serverport", outputServerPort )  --add the command Handler
```

## See Also

- [getMaxPlayers](mta://scripting/server/functions/getmaxplayers.md)

- [getServerConfigSetting](mta://scripting/server/functions/getserverconfigsetting.md)

- [getServerHttpPort](mta://scripting/server/functions/getserverhttpport.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22890](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22890):

- [getServerIpFromMasterServer](mta://scripting/server/functions/getserveripfrommasterserver.md)

- [getServerName](mta://scripting/server/functions/getservername.md)

- [getServerPassword](mta://scripting/server/functions/getserverpassword.md)

- getServerPort

- [isGlitchEnabled](mta://scripting/server/functions/isglitchenabled.md)

- [setGlitchEnabled](mta://scripting/server/functions/setglitchenabled.md)

- [setMaxPlayers](mta://scripting/server/functions/setmaxplayers.md)

- [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

- [setServerPassword](mta://scripting/server/functions/setserverpassword.md)

- [shutdown](mta://scripting/server/functions/shutdown.md)

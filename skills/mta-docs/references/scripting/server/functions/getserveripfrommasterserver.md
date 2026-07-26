---
doc_id: "mta-wiki:14519"
title: "GetServerIpFromMasterServer"
source_title: "GetServerIpFromMasterServer"
source_url: "https://wiki.multitheftauto.com/wiki/GetServerIpFromMasterServer"
revision_id: 81677
language: "en"
categories: ["Server_functions", "Changes_in_1.6.0"]
---

# GetServerIpFromMasterServer

ADDED/UPDATED IN VERSION 1.6.0 [r22890](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22890):

This function returns the remote address as reported by the first master server that provides this value. 

| [[{{{image}}}\|link=\|]] | Note: It might take a while until the master server responds to the query sent out by the server, which in turn means that this function will not return any IP until the information has been received. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: On client-side there is the getServerIp function, in case you need the remote address of the currently connected server. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: If you want to retrieve the server IP address from the server configuration, then you should use getServerConfigSetting("serverip") , but this might yield only "auto" if the default value was used. |
| --- | --- |
|  |  |

## Syntax

```
string getServerIpFromMasterServer ( )
```

### Returns

A string containing the remote address of the server as reported, once it's available.

## Example

This example creates a console command that outputs the server's IP to the chatbox.

```
function outputServerIp()
    outputChatBox(getServerIpFromMasterServer())
end

addCommandHandler("serverIp", outputServerIp)
```

## See Also

- [getMaxPlayers](mta://scripting/server/functions/getmaxplayers.md)

- [getServerConfigSetting](mta://scripting/server/functions/getserverconfigsetting.md)

- [getServerHttpPort](mta://scripting/server/functions/getserverhttpport.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22890](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22890):

- getServerIpFromMasterServer

- [getServerName](mta://scripting/server/functions/getservername.md)

- [getServerPassword](mta://scripting/server/functions/getserverpassword.md)

- [getServerPort](mta://scripting/server/functions/getserverport.md)

- [isGlitchEnabled](mta://scripting/server/functions/isglitchenabled.md)

- [setGlitchEnabled](mta://scripting/server/functions/setglitchenabled.md)

- [setMaxPlayers](mta://scripting/server/functions/setmaxplayers.md)

- [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

- [setServerPassword](mta://scripting/server/functions/setserverpassword.md)

- [shutdown](mta://scripting/server/functions/shutdown.md)

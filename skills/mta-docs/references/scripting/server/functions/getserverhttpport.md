---
doc_id: "mta-wiki:4979"
title: "GetServerHttpPort"
source_title: "GetServerHttpPort"
source_url: "https://wiki.multitheftauto.com/wiki/GetServerHttpPort"
revision_id: 82646
language: "en"
categories: ["Server_functions"]
---

# GetServerHttpPort

This function retrieves the server's HTTP port.

## Syntax

```
int getServerHttpPort ( )
```

### Returns

An integer corresponding to the server's HTTP port.

## Example

This example outputs server's HTTP port to the chat box when player uses command *getHttpPort*

```
addCommandHandler("getHttpPort",
    function(player, command)
        outputChatBox("HTTP port of this server is: " .. getServerHttpPort(), player, 0, 255, 0)
    end
)
```

## See Also

- [getMaxPlayers](mta://scripting/server/functions/getmaxplayers.md)

- [getServerConfigSetting](mta://scripting/server/functions/getserverconfigsetting.md)

- getServerHttpPort

ADDED/UPDATED IN VERSION 1.6.0 [r22890](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22890):

- [getServerIpFromMasterServer](mta://scripting/server/functions/getserveripfrommasterserver.md)

- [getServerName](mta://scripting/server/functions/getservername.md)

- [getServerPassword](mta://scripting/server/functions/getserverpassword.md)

- [getServerPort](mta://scripting/server/functions/getserverport.md)

- [isGlitchEnabled](mta://scripting/server/functions/isglitchenabled.md)

- [setGlitchEnabled](mta://scripting/server/functions/setglitchenabled.md)

- [setMaxPlayers](mta://scripting/server/functions/setmaxplayers.md)

- [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

- [setServerPassword](mta://scripting/server/functions/setserverpassword.md)

- [shutdown](mta://scripting/server/functions/shutdown.md)

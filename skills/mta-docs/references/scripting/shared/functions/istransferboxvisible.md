---
doc_id: "mta-wiki:12673"
title: "IsTransferBoxVisible"
source_title: "IsTransferBoxVisible"
source_url: "https://wiki.multitheftauto.com/wiki/IsTransferBoxVisible"
revision_id: 81286
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# IsTransferBoxVisible

Determines if the transfer box is visible.

## Syntax

```
bool isTransferBoxVisible ( )
```

### Returns

On **server** this returns a boolean, whether the transfer box should be visible during downloads or not.

On **client** this returns a boolean, whether the transfer box should be visible or not at the time of invocation.

## Example

Click to collapse [-]
Client

This example defines a command to remove the player's transfer box.

```
function isVisible ()
    if isTransferBoxVisible () then 
        setTransferBoxVisible (false)
        outputChatBox ("* "..getPlayerName (localPlayer).." you are downloading the server!", 255, 255, 255, true)      
    end
end
addCommandHandler ("download2", isVisible)
```

## See Also

- [getMaxPlayers](mta://scripting/server/functions/getmaxplayers.md)

- [getServerConfigSetting](mta://scripting/server/functions/getserverconfigsetting.md)

- [getServerHttpPort](mta://scripting/server/functions/getserverhttpport.md)

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

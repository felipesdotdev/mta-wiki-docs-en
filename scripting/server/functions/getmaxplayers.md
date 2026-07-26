---
doc_id: "mta-wiki:1322"
title: "GetMaxPlayers"
source_title: "GetMaxPlayers"
source_url: "https://wiki.multitheftauto.com/wiki/GetMaxPlayers"
revision_id: 46696
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:15:15.502019+00:00"
---

# GetMaxPlayers

This function returns the maximum number of player slots on the server.

## Syntax

```
int getMaxPlayers ()
```

### Returns

Returns the maximum number of players allowed on the server.

## Example

This example outputs the current number of players together with the maximum number of players when a player joins.

```
function showPlayers()
	outputChatBox("There are "..getPlayerCount().."/"..getMaxPlayers().." players playing.",source) --output a message to the joined player informing the player count and max players.
end
addEventHandler("onPlayerJoin",root,showPlayers) --Add an event handler to call the function when a player joins.
```

## See Also

- getMaxPlayers

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

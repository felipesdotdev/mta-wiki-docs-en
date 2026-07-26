---
doc_id: "mta-wiki:12647"
title: "SetTransferBoxVisible"
source_title: "SetTransferBoxVisible"
source_url: "https://wiki.multitheftauto.com/wiki/SetTransferBoxVisible"
revision_id: 81281
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:16:45.859471+00:00"
---

# SetTransferBoxVisible

Determines whether or not the transfer box should appear to [players](mta://reference/misc/player.md).

## Syntax

```
bool setTransferBoxVisible ( bool visible )
```

### Required Arguments

- **visible:** The new transfer box visibility state.

### Returns

Returns *true* if the visibility was set successfully, *false* otherwise.

## Examples

Click to collapse [-]
Server

```
addEventHandler ("onResourceStart", resourceRoot, function()
    setTransferBoxVisible (false)
end)
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

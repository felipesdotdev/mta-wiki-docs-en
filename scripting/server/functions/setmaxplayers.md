---
doc_id: "mta-wiki:5835"
title: "SetMaxPlayers"
source_title: "SetMaxPlayers"
source_url: "https://wiki.multitheftauto.com/wiki/SetMaxPlayers"
revision_id: 63704
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:41.406084+00:00"
---

# SetMaxPlayers

This function sets the maximum number of player slots on the server.

| [[{{{image}}}\|link=\|]] | Note: This function cannot set more than <maxplayers> as defined in mtaserver.conf . (To find out the <maxplayers> value, use getServerConfigSetting("maxplayers")) |
| --- | --- |
|  |  |

## Syntax

```
bool setMaxPlayers ( int slots )
```

### Required Arguments

- **slots:** Maximum number of player slots on the server.

### Returns

Returns *true* if number of player slots was successfully changed, *false* or *nil* otherwise.

## Example

This example set server slots count to half value from current value.

```
local curMaxPlayers = getMaxPlayers()
local newMaxPlayers = math.ceil( curMaxPlayers / 2 )

setMaxPlayers( newMaxPlayers )
```

This example resets the server slots count to the value from mtaserver.conf

```
setMaxPlayers( tonumber( getServerConfigSetting("maxplayers") ) )
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

- setMaxPlayers

- [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

- [setServerPassword](mta://scripting/server/functions/setserverpassword.md)

- [shutdown](mta://scripting/server/functions/shutdown.md)

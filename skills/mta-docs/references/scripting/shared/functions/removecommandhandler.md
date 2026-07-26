---
doc_id: "mta-wiki:1577"
title: "RemoveCommandHandler"
source_title: "RemoveCommandHandler"
source_url: "https://wiki.multitheftauto.com/wiki/RemoveCommandHandler"
revision_id: 26331
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# RemoveCommandHandler

This function removes a command handler, that is one that has been added using [addCommandHandler](mta://scripting/shared/functions/addcommandhandler.md). This function can only remove command handlers that were added by the resource that it is called in.

## Syntax

```
bool removeCommandHandler ( string commandName [, function handler] )
```

### Required Arguments

- **commandName:** the name of the command you wish to remove.

### Optional Arguments

- **handler:** the specific handler function to remove. If not specified, all handler functions for the command (from the calling resource) will be removed. *This argument is only available in the server.*

### Returns

Returns *true* if the command handler was removed successfully, *false* if the command doesn't exist.

## Example

Click to collapse [-]
Server

This example adds a command handler that briefly shows the position of 'huntedPlayer', and removes the command handler when 'huntedPlayer' dies:

```
-- add a command that allows players to see the position of the 'huntedPlayer' for 5 seconds:
function consoleShowHuntedBlip ( thePlayer, commandName )
    local x, y, z = getElementPosition ( huntedPlayer )
    local huntedblip = createBlip ( x, y, z, 0, 2, 255, 0, 0, 255, thePlayer )
    setTimer ( "destroyElement", 5000, 1, huntedblip )
end
addCommandHandler ( "showhuntedblip", consoleShowHuntedBlip )

-- remove the command once the hunter player dies:
function onHuntedPlayerWasted ( ammo, killer, killerweapon, bodypart )
    removeCommandHandler ( "showhuntedblip" )
end
addEventHandler ( "onPlayerWasted", huntedPlayer, onHuntedPlayerWasted )
```

Click to collapse [-]
Client

This example adds a command handler that briefly shows the position of 'huntedPlayer', and removes the command handler when 'huntedPlayer' dies:

```
-- add a command that allows players to see the position of the 'huntedPlayer' for 5 seconds:
function consoleShowHuntedBlip ( commandName )
    local x, y, z = getElementPosition ( huntedPlayer )
    local huntedblip = createBlip ( x, y, z, 0, 2, 255, 0, 0, 255, thePlayer )
    setTimer ( "destroyElement", 5000, 1, huntedblip )
end
addCommandHandler ( "showhuntedblip", consoleShowHuntedBlip )

-- remove the command once the hunter player dies:
function onHuntedPlayerWasted ( killer, killerweapon, bodypart )
    removeCommandHandler ( "showhuntedblip" )
end
addEventHandler ( "onClientPlayerWasted", huntedPlayer, onHuntedPlayerWasted )
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

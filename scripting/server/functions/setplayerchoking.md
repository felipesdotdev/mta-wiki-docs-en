---
doc_id: "mta-wiki:3647"
title: "SetPlayerChoking"
source_title: "SetPlayerChoking"
source_url: "https://wiki.multitheftauto.com/wiki/SetPlayerChoking"
revision_id: 40593
language: "en"
categories: ["Server_functions", "Deprecated"]
generated_at: "2026-07-26T16:16:43.669205+00:00"
---

# SetPlayerChoking

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use setPedChoking instead. |  |

This function can be used to force the player to do the choking animation (teargas etc...) until he respawns or toggled off using this function. The animation can not be cancelled by the player and he will not loose health.

## Syntax

```
bool setPlayerChoking ( player thePlayer, bool choking )
```

### Required Arguments

- **thePlayer:** Define the player whose choking status to toggle

- **choking:** Use true to make the player choke, false to no longer force his choking animation

### Returns

Returns *true* if successful, *false* otherwise (e.g. player handle is invalid)

## Example

This script will make all players choke on resource start

```
-- Choke all the players when the resource starts
function ResourceStart ()
    setPlayerChoking ( root, true )
end
addEventHandler ( "onResourceStart", getResourceRootElement ( getThisResource () ), ResourceStart, true )

-- Unchoke all the players when the resource stops
function ResourceStop ()
    setPlayerChoking ( root, false )
end
addEventHandler ( "onResourceStop", getResourceRootElement ( getThisResource () ), ResourceStop, true )

-- Choke players spawning
function PlayerSpawn ()
    setPlayerChoking ( source, true )
end
addEventHandler ( "onPlayerSpawn", root, PlayerJoin )
```

## See Also

- [getPlayerTeam](mta://scripting/shared/functions/getplayerteam.md)

- [getPlayerBlurLevel](mta://scripting/shared/functions/getplayerblurlevel.md)

- [setPlayerBlurLevel](mta://scripting/shared/functions/setplayerblurlevel.md)

- [getPlayerSerial](mta://scripting/shared/functions/getplayerserial.md)

- [forcePlayerMap](mta://scripting/shared/functions/forceplayermap.md)

- [getPlayerScriptDebugLevel](mta://scripting/shared/functions/getplayerscriptdebuglevel.md)

- [getPlayerFromName](mta://scripting/shared/functions/getplayerfromname.md)

- [getPlayerMoney](mta://scripting/shared/functions/getplayermoney.md)

- [getPlayerName](mta://scripting/shared/functions/getplayername.md)

- [getPlayerNametagColor](mta://scripting/shared/functions/getplayernametagcolor.md)

- [getPlayerNametagText](mta://scripting/shared/functions/getplayernametagtext.md)

- [getPlayerPing](mta://scripting/shared/functions/getplayerping.md)

- [getPlayerWantedLevel](mta://scripting/shared/functions/getplayerwantedlevel.md)

- [givePlayerMoney](mta://scripting/shared/functions/giveplayermoney.md)

- [isPlayerMapForced](mta://scripting/shared/functions/isplayermapforced.md)

- [isPlayerNametagShowing](mta://scripting/shared/functions/isplayernametagshowing.md)

- [setPlayerHudComponentVisible](mta://scripting/shared/functions/setplayerhudcomponentvisible.md)

- [setPlayerMoney](mta://scripting/shared/functions/setplayermoney.md)

- [setPlayerNametagColor](mta://scripting/shared/functions/setplayernametagcolor.md)

- [setPlayerNametagShowing](mta://scripting/shared/functions/setplayernametagshowing.md)

- [setPlayerNametagText](mta://scripting/shared/functions/setplayernametagtext.md)

- [takePlayerMoney](mta://scripting/shared/functions/takeplayermoney.md)

- [countPlayersInTeam](mta://scripting/shared/functions/countplayersinteam.md)

- [getPlayersInTeam](mta://scripting/shared/functions/getplayersinteam.md)

- [isVoiceEnabled](mta://scripting/shared/functions/isvoiceenabled.md)

- [setControlState](mta://scripting/shared/functions/setcontrolstate.md)

- [getControlState](mta://scripting/shared/functions/getcontrolstate.md)

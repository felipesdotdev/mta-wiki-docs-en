---
doc_id: "mta-wiki:1564"
title: "SetPlayerRotation"
source_title: "SetPlayerRotation"
source_url: "https://wiki.multitheftauto.com/wiki/SetPlayerRotation"
revision_id: 40563
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated"]
---

# SetPlayerRotation

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use setElementRotation instead. |  |

This function allows you to set the current rotation of the specified player.

## Syntax

```
bool setPlayerRotation ( player thePlayer, float rotation )
```

### Required Arguments

- **thePlayer:** The [player](https://wiki.multitheftauto.com/index.php?search=player) to set the rotation of

- **rotation:** A [float](mta://reference/misc/float.md) specifying the desired rotation in degrees.

### Returns

Returns *true* if successful, *false* otherwise.

## Example

This example allows a player to type the command 'disco', which will result in the player being rotated to a random direction every 1 second, infinite times.

```
function discoTime ( player )
     -- Randomly choose a new player rotation and set it
     newRotation = math.random ( 0, 360 )
     setPlayerRotation ( player, newRotation )
end

function initiateDiscoMode ( player, commandName )
     --Trigger a random change in player rotation every second
     --Send the stored 'activating player' to the discoTime
     --function, so his rotation will be changed.
     setTimer (discoTime, 1000, 0, player )
end
addCommandHandler ( "disco", initiateDiscoMode )
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

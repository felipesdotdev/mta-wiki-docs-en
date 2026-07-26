---
doc_id: "mta-wiki:1333"
title: "GetPlayerOccupiedVehicleSeat"
source_title: "GetPlayerOccupiedVehicleSeat"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerOccupiedVehicleSeat"
revision_id: 44554
language: "en"
categories: ["Server_functions", "Deprecated"]
generated_at: "2026-07-26T16:15:20.230509+00:00"
---

# GetPlayerOccupiedVehicleSeat

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getPedOccupiedVehicleSeat instead. |  |

This function gets the seat that a specific player is sitting in in a vehicle.

## Syntax

```
int getPlayerOccupiedVehicleSeat ( player thePlayer )
```

### Required Arguments

- **thePlayer**: The [player](mta://reference/misc/player.md) whose vehicle seat you're looking up.

### Returns

Returns an integer containing the number of the seat that the player is currently in, if any. Returns *false* if the player is on foot, or the player doesn't exist.

## Example

This example finds what seat the player called 'someguy' is sitting in and outputs it to the chat box.

```
thePlayer = getPlayerFromNick ( "someguy" )
theVehicle = getPlayerOccupiedVehicle ( thePlayer )
if ( theVehicle ) then
    outputChatBox ( "someguy is in a vehicle in seat number " .. getPlayerOccupiedVehicleSeat ( thePlayer ) .. "." )
else
    outputChatBox ( "someguy is not in a vehicle." )
end
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

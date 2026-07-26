---
doc_id: "mta-wiki:2316"
title: "WarpPlayerIntoVehicle"
source_title: "WarpPlayerintoVehicle"
source_url: "https://wiki.multitheftauto.com/wiki/WarpPlayerintoVehicle"
revision_id: 49524
language: "en"
categories: ["Server_functions", "Deprecated", "Utility_templates"]
generated_at: "2026-07-26T16:17:06.332235+00:00"
---

# WarpPlayerIntoVehicle

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use warpPedIntoVehicle instead. |  |

This function is used to warp or force a player into a vehicle.  There are no animations involved when this happens.

## Syntax

```
bool warpPlayerIntoVehicle ( player thePlayer, vehicle theVehicle, [ int seat=0 ] )
```

### Required Arguments

- **thePlayer:** The player which you wish to force inside the vehicle

- **theVehicle:** The vehicle you wish to force the player into

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **seat:** An integer representing the seat ID. *0* represents the driver, any higher represent passenger seats.

### Returns

Returns *true* if the operation is successful, *false* otherwise.

## Example

This example creates a vehicle and warps a player inside immediately

```
function createstartvehicles ( playerSource, commandName, car, x, y, z ) -- the function allows specification of your car, and the position
    local racevehicle = createVehicle ( car, x, y, z )                   -- create a vehicle at the position specified by the startrace command
    warpPlayerIntoVehicle ( playerSource, racevehicle )                  -- warp them straight into the vehicle
end
addCommandHandler ( "startrace", createstartvehicles )                   -- add a command to start race
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

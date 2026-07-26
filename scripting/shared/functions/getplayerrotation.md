---
doc_id: "mta-wiki:1351"
title: "GetPlayerRotation"
source_title: "GetPlayerRotation"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerRotation"
revision_id: 44552
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated"]
generated_at: "2026-07-26T16:15:20.388800+00:00"
---

# GetPlayerRotation

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getElementRotation instead. |  |

This function returns the current rotation (in degrees) of a player around the Z axis. It's used with on-foot players: use [getVehicleRotation](mta://scripting/shared/functions/getvehiclerotation.md) on the occupied [vehicle](mta://reference/misc/vehicle.md) if the player is in one.

## Syntax

```
float getPlayerRotation ( player thePlayer )
```

### Required Arguments

- **thePlayer**: the [player](mta://reference/misc/player.md) whose rotation you want to retrieve.

### Returns

Returns a *float* containing the player's rotation, or *false* if an invalid player (or one in a vehicle) was passed.

## Example

This code adds a *getrot* command to get the player's current rotation.

```
function outputPlayerRotation ( sourcePlayer )
	-- if the command was triggered by an ingame player
	if ( sourcePlayer ) then
		-- if he is in a vehicle
		if isPlayerInVehicle ( sourcePlayer ) then
			-- store the vehicle element
			local playerVehicle = getPlayerOccupiedVehicle ( sourcePlayer )
			-- and output its rotation
			local x,y,z = getVehicleRotation ( playerVehicle )
			outputChatBox ( "Your vehicle's rotation is: " .. z, sourcePlayer )
		-- if he is on foot
		else
			-- output the player's rotation
			outputChatBox ( "Your rotation is: " .. getPlayerRotation ( sourcePlayer ), sourcePlayer )
		end
	end
end

-- register outputPlayerRotation as a handler for the getrot command
addCommandHandler ( "getrot", outputPlayerRotation )
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

---
doc_id: "mta-wiki:1670"
title: "IsPlayerInVehicle"
source_title: "IsPlayerInVehicle"
source_url: "https://wiki.multitheftauto.com/wiki/IsPlayerInVehicle"
revision_id: 40334
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated"]
generated_at: "2026-07-26T16:15:59.574544+00:00"
---

# IsPlayerInVehicle

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use isPedInVehicle instead. |  |

This function checks if a player is in a vehicle.

## Syntax

```
bool isPlayerInVehicle ( player thePlayer )
```

### Required Arguments

- **thePlayer**: The [player](mta://reference/misc/player.md) element you are checking.

### Returns

Returns *true* if the player is inside a vehicle, *false* if he isn't or an invalid player was passed.

## Example

This code defines an *isinvehicle* command which tells a player whether another player is in a vehicle or not.

```
-- we create our handler function, where sourcePlayer is the player who sent the command,
-- and checkedPlayerName is the player name specified.
function outputIsInVehicle ( sourcePlayer, commandName, checkedPlayerName )
	-- we get the player element from the nick specified
	local checkedPlayer = getPlayerFromNick ( checkedPlayerName )
	-- if it exists,
	if ( checkedPlayer ) then
		-- if it's in a vehicle,
		if isPlayerInVehicle ( checkedPlayer ) then
			-- tell the source player
			outputChatBox ( checkedPlayerName .. " is in a vehicle.", sourcePlayer )
		-- if it's not in a vehicle,
		else
			-- tell the source player
			outputChatBox ( checkedPlayerName .. " is not in a vehicle.", sourcePlayer )
		end
	-- if it doesn't exist,
	else
		-- tell the source player
		outputChatBox ( "Invalid player name.", sourcePlayer )
	end
end

-- define a handler for the isinvehicle command
addCommandHandler ( "isinvehicle", outputIsInVehicle )
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

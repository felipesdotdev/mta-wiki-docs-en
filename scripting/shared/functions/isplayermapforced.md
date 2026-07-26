---
doc_id: "mta-wiki:2284"
title: "IsPlayerMapForced"
source_title: "IsPlayerMapForced"
source_url: "https://wiki.multitheftauto.com/wiki/IsPlayerMapForced"
revision_id: 81390
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:59.611646+00:00"
---

# IsPlayerMapForced

This function checks if the specified player's map (F11) has been forced on or not.

## Syntax

Click to collapse [-]
Server

```
bool isPlayerMapForced ( player thePlayer )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](mta://reference/misc/player.md):isMapForced(...)*

**Variable**: *.mapForced*

**Counterpart**: *[forcePlayerMap](mta://scripting/shared/functions/forceplayermap.md)*

### Required Arguments

- **thePlayer:** A [player](mta://reference/misc/player.md) object referencing the specified player

### Returns

Returns *true* if the player's map is forced on, *false* otherwise.

Click to collapse [-]
Client

```
bool isPlayerMapForced ()
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Player](mta://reference/misc/player.md).isMapForced(...)*

**Counterpart**: *[forcePlayerMap](mta://scripting/shared/functions/forceplayermap.md)*

### Returns

Returns *true* if the local player's map is forced on, *false* otherwise.

## Example

Click to collapse [-]
Server

This example forces a player's map on for 10 seconds if it hasn't been already.

```
function forceMapForPlayer ( callingPlayer, command, whoNick )
	local who = getPlayerFromName ( whoNick )                                   -- Look up the specified player
	if ( who ) then
		if ( not isPlayerMapForced ( who ) ) then                           -- if their map isn't already forced on
			forcePlayerMap ( who, true )                                -- force it on
			setTimer ( forcePlayerMap, 10000, 1, who, false )           -- force it off in 10secs
			outputChatBox ( "Forcing Map for " .. whoNick, callingPlayer ) -- output a message to the one who entered the command
		else
			outputChatBox ( "Map already forced for " .. whoNick, callingPlayer ) -- if the map is already forced, output a message
		end
	else
		outputChatBox ( "Couldn't find " .. whoNick, callingPlayer )        -- if the player wasn't found, output a message
	end
end
addCommandHandler ( "forcemap", forceMapForPlayer ) -- add a command handler
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

- isPlayerMapForced

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

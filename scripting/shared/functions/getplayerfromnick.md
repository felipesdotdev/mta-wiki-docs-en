---
doc_id: "mta-wiki:1328"
title: "GetPlayerFromNick"
source_title: "GetPlayerFromNick"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerFromNick"
revision_id: 44621
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated"]
generated_at: "2026-07-26T16:15:19.563310+00:00"
---

# GetPlayerFromNick

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getPlayerFromName instead. |  |

This function returns a [player](mta://reference/misc/player.md) [element](mta://reference/misc/element.md) for the player with the name passed to the function.

## Syntax

```
player getPlayerFromNick ( string playerName )
```

### Required Arguments

- **playerName**: A string containing the name of the player you want to reference

### Returns

Returns a [player](mta://reference/misc/player.md) [element](mta://reference/misc/element.md) for the player with the nickname provided. If there is no player with that name, *false* is returned.

## Example

This example finds a [player](mta://reference/misc/player.md) as specified in the command and outputs the direction and distance he is from the player who entered the command. For example: 'locate someguy'.

```
function locatePlayer( sourcePlayer, command, who )
	local targetPlayer = getPlayerFromNick ( who )                -- find the player that was specified in the command
	if ( targetPlayer ) then                                      -- if a player was found
		local x,y,z = getElementPosition ( sourcePlayer )     -- save the position of the player who entered the command
		local xp,yp,zp = getElementPosition ( targetPlayer )  -- save the position of the player who should be located
		local dir = nil
		if (yp > y) then
			dir = "N"
		else
			dir = "S"
		end
		if (xp > x) then
			dir = dir .. "E"
		else
			dir = dir .. "W"
		end
		local distance = math.ceil ( getDistanceBetweenPoints3D(x, y, z, xp, yp, zp) )
		outputChatBox( who .. " found " .. dir .. " (" .. distance .. ")", sourcePlayer) -- output the message
	end
end
addCommandHandler ( "locate", locatePlayer )
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

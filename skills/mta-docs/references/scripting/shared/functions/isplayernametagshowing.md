---
doc_id: "mta-wiki:2386"
title: "IsPlayerNametagShowing"
source_title: "IsPlayerNametagShowing"
source_url: "https://wiki.multitheftauto.com/wiki/IsPlayerNametagShowing"
revision_id: 40792
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.0"]
---

# IsPlayerNametagShowing

This function will allow you to determine if a player's name tag is currently showing.

## Syntax

```
bool isPlayerNametagShowing ( player thePlayer )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](https://wiki.multitheftauto.com/index.php?search=player):isNametagShowing(...)*

**Variable**: *.nametagShowing*

**Counterpart**: *[setPlayerNametagShowing](mta://scripting/shared/functions/setplayernametagshowing.md)*

### Required Arguments

- **thePlayer:** The player whose current name tag condition you want to check

### Returns

Returns *true* if the player's name tag is being shown, *false* otherwise.

## Example

This example toggles a player's nametag. If no playername is given, it toggles the nametag of the player who entered the command.

```
function toggleNametag ( sourcePlayer, command, who )
	local tplayer = sourcePlayer                   -- by default, toggle the name tag of the player who issued the command
	if ( who ) then                                -- if there was a nick entered in the command
		tplayer = getPlayerFromName ( who )    -- search for the player
	else
		whoNick = getPlayerName(sourcePlayer)
	end
	if ( tplayer ~= false ) then                                -- if the player was found (or no playername was entered)
		if isPlayerNametagShowing ( tplayer ) then          -- if the nametag is shown
			setPlayerNametagShowing ( tplayer, false )  -- hide it
			outputChatBox ( who .. "'s nametag is now hidden", sourcePlayer )  -- output a message to the player who entered the command
		else                                                -- if the nametag is not shown
			setPlayerNametagShowing ( tplayer, true )   -- show it
			outputChatBox ( who .. "'s nametag is now showing", sourcePlayer ) -- output a message to the player who entered the command
		end
	else
		outputChatBox ( "Player not found.", sourcePlayer )
	end
end
addCommandHandler ( "toggleNametag", toggleNametag )
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

- isPlayerNametagShowing

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

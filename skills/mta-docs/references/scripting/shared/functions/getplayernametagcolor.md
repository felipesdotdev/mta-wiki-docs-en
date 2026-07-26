---
doc_id: "mta-wiki:2359"
title: "GetPlayerNametagColor"
source_title: "GetPlayerNametagColor"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerNametagColor"
revision_id: 46103
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetPlayerNametagColor

This function gets the current color of a player's name tag as RGB values. These are in the range 0-255.

## Syntax

```
int, int, int getPlayerNametagColor ( player thePlayer )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](https://wiki.multitheftauto.com/index.php?search=player):getNametagColor(...)*

**Counterpart**: *[setPlayerNametagColor](mta://scripting/shared/functions/setplayernametagcolor.md)*

### Required Arguments

- **thePlayer:** The player whose name tag RGB color values you wish to retrieve.

### Returns

Returns *red*, *green* and *blue* values if an existent player was specified, *false* otherwise.

## Example

Click to collapse [-]
Server

This console command will tell the player what his tag color is. The color is composed of a red, a green and a blue component, each ranging from 0-255.

```
function tagInfoCommand ( thePlayer, commandName )
	-- store the RGB data about the player who activated the command handler into the local variables r, g, b. 
	local r, g, b = getPlayerNametagColor ( thePlayer )
	-- Display the RGB values in the chatbox
	outputChatBox ( "Your tag color is: R:" .. r .. " G:" .. g .. " B:" .. b, thePlayer )
end
addCommandHandler ( "retrievetagcolor", tagInfoCommand )
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

- getPlayerNametagColor

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

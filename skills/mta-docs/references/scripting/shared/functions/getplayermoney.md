---
doc_id: "mta-wiki:1465"
title: "GetPlayerMoney"
source_title: "GetPlayerMoney"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerMoney"
revision_id: 63662
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetPlayerMoney

Returns the amount of money a player currently has.

| [[{{{image}}}\|link=\|]] | Note: The amount may vary between the server and client, you shouldn't trust the client side value to always be accurate. |
| --- | --- |
|  |  |

## Syntax

Click to collapse [-]
Server

```
int getPlayerMoney ( player thePlayer )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](https://wiki.multitheftauto.com/index.php?search=player):getMoney(...)*

**Variable**: *.money*

**Counterpart**: *[setPlayerMoney](mta://scripting/shared/functions/setplayermoney.md)*

### Required Arguments

- **thePlayer:** The player you wish the retrieve the amount of money from.

### Returns

Returns an integer with the amount of money the specified player has, *false* if the player is invalid.

Click to collapse [-]
Client

```
int getPlayerMoney ( )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Player](https://wiki.multitheftauto.com/index.php?search=Player).getMoney(...)*

**Counterpart**: *[setPlayerMoney](mta://scripting/shared/functions/setplayermoney.md)*

### Returns

Returns an integer with the amount of money the local player has.

## Example

Click to collapse [-]
Server

When a player types '/checkMoney' this example retrieves the player's money and outputs a message according to the value.

```
function checkMoney(thePlayer, command)
	local money = getPlayerMoney(thePlayer)                                -- get the amount of money from the player who entered the command
	if (money > 1000) then                                                 -- if money is more than 1000
		outputChatBox("You are rich: " .. tostring(money), thePlayer)  -- output this message together with the money
 	else
		outputChatBox("Poor guy...", thePlayer)                        -- and else, output this message
	end
end
addCommandHandler("checkMoney", checkMoney)                                    -- add the console command
```

## See Also

- [getPlayerTeam](mta://scripting/shared/functions/getplayerteam.md)

- [getPlayerBlurLevel](mta://scripting/shared/functions/getplayerblurlevel.md)

- [setPlayerBlurLevel](mta://scripting/shared/functions/setplayerblurlevel.md)

- [getPlayerSerial](mta://scripting/shared/functions/getplayerserial.md)

- [forcePlayerMap](mta://scripting/shared/functions/forceplayermap.md)

- [getPlayerScriptDebugLevel](mta://scripting/shared/functions/getplayerscriptdebuglevel.md)

- [getPlayerFromName](mta://scripting/shared/functions/getplayerfromname.md)

- getPlayerMoney

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

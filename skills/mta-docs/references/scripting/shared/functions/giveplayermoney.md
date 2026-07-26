---
doc_id: "mta-wiki:1463"
title: "GivePlayerMoney"
source_title: "GivePlayerMoney"
source_url: "https://wiki.multitheftauto.com/wiki/GivePlayerMoney"
revision_id: 72864
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GivePlayerMoney

This function adds money to a [player](https://wiki.multitheftauto.com/index.php?search=player)'s current money amount.  To set absolute values, [setPlayerMoney](mta://scripting/shared/functions/setplayermoney.md) can be used.

| [[{{{image}}}\|link=\|]] | Note: Using this function client side (not recommended) will not change a players money server side. |
| --- | --- |
|  |  |

## Syntax

Click to collapse [-]
Server

```
bool givePlayerMoney ( player thePlayer, int amount )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](https://wiki.multitheftauto.com/index.php?search=player):giveMoney(...)*

**Variable**: *.money*

### Required Arguments

- **thePlayer:** the [player](https://wiki.multitheftauto.com/index.php?search=player) you are giving the money to.

- **amount:** a positive integer number specifying the amount of money to give to the player.

Click to collapse [-]
Client

```
bool givePlayerMoney ( int amount )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Player](https://wiki.multitheftauto.com/index.php?search=Player).giveMoney(...)*

### Required Arguments

- **amount:** a positive integer number specifying the amount of money to give to the player.

### Returns

Returns *true* if the money was added, or *false* if invalid parameters were passed.

## Remarks

As of MTA SA version 1.5.9, despite the documentation claiming that **amount** should be a positive integer, this function does work with negative values or zero. In that case the function does still add the number to the game money value, in the negative case resulting in a decreased value.

## Example

Click to collapse [-]
Example 1 - Client and Server

This example gives a player money when using "givecash" command.

```
function consoleGiveCash ( thePlayer, command, amount ) --when the givecash command is called
	givePlayerMoney ( thePlayer, amount ) --give the player money according to the amount
end
addCommandHandler ( "givecash", consoleGiveCash  ) --add a handler function for the command "givecash"
```

Click to collapse [-]
Example 2 - Server

This example gives a player one thousand dollars, as a reward for killing another player.

```
function rewardOnWasted ( ammo, killer, killerweapon, bodypart )
	--if there is a killer, and that killer is not the same person as whoever died
	if ( killer ) and ( killer ~= source ) then 
		givePlayerMoney ( killer, 1000 ) --reward the killer with 1000 cash.
	end
end
addEventHandler ( "onPlayerWasted", root, rewardOnWasted ) --attach the rewardOnWasted function to the relevant event.
```

Click to collapse [-]
Example 3 - Server

This example Creates money Money (dollar symbol) pickup and gives 30,000 dollars on Pick up hit.

```
local money = createPickup (1896.4000244141, -1950.9000244141, 13, 3, 1274, 10000 )
function pickupUse ( player )
    givePlayerMoney ( player, 30000 )
end
addEventHandler ( "onPickupUse", money, pickupUse )
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

- givePlayerMoney

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

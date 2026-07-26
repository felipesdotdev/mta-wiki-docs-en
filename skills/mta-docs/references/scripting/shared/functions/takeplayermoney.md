---
doc_id: "mta-wiki:1464"
title: "TakePlayerMoney"
source_title: "TakePlayerMoney"
source_url: "https://wiki.multitheftauto.com/wiki/TakePlayerMoney"
revision_id: 43563
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# TakePlayerMoney

This function subtracts money from a [player](https://wiki.multitheftauto.com/index.php?search=player)'s current money amount.

| [[{{{image}}}\|link=\|]] | Note: Using this function client side (not recommended) will not change a players money server side. |
| --- | --- |
|  |  |

## Syntax

Click to collapse [-]
Server

```
bool takePlayerMoney ( player thePlayer, int amount )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](https://wiki.multitheftauto.com/index.php?search=player):takeMoney(...)*

**Variable**: *.money*

#### Required Arguments

- **thePlayer:** the [player](https://wiki.multitheftauto.com/index.php?search=player) you are taking the money from.

- **amount:** an integer number specifying the amount of money to take from the player.

Click to collapse [-]
Client

```
bool takePlayerMoney ( int amount )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Player](https://wiki.multitheftauto.com/index.php?search=Player).takeMoney(...)*

#### Required Arguments

- **amount:** an integer number specifying the amount of money to take from the player.

### Returns

Returns *true* if the money was taken, or *false* if invalid parameters were passed.

## Example

Click to collapse [-]
Server

This example takes money from a player when he types "takecash *number*" in the console.

```
function takeCash ( thePlayer, command, amount )     -- when the takecash command is called
     takePlayerMoney ( thePlayer, tonumber(amount) ) -- take the amount of money from the player
end
addCommandHandler ( "takecash", takeCash )           -- add a handler function for the command "takecash"
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

- takePlayerMoney

- [countPlayersInTeam](mta://scripting/shared/functions/countplayersinteam.md)

- [getPlayersInTeam](mta://scripting/shared/functions/getplayersinteam.md)

- [isVoiceEnabled](mta://scripting/shared/functions/isvoiceenabled.md)

- [setControlState](mta://scripting/shared/functions/setcontrolstate.md)

- [getControlState](mta://scripting/shared/functions/getcontrolstate.md)

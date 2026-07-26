---
doc_id: "mta-wiki:1462"
title: "SetPlayerMoney"
source_title: "SetPlayerMoney"
source_url: "https://wiki.multitheftauto.com/wiki/SetPlayerMoney"
revision_id: 75197
language: "en"
categories: ["Utility_templates", "Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:16:43.830972+00:00"
---

# SetPlayerMoney

Sets a player's money to a certain value, regardless of current player money. It should be noted that setting negative values does not work and in fact gives the player large amounts of money.

| [[{{{image}}}\|link=\|]] | Note: Using this function client side (not recommended) will not change a players money server side. |
| --- | --- |
|  |  |

## Syntax

Click to collapse [-]
Server

```
bool setPlayerMoney ( player thePlayer, int amount [, bool instant = false ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](mta://reference/misc/player.md):setMoney(...)*

**Variable**: *.money*

**Counterpart**: *[getPlayerMoney](mta://scripting/shared/functions/getplayermoney.md)*

### Required Arguments

- **thePlayer:** Which player to set the money of.

- **amount:** A whole integer specifying the new amount of money the player will have.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **instant:** If set to *true* money will be set instantly without counting up/down like in singleplayer.

Click to collapse [-]
Client

```
bool setPlayerMoney ( int amount [, bool instant = false ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Player](mta://reference/misc/player.md).setMoney(...)*

**Counterpart**: *[getPlayerMoney](mta://scripting/shared/functions/getplayermoney.md)*

### Required Arguments

- **amount:** A whole integer specifying the new amount of money the local player will have.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **instant:** If set to *true* money will be set instantly without counting up/down like in singleplayer.

### Returns

Returns *true* if the money was added, or *false* if invalid parameters were passed.

## Example

**Example 1:** This example sets the player's money to the desired amount when he types "setcash" in console.

```
function setCash(thePlayer, command, amount)       -- when the setcash function is called
    setPlayerMoney(thePlayer, tonumber(amount))    -- change player's money to the desired amount
end
addCommandHandler("setcash", setCash)           -- add a command handler for setcash
```

**Example 2:** This sets all players the amount of 1337 money when "leet" is typed in console.

```
function leetmoney()
	setPlayerMoney(root, 1337)
end
addCommandHandler("leet", leetmoney)
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

- setPlayerMoney

- [setPlayerNametagColor](mta://scripting/shared/functions/setplayernametagcolor.md)

- [setPlayerNametagShowing](mta://scripting/shared/functions/setplayernametagshowing.md)

- [setPlayerNametagText](mta://scripting/shared/functions/setplayernametagtext.md)

- [takePlayerMoney](mta://scripting/shared/functions/takeplayermoney.md)

- [countPlayersInTeam](mta://scripting/shared/functions/countplayersinteam.md)

- [getPlayersInTeam](mta://scripting/shared/functions/getplayersinteam.md)

- [isVoiceEnabled](mta://scripting/shared/functions/isvoiceenabled.md)

- [setControlState](mta://scripting/shared/functions/setcontrolstate.md)

- [getControlState](mta://scripting/shared/functions/getcontrolstate.md)

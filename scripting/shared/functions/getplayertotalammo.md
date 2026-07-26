---
doc_id: "mta-wiki:2363"
title: "GetPlayerTotalAmmo"
source_title: "GetPlayerTotalAmmo"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerTotalAmmo"
revision_id: 44589
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated"]
generated_at: "2026-07-26T16:15:20.646022+00:00"
---

# GetPlayerTotalAmmo

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getPedTotalAmmo instead. |  |

This function returns an integer that contains the total ammo in a specified [player](mta://reference/misc/player.md)'s weapon. See [Weapon Info](mta://reference/misc/weapon.md)

## Syntax

Click to collapse [-]
Server

```
int getPlayerTotalAmmo ( player thePlayer )
```

### Required Arguments

- **thePlayer**: The [player](mta://reference/misc/player.md) whose ammo you want to check.

### Returns

Returns an [int](mta://reference/misc/int.md) containing the total amount of ammo for the player's current weapon.

Click to collapse [-]
Client

```
int getPlayerTotalAmmo ( player thePlayer [, int weaponSlot = current ] )
```

### Required Arguments

- **thePlayer**: The [player](mta://reference/misc/player.md) whose ammo you want to check.

- **weaponSlot**: an integer representing the weapon slot (set to the players current slot if not given)

### Returns

Returns an [int](mta://reference/misc/int.md) containing the total amount of ammo for the specified player's weapon, or 0 if the player specified is invalid.

## Example

This example outputs the total amount of ammo a player called *Someguy* has for his weapon.

```
-- Find the player called 'Someguy'
myPlayer = getPlayerFromNick ( "Someguy" )
-- If a player called 'Someguy' was found then
if ( myPlayer ) then
	-- Retrieve the total amount of ammo for that player, and store it in a variable called 'ammo'
	ammo = getPlayerTotalAmmo ( myPlayer )
	-- Tell all the players how much ammo 'Someguy' has
	outputChatBox ( "Someguy's current total ammo: " .. ammo .. "." )
end
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

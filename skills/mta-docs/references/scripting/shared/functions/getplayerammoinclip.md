---
doc_id: "mta-wiki:2362"
title: "GetPlayerAmmoInClip"
source_title: "GetPlayerAmmoInClip"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerAmmoInClip"
revision_id: 44588
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated"]
---

# GetPlayerAmmoInClip

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getPedAmmoInClip instead. |  |

This function returns an integer that contains the ammo in a specified [player](https://wiki.multitheftauto.com/index.php?search=player)'s weapon. See [Weapon Info](https://wiki.multitheftauto.com/index.php?search=Weapon%20Info)

## Syntax

Click to collapse [-]
Server

```
int getPlayerAmmoInClip ( player thePlayer )
```

### Required Arguments

- **thePlayer:** The [player](https://wiki.multitheftauto.com/index.php?search=player) whose ammo you want to check.

### Returns

Returns an [int](mta://reference/misc/int.md) containing the amount of ammo in the player's currently selected clip, or 0 if the player specified is invalid.

Click to collapse [-]
Client

```
int getPlayerAmmoInClip ( player thePlayer, int weaponSlot )
```

### Required Arguments

- **thePlayer:** The [player](https://wiki.multitheftauto.com/index.php?search=player) whose ammo you want to check.

- **weaponSlot:** an integer representing the weapon slot.

### Returns

Returns an [int](mta://reference/misc/int.md) containing the amount of ammo in the specified player's currently selected or specified clip, or 0 if the player specified is invalid.

## Example

Click to collapse [-]
Server

This example outputs the amount of ammo the specified player has in his current slot. For example: 'ammo someguy'.

```
function showAmmo( thePlayer, command, who )
	local targetPlayer = getPlayerFromNick ( who )
	if ( thePlayer ) then
		local ammo = getPlayerAmmoInClip ( targetPlayer )
		outputChatBox ( who .. " has " .. ammo .. " ammo in his active clip", thePlayer )
	else
		outputChatBox ( "Player '" .. who .. "' not found.", thePlayer )
	end
end
addCommandHandler( "ammo", showAmmo )
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

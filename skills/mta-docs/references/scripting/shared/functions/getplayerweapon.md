---
doc_id: "mta-wiki:2388"
title: "GetPlayerWeapon"
source_title: "GetPlayerWeapon"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerWeapon"
revision_id: 40323
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated"]
---

# GetPlayerWeapon

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getPedWeapon instead. |  |

This function tells you which weapon type is in the player's current slot (clientside, you can optionally specify a slot other than the current one). See [Weapon Info](https://wiki.multitheftauto.com/index.php?search=Weapon%20Info)

## Syntax

Click to collapse [-]
Server

```
int getPlayerWeapon ( player thePlayer )
```

### Required Arguments

- **thePlayer**: the [player](https://wiki.multitheftauto.com/index.php?search=player) you want to get the weapon type from.

### Returns

Returns an [int](mta://reference/misc/int.md) indicating the type of the weapon the player has currently equipped.

Click to collapse [-]
Client

```
int getPlayerWeapon ( player thePlayer, [ int weaponSlot = current ] )
```

### Required Arguments

- **thePlayer**: the [player](https://wiki.multitheftauto.com/index.php?search=player) you want to get the weapon type from.

### Optional Arguments

- **weaponSlot**: an integer representing the weapon slot (set to the players current slot if not given).

### Returns

Returns an [int](mta://reference/misc/int.md) indicating the type of the weapon the player has in the specified slot.

It should be noted that if a player runs out of ammo for a weapon, it will still return the ID of that weapon in the slot (even if it appears as if the player does not have a weapon at all), though [getPlayerTotalAmmo](mta://scripting/shared/functions/getplayertotalammo.md) will return **0**.  Therefore, [getPlayerTotalAmmo](mta://scripting/shared/functions/getplayertotalammo.md) should be used in conjunction with getPlayerWeapon in order to check if a player has a weapon.

## Example

Click to collapse [-]
Example

This serverside example will display a player's current weapon type. In this case, it is hard coded to use the player called *someguy*.

```
-- Find a player called someguy and find his current weapon id.
local weaponType = getPlayerWeapon ( getPlayerFromNick ( "someguy" ) )
-- If a weapon type was returned then
if ( weaponType ) then
  outputChatBox ( "someguy's current Weapon-type: " .. weaponType .. "." ) -- Display the weapon type in the chat box
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

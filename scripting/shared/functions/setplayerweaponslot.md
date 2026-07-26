---
doc_id: "mta-wiki:2494"
title: "SetPlayerWeaponSlot"
source_title: "SetPlayerWeaponSlot"
source_url: "https://wiki.multitheftauto.com/wiki/SetPlayerWeaponSlot"
revision_id: 25630
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated"]
generated_at: "2026-07-26T16:16:44.188479+00:00"
---

# SetPlayerWeaponSlot

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions, but there should be a more generic way to perform what it does. |
| --- | --- |
|  |  |

Please use [setPedWeaponSlot](mta://scripting/shared/functions/setpedweaponslot.md)

This function sets the player's weapon slot. This affects the current weapon.

## Syntax

```
bool setPlayerWeaponSlot ( player theplayer, int weapon_slot )
```

### Required Arguments

- **theplayer:** the [player](mta://reference/misc/player.md) whose weapon slot you want to set. In a clientside script, this can only be the local player.

- **weapon_slot:** the weapon slot to set.

Weapon Slots

- **0:** WEAPONSLOT_TYPE_UNARMED

- **1:** WEAPONSLOT_TYPE_MELEE

- **2:** WEAPONSLOT_TYPE_HANDGUN

- **3:** WEAPONSLOT_TYPE_SHOTGUN

- **4:** WEAPONSLOT_TYPE_SMG (used for driveby's)

- **5:** WEAPONSLOT_TYPE_RIFLE

- **6:** WEAPONSLOT_TYPE_SNIPER

- **7:** WEAPONSLOT_TYPE_HEAVY

- **8:** WEAPONSLOT_TYPE_THROWN

- **9:** WEAPONSLOT_TYPE_SPECIAL

- **10:** WEAPONSLOT_TYPE_GIFT

- **11:** WEAPONSLOT_TYPE_PARACHUTE

- **12:** WEAPONSLOT_TYPE_DETONATOR

### Returns

Returns *true* if successful in setting the player's equipped weapon slot, *false* otherwise.

## Example

Click to collapse [-]
Server

This example allows the player to type the command 'giveweapons', which gives the player a weapon for every slot. Instead of equipping the last given weapon, the script randomly decides which weapon to equip after all the weapons are given.

```
function givePlayerWeapons ( player, commandName )
        --Give the player a weapon for each slot
	giveWeapon ( player, 1, 1 )
	giveWeapon ( player, 2, 1 )
	giveWeapon ( player, 22, 1 )
	giveWeapon ( player, 25, 1 )
	giveWeapon ( player, 28, 1 )
	giveWeapon ( player, 30, 1 )
	giveWeapon ( player, 33, 1 )
	giveWeapon ( player, 35, 1 )
	giveWeapon ( player, 16, 1 )
	giveWeapon ( player, 42, 1 )
	giveWeapon ( player, 10, 1 )
	giveWeapon ( player, 44, 1 )
	giveWeapon ( player, 40, 1 )
        --Randomly select which weapon to equip, slots 1 through 12
	setPlayerWeaponSlot ( player, math.random ( 1, 12) )
end
addCommandHandler ( "giveweapons", givePlayerWeapons )
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

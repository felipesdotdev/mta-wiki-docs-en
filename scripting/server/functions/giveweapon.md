---
doc_id: "mta-wiki:1457"
title: "GiveWeapon"
source_title: "GiveWeapon"
source_url: "https://wiki.multitheftauto.com/wiki/GiveWeapon"
revision_id: 80387
language: "en"
categories: ["Server_functions", "Utility_templates"]
generated_at: "2026-07-26T16:15:31.046731+00:00"
---

# GiveWeapon

giveWeapon gives a specified weapon to a certain player or ped. There is an optional argument to specify ammunition. For example, a melee weapon doesn't need an ammo argument.

| [[{{{image}}}\|link=\|]] | Note: When setting ammo for weapons in slot 0,1,10,11 or 12, the ammo max is 1 When setting ammo for weapons in slot 3,4,5, the ammo is added When setting ammo for weapons in slot 2,6,7,8,9 and the slot weapon is changing, the ammo is replaced |
| --- | --- |
|  |  |

## Syntax

```
bool giveWeapon ( ped thePlayer, int weapon [, int ammo=30, bool setAsCurrent=false ] )
```

### Required Arguments

- **thePlayer:** A [player](mta://reference/misc/player.md) or [ped](mta://reference/misc/ped.md) object referencing the specified player (or [ped](mta://reference/misc/ped.md))

- **weapon:** A whole number integer that refers to a [Weapon](mta://reference/misc/weapon.md) ID.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **ammo:** A whole number integer serving as the ammo amount for the given weapon.  For weapons that do not require ammo, such as melee, this should be at least 1.

- **setAsCurrent:** A boolean value determining whether or not the weapon will be set as the players current.

### Returns

Returns *true* if weapon was successfully acquired, *false* otherwise.

## Example

**Example 1:** This example gives a player an M4 with 200 ammo whenever they spawn.

```
function giveWeaponsOnSpawn ( theSpawnpont, theTeam )
    giveWeapon ( source, 31, 200 ) -- Gives the M4 weapon with 200 ammo
end
addEventHandler ( "onPlayerSpawn", root, giveWeaponsOnSpawn ) -- attach the event handler
```

**Example 2:** This example adds a "give" command in console which allows giving of any weapon by entering "give <id> <amount>".

```
function consoleGive ( thePlayer, commandName, weaponID, ammo )
	local status = giveWeapon ( thePlayer, weaponID, ammo, true )   -- attempt to give the weapon, forcing it as selected weapon
	if ( not status ) then                                          -- if it was unsuccessful
		outputConsole ( "Failed to give weapon.", thePlayer )   -- tell the player
	end
end
addCommandHandler ( "give", consoleGive )
```

**Example 3:** This example creates a ped in certain coordinates. You can give him a weapon with "give <weaponID> <amount>" command in console.

```
ped = createPed( 19, -1634.5775, 1203.85, 7.1796 )

addCommandHandler( "give",
  function ( player, command, id, amount )
    if not tonumber ( id ) then return end

    if not tonumber ( amount ) then
        amount = 9001
    end

    giveWeapon( ped, id, amount, true )
  end
)
```

## See Also

- giveWeapon

- [takeAllWeapons](mta://scripting/server/functions/takeallweapons.md)

- [takeWeapon](mta://scripting/server/functions/takeweapon.md)
  

- **Shared**

- [getWeaponProperty](mta://scripting/shared/functions/getweaponproperty.md)

- [getOriginalWeaponProperty](mta://scripting/shared/functions/getoriginalweaponproperty.md)

- [getSlotFromWeapon](mta://scripting/shared/functions/getslotfromweapon.md)

- [getWeaponIDFromName](mta://scripting/shared/functions/getweaponidfromname.md)

- [getWeaponNameFromID](mta://scripting/shared/functions/getweaponnamefromid.md)

- [setWeaponAmmo](mta://scripting/shared/functions/setweaponammo.md)

- [setWeaponProperty](mta://scripting/shared/functions/setweaponproperty.md)

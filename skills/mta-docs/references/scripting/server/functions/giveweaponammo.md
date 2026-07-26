---
doc_id: "mta-wiki:1631"
title: "GiveWeaponAmmo"
source_title: "GiveWeaponAmmo"
source_url: "https://wiki.multitheftauto.com/wiki/GiveWeaponAmmo"
revision_id: 67693
language: "en"
categories: ["Server_functions", "Deprecated"]
---

# GiveWeaponAmmo

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use giveWeapon instead. |  |

giveWeaponAmmo gives a specified ammount of ammo to a certain player, for a specified weapon (if they already have it).

## Syntax

```
bool giveWeaponAmmo ( player thePlayer, int weapon, int ammo )
```

### Required Arguments

- **thePlayer:** A [player](https://wiki.multitheftauto.com/index.php?search=player) object referencing the specified player

- **weapon:** A whole number integer that refers to a [weapon](https://wiki.multitheftauto.com/index.php?search=weapon) ID.

- **ammo:** A whole number integer serving as the ammo amount for the given weapon

## Returns

Returns a boolean value *true* or *false* that tells you if it was successful or not.

## Example

This example will give players an M4 weapon with 200 ammo followed by 5 more ammo when they spawn.

```
function scriptOnSpawnpointUse ( thePlayer )
    giveWeapon ( thePlayer, 31, 200 ) -- Gives the M4 weapon with 200 ammo to any player when they use a spawnpoint
    giveWeaponAmmo ( thePlayer, 31, 5 ) -- Gives the player 5 more ammo for the M4
end
addEventHandler ( "onSpawnpointUse", root, onSpawnpointUse )
```

## See Also

- [getWeaponProperty](mta://scripting/shared/functions/getweaponproperty.md)

- [getOriginalWeaponProperty](mta://scripting/shared/functions/getoriginalweaponproperty.md)

- [getSlotFromWeapon](mta://scripting/shared/functions/getslotfromweapon.md)

- [getWeaponIDFromName](mta://scripting/shared/functions/getweaponidfromname.md)

- [getWeaponNameFromID](mta://scripting/shared/functions/getweaponnamefromid.md)

- [setWeaponAmmo](mta://scripting/shared/functions/setweaponammo.md)

- [setWeaponProperty](mta://scripting/shared/functions/setweaponproperty.md)

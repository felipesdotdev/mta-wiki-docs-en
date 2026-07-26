---
doc_id: "mta-wiki:1784"
title: "TakeWeaponAmmo"
source_title: "TakeWeaponAmmo"
source_url: "https://wiki.multitheftauto.com/wiki/TakeWeaponAmmo"
revision_id: 67716
language: "en"
categories: ["Server_functions", "Deprecated"]
---

# TakeWeaponAmmo

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use takeWeapon instead. |  |

takeWeaponAmmo takes a specified amount of ammo from a certain player, for a specified weapon (if they already have it).

## Syntax

```
takeWeaponAmmo ( player thePlayer, int weapon, int ammo )
```

### Required Arguments

- **thePlayer:** A [player](https://wiki.multitheftauto.com/index.php?search=player) object referencing the specified player

- **weapon:** A whole number integer that refers to a [weapon](https://wiki.multitheftauto.com/index.php?search=weapon) ID.

- **ammo:** A whole number integer serving as the ammo amount for the given weapon

## Example

This example will give players an M4 weapon with 200 ammo followed by taking 5 ammo when they spawn.

```
function onSpawnpointUse ( thePlayer )
    giveWeapon ( thePlayer, 31, 200 )    -- Gives the M4 weapon with 200 ammo to any player when they use a spawnpoint
    takeWeaponAmmo ( thePlayer, 31, 5 )  -- Takes 5 ammo from the player's M4
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

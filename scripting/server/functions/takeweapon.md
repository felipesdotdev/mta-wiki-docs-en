---
doc_id: "mta-wiki:1367"
title: "TakeWeapon"
source_title: "TakeWeapon"
source_url: "https://wiki.multitheftauto.com/wiki/TakeWeapon"
revision_id: 80385
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:57.478499+00:00"
---

# TakeWeapon

This function removes a specified weapon or ammo from a certain player's inventory.

## Syntax

```
bool takeWeapon ( player thePlayer, int weaponId [, int ammo ] )
```

### Required Arguments

- **thePlayer**: A player object referencing the specified player.

- **weaponId**: An integer that refers to a [weapon](mta://reference/misc/weapon.md) that you wish to remove.

### Optional Arguments

- **ammo**: If used, this amount of ammo will be taken instead and the weapon will not be removed.

### Returns

Returns a *true* if the weapon/ammo was removed successfully, *false* otherwise.

## Example

This example removes teargas from player.

```
addCommandHandler( 'rtear',
  function( thePlayer )
    takeWeapon( thePlayer, 17 )
  end
)
```

## See Also

- [giveWeapon](mta://scripting/server/functions/giveweapon.md)

- [takeAllWeapons](mta://scripting/server/functions/takeallweapons.md)

- takeWeapon
  

- **Shared**

- [getWeaponProperty](mta://scripting/shared/functions/getweaponproperty.md)

- [getOriginalWeaponProperty](mta://scripting/shared/functions/getoriginalweaponproperty.md)

- [getSlotFromWeapon](mta://scripting/shared/functions/getslotfromweapon.md)

- [getWeaponIDFromName](mta://scripting/shared/functions/getweaponidfromname.md)

- [getWeaponNameFromID](mta://scripting/shared/functions/getweaponnamefromid.md)

- [setWeaponAmmo](mta://scripting/shared/functions/setweaponammo.md)

- [setWeaponProperty](mta://scripting/shared/functions/setweaponproperty.md)

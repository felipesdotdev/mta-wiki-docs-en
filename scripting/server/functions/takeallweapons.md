---
doc_id: "mta-wiki:1355"
title: "TakeAllWeapons"
source_title: "TakeAllWeapons"
source_url: "https://wiki.multitheftauto.com/wiki/TakeAllWeapons"
revision_id: 80386
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:57.399349+00:00"
---

# TakeAllWeapons

This function removes every weapons from a specified [ped](mta://reference/misc/ped.md), rendering it unarmed.

| [[{{{image}}}\|link=\|]] | Note: Weapons are removed when a ped dies by default. This means that it is only appropriate to use this function while a ped is alive. |
| --- | --- |
|  |  |

## Syntax

```
bool takeAllWeapons ( ped thePed )
```

### Required Arguments

- **thePed**: A [ped](mta://reference/misc/ped.md) element referencing the specified ped

### Returns

Returns *true* if the function succeeded, *false* otherwise.

## Example

This example removes all weapons from every player

```
takeAllWeapons ( root )  --remove all the weapons
outputChatBox ( "Weapons are not permitted!" ) --tell the players why they lost their weapons
```

## See Also

- [giveWeapon](mta://scripting/server/functions/giveweapon.md)

- takeAllWeapons

- [takeWeapon](mta://scripting/server/functions/takeweapon.md)
  

- **Shared**

- [getWeaponProperty](mta://scripting/shared/functions/getweaponproperty.md)

- [getOriginalWeaponProperty](mta://scripting/shared/functions/getoriginalweaponproperty.md)

- [getSlotFromWeapon](mta://scripting/shared/functions/getslotfromweapon.md)

- [getWeaponIDFromName](mta://scripting/shared/functions/getweaponidfromname.md)

- [getWeaponNameFromID](mta://scripting/shared/functions/getweaponnamefromid.md)

- [setWeaponAmmo](mta://scripting/shared/functions/setweaponammo.md)

- [setWeaponProperty](mta://scripting/shared/functions/setweaponproperty.md)

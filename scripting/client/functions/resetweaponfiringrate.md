---
doc_id: "mta-wiki:6722"
title: "ResetWeaponFiringRate"
source_title: "ResetWeaponFiringRate"
source_url: "https://wiki.multitheftauto.com/wiki/ResetWeaponFiringRate"
revision_id: 81129
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:34.303177+00:00"
---

# ResetWeaponFiringRate

This function resets the firing rate of a [custom weapon](mta://reference/misc/element-weapon.md) to the default one.

## Syntax

```
bool resetWeaponFiringRate ( weapon theWeapon )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[weapon](mta://reference/misc/element-weapon.md):resetFiringRate(...)*

### Required Arguments

- **theWeapon:** the weapon to reset the firing rate of.

### Returns

Returns *true* on success, *false* otherwise.

### Example

```
local weapon = createWeapon ("mp5",0,0,10) 
resetWeaponFiringRate (weapon)
```

## See also

- [createWeapon](mta://scripting/client/functions/createweapon.md)

- [fireWeapon](mta://scripting/client/functions/fireweapon.md)

- [getWeaponFiringRate](mta://scripting/client/functions/getweaponfiringrate.md)

- [getWeaponClipAmmo](mta://scripting/client/functions/getweaponclipammo.md)

- [getWeaponAmmo](mta://scripting/client/functions/getweaponammo.md)

- [getWeaponFlags](mta://scripting/client/functions/getweaponflags.md)

- [getWeaponState](mta://scripting/client/functions/getweaponstate.md)

- [getWeaponTarget](mta://scripting/client/functions/getweapontarget.md)

- resetWeaponFiringRate

- [setWeaponClipAmmo](mta://scripting/client/functions/setweaponclipammo.md)

- [setWeaponFiringRate](mta://scripting/client/functions/setweaponfiringrate.md)

- [setWeaponFlags](mta://scripting/client/functions/setweaponflags.md)

- [setWeaponState](mta://scripting/client/functions/setweaponstate.md)

- [setWeaponTarget](mta://scripting/client/functions/setweapontarget.md)

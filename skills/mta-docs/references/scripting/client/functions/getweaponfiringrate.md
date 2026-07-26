---
doc_id: "mta-wiki:6723"
title: "GetWeaponFiringRate"
source_title: "GetWeaponFiringRate"
source_url: "https://wiki.multitheftauto.com/wiki/GetWeaponFiringRate"
revision_id: 81130
language: "en"
categories: ["Client_functions"]
---

# GetWeaponFiringRate

This gets the firing rate to be used when a [custom weapon](mta://reference/misc/element-weapon.md) opens fire.

## Syntax

```
int getWeaponFiringRate ( weapon theWeapon )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[weapon](mta://reference/misc/element-weapon.md):getFiringRate(...)*

**Variable**: *.firingRate*

**Counterpart**: *[setWeaponFiringRate](mta://scripting/client/functions/setweaponfiringrate.md)*

### Required Arguments

- **theWeapon:** The weapon to modify the firing rate of.

### Returns

Returns an *integer* with the firing rate of the custom weapon, *false* otherwise.

## Example

This example creates a minigun at the center of the map and creates a */firerate* command that outputs its firerate to the player who types it.

```
local weapon = createWeapon("minigun", 0, 0, 3)

function outputMinigunFireRate()
    outputChatBox("Fire rate: " .. getWeaponFiringRate(weapon))
end
addCommandHandler("firerate", outputMinigunFireRate)
```

## See also

- [createWeapon](mta://scripting/client/functions/createweapon.md)

- [fireWeapon](mta://scripting/client/functions/fireweapon.md)

- getWeaponFiringRate

- [getWeaponClipAmmo](mta://scripting/client/functions/getweaponclipammo.md)

- [getWeaponAmmo](mta://scripting/client/functions/getweaponammo.md)

- [getWeaponFlags](mta://scripting/client/functions/getweaponflags.md)

- [getWeaponState](mta://scripting/client/functions/getweaponstate.md)

- [getWeaponTarget](mta://scripting/client/functions/getweapontarget.md)

- [resetWeaponFiringRate](mta://scripting/client/functions/resetweaponfiringrate.md)

- [setWeaponClipAmmo](mta://scripting/client/functions/setweaponclipammo.md)

- [setWeaponFiringRate](mta://scripting/client/functions/setweaponfiringrate.md)

- [setWeaponFlags](mta://scripting/client/functions/setweaponflags.md)

- [setWeaponState](mta://scripting/client/functions/setweaponstate.md)

- [setWeaponTarget](mta://scripting/client/functions/setweapontarget.md)

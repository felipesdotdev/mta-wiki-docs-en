---
doc_id: "mta-wiki:6724"
title: "SetWeaponFiringRate"
source_title: "SetWeaponFiringRate"
source_url: "https://wiki.multitheftauto.com/wiki/SetWeaponFiringRate"
revision_id: 81131
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:49.664868+00:00"
---

# SetWeaponFiringRate

This function sets the firing rate to be used when a [custom weapon](mta://reference/misc/element-weapon.md) is in *firing* state.

## Syntax

```
bool setWeaponFiringRate ( weapon theWeapon, int firingRate )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[weapon](mta://reference/misc/element-weapon.md):setFiringRate(...)*

**Variable**: *.firingRate*

**Counterpart**: *[getWeaponFiringRate](mta://scripting/client/functions/getweaponfiringrate.md)*

### Required Arguments

- **theWeapon:** The weapon to modify the firing rate of.

- **firingRate:** The weapon firing rate. It seems to be a kind of frecuency value, so the lower the quicker the [custom weapon](mta://reference/misc/element-weapon.md) will shoot.

### Returns

Returns *true* on success, *false* otherwise.

## Example

This example makes the Desert Eagle gun fire faster.

```
addEventHandler("onClientResourceStart", resourceRoot,
function()
   local weapon = createWeapon ("deagle",0,0,10) -- create the weapon (deagle)
   setWeaponAmmo(weapon,5000) -- set weapon ammo to 5000
   setWeaponState(weapon, "firing") -- in firing state.
   setWeaponFiringRate (weapon,2) -- change the weapon firing rate
end
)
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

- [resetWeaponFiringRate](mta://scripting/client/functions/resetweaponfiringrate.md)

- [setWeaponClipAmmo](mta://scripting/client/functions/setweaponclipammo.md)

- setWeaponFiringRate

- [setWeaponFlags](mta://scripting/client/functions/setweaponflags.md)

- [setWeaponState](mta://scripting/client/functions/setweaponstate.md)

- [setWeaponTarget](mta://scripting/client/functions/setweapontarget.md)

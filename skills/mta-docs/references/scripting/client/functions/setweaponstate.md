---
doc_id: "mta-wiki:6730"
title: "SetWeaponState"
source_title: "SetWeaponState"
source_url: "https://wiki.multitheftauto.com/wiki/SetWeaponState"
revision_id: 81137
language: "en"
categories: ["Client_functions"]
---

# SetWeaponState

This function sets a [custom weapon](mta://reference/misc/element-weapon.md)'s state.

## Syntax

```
bool setWeaponState ( weapon theWeapon, string theState )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[weapon](mta://reference/misc/element-weapon.md):setState(...)*

**Variable**: *.state*

**Counterpart**: *[getWeaponState](mta://scripting/client/functions/getweaponstate.md)*

### Required Arguments

- **theWeapon**: the weapon you wish to set the state of.

- **theState**: the state you wish to set:

- **reloading**: makes the weapon reload.

- **firing**: makes the weapon constantly fire its target (unless any shooting blocking flags are set) according to its assigned firing rate.

- **ready**: makes the weapon stop reloading or firing.

### Returns

Returns *true* on success, *false* otherwise.

### Example

```
addEventHandler("onClientResourceStart", resourceRoot,
      function()
            local wep = createWeapon("m4", 0, 0, 4)
            setWeaponState(wep, "firing")
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

- [setWeaponFiringRate](mta://scripting/client/functions/setweaponfiringrate.md)

- [setWeaponFlags](mta://scripting/client/functions/setweaponflags.md)

- setWeaponState

- [setWeaponTarget](mta://scripting/client/functions/setweapontarget.md)

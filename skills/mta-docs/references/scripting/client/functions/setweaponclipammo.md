---
doc_id: "mta-wiki:6720"
title: "SetWeaponClipAmmo"
source_title: "SetWeaponClipAmmo"
source_url: "https://wiki.multitheftauto.com/wiki/SetWeaponClipAmmo"
revision_id: 81128
language: "en"
categories: ["Client_functions"]
---

# SetWeaponClipAmmo

This function sets the ammo left in a [custom weapon](mta://reference/misc/element-weapon.md)'s magazine/clip.

## Syntax

```
bool setWeaponClipAmmo ( weapon theWeapon, int clipAmmo )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[weapon](mta://reference/misc/element-weapon.md):setClipAmmo(...)*

**Variable**: *.clipAmmo*

**Counterpart**: *[getWeaponClipAmmo](mta://scripting/client/functions/getweaponclipammo.md)*

### Required Arguments

- **theWeapon:** The [weapon](mta://reference/misc/element-weapon.md) to set the clip ammo of.

- **clipAmmo:** The amount of ammo in the clip.

### Returns

This function returns *true* if the arguments are valid and the weapon clip ammo could be changed; *false* otherwise.

## Example

This example adds a */weapon* command that creates a M4 where the player uses it, and gives 1 clip ammo to it.

```
function createWeaponWithLowClipAmmo()
	local wep = createWeapon("m4", getElementPosition(localPlayer))
	setWeaponClipAmmo(wep, 1) -- Give the weapon 1 clip ammo, so it will reload at the next shoot.
end
addCommandHandler("weapon", createWeaponWithLowClipAmmo)
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

- setWeaponClipAmmo

- [setWeaponFiringRate](mta://scripting/client/functions/setweaponfiringrate.md)

- [setWeaponFlags](mta://scripting/client/functions/setweaponflags.md)

- [setWeaponState](mta://scripting/client/functions/setweaponstate.md)

- [setWeaponTarget](mta://scripting/client/functions/setweapontarget.md)

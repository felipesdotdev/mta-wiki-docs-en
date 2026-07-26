---
doc_id: "mta-wiki:6727"
title: "SetWeaponOwner"
source_title: "SetWeaponOwner"
source_url: "https://wiki.multitheftauto.com/wiki/SetWeaponOwner"
revision_id: 81134
language: "en"
categories: ["Client_functions", "Disabled_Functions_and_Events"]
generated_at: "2026-07-26T16:16:49.705695+00:00"
---

# SetWeaponOwner

|  | Function has been disabled. |
| --- | --- |
| Reason/Note: This function was disabled in revision r4872 . |  |

This function sets the owner (which is a [player](mta://reference/misc/player.md)) of a [custom weapon](mta://reference/misc/element-weapon.md). The owner of a weapon was used for lag compensation, and it was also intended to only allow him to shoot the weapon.

## Syntax

```
bool setWeaponOwner ( weapon theWeapon, player theOwner )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This function is completely disabled, so it lacks a method.*

**Variable**: *.owner*

**Counterpart**: *[getWeaponOwner](mta://scripting/client/functions/getweaponowner.md)*

### Required Arguments

- **theWeapon:** The weapon to set the owner of.

- **theOwner:** The new weapon owner.

### Returns

Returns *true* on success, *false* otherwise.

## Example

```
--TODO
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

- [setWeaponState](mta://scripting/client/functions/setweaponstate.md)

- [setWeaponTarget](mta://scripting/client/functions/setweapontarget.md)

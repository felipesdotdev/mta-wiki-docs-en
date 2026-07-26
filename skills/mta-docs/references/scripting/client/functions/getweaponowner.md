---
doc_id: "mta-wiki:6728"
title: "GetWeaponOwner"
source_title: "GetWeaponOwner"
source_url: "https://wiki.multitheftauto.com/wiki/GetWeaponOwner"
revision_id: 81135
language: "en"
categories: ["Client_functions"]
---

# GetWeaponOwner

This function gets the owner of a [custom weapon](mta://reference/misc/element-weapon.md). Weapon ownership system was, however, disabled, so this function always returns *false*. Please refer to [setWeaponOwner](mta://scripting/client/functions/setweaponowner.md) for details.

## Syntax

```
bool getWeaponOwner ( weapon theWeapon )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *Pair is completely disabled at the moment (its value is*[nil](mta://reference/misc/nil.md)*).*

**Method**: *[weapon](mta://reference/misc/element-weapon.md):getOwner(...)*

**Variable**: *.owner*

**Counterpart**: *[setWeaponOwner](mta://scripting/client/functions/setweaponowner.md)*

### Required Arguments

- **theWeapon:** The weapon to get the owner of.

### Returns

This function was intended to return the [player](https://wiki.multitheftauto.com/index.php?search=player) which owns the [custom weapon](mta://reference/misc/element-weapon.md), and *false* if an error occured. However, at the moment it always returns *false*.

## Example

```
function arma()
	minigun = createWeapon("minigun", 1, 1, 3)--Create the weapon
	setWeaponClipAmmo(minigun, 99999)
        setWeaponState(minigun, "firing")
	setWeaponProperty(minigun, "fire_rotation", 0, -30, 0)
	dueno = getWeaponOwner(minigun)--This gets the owner
	outputChatBox(tostring(dueno))--And this say it in the chatbox
end
addCommandHandler("weapon", arma)--CommandHandler
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

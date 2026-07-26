---
doc_id: "mta-wiki:6773"
title: "GetWeaponState"
source_title: "GetWeaponState"
source_url: "https://wiki.multitheftauto.com/wiki/GetWeaponState"
revision_id: 81146
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:15:30.179996+00:00"
---

# GetWeaponState

This function gets the state of a [custom weapon](mta://reference/misc/element-weapon.md).

## Syntax

```
string getWeaponState ( weapon theWeapon )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[weapon](mta://reference/misc/element-weapon.md):getState(...)*

**Variable**: *.state*

**Counterpart**: *[setWeaponState](mta://scripting/client/functions/setweaponstate.md)*

### Required arguments

- **theWeapon:** the [weapon](mta://reference/misc/element-weapon.md) to get the state of.

### Returns

- A [string](mta://reference/misc/string.md) if the [weapon](mta://reference/misc/element-weapon.md) is valid, indicating the weapon state, which can be:

- **reloading**: the weapon is reloading.

- **firing**: the weapon is constantly shooting (unless any shooting blocking flags are set) according to its assigned firing rate.

- **ready**: the weapon is idle.

- *false* if an error occured or the [weapon](mta://reference/misc/element-weapon.md) is invalid.

## Example

This example creates a gun where the local player is and informs any player about its state.

```
local function testWeaponState()
    local weapon = createWeapon("m4", getElementPosition(localPlayer)) -- Create the weapon
    outputChatBox("The weapon that has just been created state is " .. getWeaponState(weapon) .. ".") -- Tell the player its state
end
addEventHandler("onClientResourceStart", resourceRoot, testWeaponState)
```

## See also

- [createWeapon](mta://scripting/client/functions/createweapon.md)

- [fireWeapon](mta://scripting/client/functions/fireweapon.md)

- [getWeaponFiringRate](mta://scripting/client/functions/getweaponfiringrate.md)

- [getWeaponClipAmmo](mta://scripting/client/functions/getweaponclipammo.md)

- [getWeaponAmmo](mta://scripting/client/functions/getweaponammo.md)

- [getWeaponFlags](mta://scripting/client/functions/getweaponflags.md)

- getWeaponState

- [getWeaponTarget](mta://scripting/client/functions/getweapontarget.md)

- [resetWeaponFiringRate](mta://scripting/client/functions/resetweaponfiringrate.md)

- [setWeaponClipAmmo](mta://scripting/client/functions/setweaponclipammo.md)

- [setWeaponFiringRate](mta://scripting/client/functions/setweaponfiringrate.md)

- [setWeaponFlags](mta://scripting/client/functions/setweaponflags.md)

- [setWeaponState](mta://scripting/client/functions/setweaponstate.md)

- [setWeaponTarget](mta://scripting/client/functions/setweapontarget.md)

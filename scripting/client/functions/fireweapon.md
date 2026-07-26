---
doc_id: "mta-wiki:6731"
title: "FireWeapon"
source_title: "FireWeapon"
source_url: "https://wiki.multitheftauto.com/wiki/FireWeapon"
revision_id: 81138
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:15:01.816787+00:00"
---

# FireWeapon

Fires one shot from a [custom weapon](mta://reference/misc/element-weapon.md).

## Syntax

```
bool fireWeapon ( weapon theWeapon )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[weapon](mta://reference/misc/element-weapon.md):fire(...)*

### Required Arguments

- **theWeapon:** The weapon to be fired.

### Returns

Returns *true* if the shot weapon is valid and therefore the shot was fired, *false* otherwise.

## Example

Click to collapse [-]
Example 1

This function creates and fires a weapon.

```
function createAndFire()
    local weaponElement = createWeapon("mp5", 0, 0, 3) -- Create a MP5 at the coordinates 0, 0, 3

    fireWeapon(weaponElement) -- Fire the weapon we spawned
end
addEventHandler("onClientResourceStart", resourceRoot, createAndFire)
```

Click to collapse [-]
Example 2

This example will create an M4, attach it to the local player and fire it every frame. Be aware that neither the weapon nor the shots are synced between players and that normally weapons don't fire every frame.

```
local weaponElement = nil

function onClientResourceStart()
	weaponElement = createWeapon("m4", 0, 0, 0) -- when the resource starts, create the M4 and attach it to the local player with an offset to place it above their head facing forwards
	attachElements(weaponElement, localPlayer, 0, 0, 1, 0, 0, 90)
end
addEventHandler("onClientResourceStart", resourceRoot, onClientResourceStart)

function onClientRender() -- fire the M4 every frame using the "onClientRender" event
	fireWeapon(weaponElement)
end
addEventHandler("onClientRender", root, onClientRender)
```

## See also

- [createWeapon](mta://scripting/client/functions/createweapon.md)

- fireWeapon

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

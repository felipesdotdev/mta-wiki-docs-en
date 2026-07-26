---
doc_id: "mta-wiki:6732"
title: "CreateWeapon"
source_title: "CreateWeapon"
source_url: "https://wiki.multitheftauto.com/wiki/CreateWeapon"
revision_id: 81139
language: "en"
categories: ["Client_functions"]
---

# CreateWeapon

Creates a [custom weapon](mta://reference/misc/element-weapon.md) that can fire bullets. **Do not confuse this with player held weapons**.

| [[{{{image}}}\|link=\|]] | Tip: Some weapons (such as the minigun) visually point to a slightly different direction to where they fire. To adjust this, use setWeaponProperty with 'fire_rotation'. See the example below. |
| --- | --- |
|  |  |

## Syntax

```
weapon createWeapon ( string theType, float x, float y, float z )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Weapon](mta://reference/misc/element-weapon.md)(...)*

### Required Arguments

- **theType:** The weapon type which can be:

- colt 45

- silenced

- deagle

- uzi

- mp5

- ak-47

- m4

- tec-9

- rifle

- sniper

- minigun

Other [weapons](mta://reference/misc/weapons.md) can be used but they can't fire. Use [createProjectile](mta://scripting/client/functions/createprojectile.md) for projectile based weapons.

- **x:** The x position to create the weapon.

- **y:** The y position to create the weapon.

- **z:** The z position to create the weapon.

### Returns

Returns a [custom weapon](mta://reference/misc/element-weapon.md) element, which represents a weapon floating at that position.

## Example

This example adds a */createminigun* command to create a weapon that is always firing.

```
function createMinigunWeapon()
    -- Create the weapon 1 meter above the player
    local x, y, z = getElementPosition(localPlayer)
    local weapon = createWeapon("minigun", x, y, z + 1)
    -- Give it some ammo and fire it
    setWeaponClipAmmo(weapon, 99999)
    setWeaponState(weapon, "firing")

    -- Optionally adjust for model rotation (this value will be different for other weapons)
    setWeaponProperty(weapon, "fire_rotation", 0, -30, 0)
end
addCommandHandler("createminigun", createMinigunWeapon)
```

## See also

- createWeapon

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

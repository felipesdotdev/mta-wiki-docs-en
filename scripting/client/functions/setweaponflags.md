---
doc_id: "mta-wiki:6726"
title: "SetWeaponFlags"
source_title: "SetWeaponFlags"
source_url: "https://wiki.multitheftauto.com/wiki/SetWeaponFlags"
revision_id: 81133
language: "en"
categories: ["Client_functions", "Functions_and_events_with_issues"]
generated_at: "2026-07-26T16:16:49.690580+00:00"
---

# SetWeaponFlags

This function sets a [custom weapon](mta://reference/misc/element-weapon.md) flags, used to change how it behaves or finds a possible target to shoot.

| [[{{{image}}}\|link=\|]] | Note: Do not confuse this function with setWeaponProperty . Although setWeaponProperty works with player-held weapons and custom weapons (in a limited extent), this function does not work with player-held weapons. |
| --- | --- |
|  |  |

## Syntax

```
bool setWeaponFlags ( weapon theWeapon, string theFlag, bool enable )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[weapon](mta://reference/misc/element-weapon.md):setFlags(...)*

**Counterpart**: *[getWeaponFlags](mta://scripting/client/functions/getweaponflags.md)*

### Required Arguments

- **theWeapon:** the [weapon element](mta://reference/misc/element-weapon.md) to set the flag of.

- **theFlag:** the weapon flag to change (all of them can be *true* or *false*):

- **disable_model**: makes the weapon and muzzle effect invisible or not.

- **flags**: configures the flags used to get where the gun shoots at. They are based on [processLineOfSight](mta://scripting/client/functions/processlineofsight.md)'s. You have to specify all the eight flags for the function to succeed. These flags are (by order):

- **checkBuildings**: allows the shoot to be blocked by GTA's internally placed buildings, i.e. the world map.

- **checkCarTires**: allows the shoot to be blocked by [vehicle](mta://reference/misc/vehicle.md) tires.

- **checkDummies**: allows the shoot to be blocked by GTA's internal dummies. These are not used in the current MTA version so this argument can be set to *false*.

- **checkObjects**: allows the shoot to be blocked by [objects](mta://reference/misc/object.md).

- **checkPeds**: allows the shoot to be blocked by [peds](mta://reference/misc/ped.md) and [players](mta://reference/misc/player.md).

- **checkVehicles**: allows the shoot to be blocked by [vehicles](mta://reference/misc/vehicle.md).

- **checkSeeThroughStuff**: allows the shoot to be blocked by translucent game objects, e.g. glass.

- **checkShootThroughStuff**: allows the shoot to be blocked by things that can be shot through.

- **instant_reload**: if enabled, the weapon will reload instantly rather than waiting the reload time until shooting again.

- **shoot_if_out_of_range**: if enabled, the weapon will still fire its target beyond the weapon range distance.

- **shoot_if_blocked**: if enabled, the weapon will still fire its target even if it's blocked by something.

- **enable**: whether to enable or disable the specified flag.

### Returns

Returns *true* if all arguments are valid and the flags where changed; *false* otherwise.

## Example

This example creates a minigun that will kill any player who approaches the center of the map, no matter if he takes cover or not.

```
local function setupDeadlyWeapon()
    local weapon = createWeapon("minigun", 0, 0, 10) -- Create the minigun
    setWeaponTarget(weapon, localPlayer) -- Set the weapon target to the local player
    setWeaponFlags(weapon, "flags", false, false, false, false, false, false, false, false) -- Allow the weapon to shoot through everything
end
addEventHandler("onClientResourceStart", resourceRoot, setupDeadlyWeapon)
```

## Issues

BEFORE VERSION 1.4.1 :

| Issue ID | Description |
| --- | --- |
| #8686 | setWeaponFlags(weapon, "flags") always returns false, but getWeaponFlags(weapon, "flags") works correctly |

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

- setWeaponFlags

- [setWeaponState](mta://scripting/client/functions/setweaponstate.md)

- [setWeaponTarget](mta://scripting/client/functions/setweapontarget.md)

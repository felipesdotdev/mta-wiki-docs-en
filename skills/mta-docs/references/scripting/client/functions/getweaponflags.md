---
doc_id: "mta-wiki:6725"
title: "GetWeaponFlags"
source_title: "GetWeaponFlags"
source_url: "https://wiki.multitheftauto.com/wiki/GetWeaponFlags"
revision_id: 81132
language: "en"
categories: ["Client_functions"]
---

# GetWeaponFlags

This function gets the flags of a [custom weapon](mta://reference/misc/element-weapon.md).

## Syntax

```
bool getWeaponFlags ( weapon theWeapon, string theFlag )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[weapon](mta://reference/misc/element-weapon.md):getFlags(...)*

**Counterpart**: *[setWeaponFlags](mta://scripting/client/functions/setweaponflags.md)*

### Required Arguments

- **theWeapon:** the weapon to get the flag of.

- **theFlag:** the weapon flag to get:

- **disable_model**: makes the weapon and muzzle effect invisible or not.

- **flags**: returns the flags used to get where the gun shoots at. These flags are (by order):

- **checkBuildings**: allows the shoot to be blocked by GTA's internally placed buildings, i.e. the world map.

- **checkCarTires**: allows the shoot to be blocked by [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle) tires.

- **checkDummies**: allows the shoot to be blocked by GTA's internal dummies. These are not used in the current MTA version so this argument can be set to *false*.

- **checkObjects**: allows the shoot to be blocked by [objects](https://wiki.multitheftauto.com/index.php?search=objects).

- **checkPeds**: allows the shoot to be blocked by [peds](https://wiki.multitheftauto.com/index.php?search=peds) and [players](https://wiki.multitheftauto.com/index.php?search=players).

- **checkVehicles**: allows the shoot to be blocked by [vehicles](https://wiki.multitheftauto.com/index.php?search=vehicles).

- **checkSeeThroughStuff**: allows the shoot to be blocked by translucent game objects, e.g. glass.

- **checkShootThroughStuff**: allows the shoot to be blocked by things that can be shot through.

- **instant_reload**: if enabled, the weapon reloads instantly rather than waiting the reload time until shooting again.

- **shoot_if_out_of_range**: if enabled, the weapon still fires its target beyond the weapon range distance.

- **shoot_if_blocked**: if enabled, the weapon still fires its target even if it's blocked by something.

### Returns

Returns the *true* or *false* on success (*flags* flag returns 8 values) if the flag is enabled or not. Returns *false* if the weapon element isn't valid or an error occured.

## Example

This example checks whether the instant_reload flag is enabled or disabled.

```
local weapon = createWeapon("silenced", 0, 0, 10) -- Create the weapon
if weapon then -- if the weapon exist then
   setWeaponFlags(weapon, "instant_reload", true) -- enable instant_reload
   local flag = (getWeaponFlags (weapon,"instant_reload") and "instant_reload enabled") or "instant_reload disabled"
   outputChatBox (flag)
end
```

## See also

- [createWeapon](mta://scripting/client/functions/createweapon.md)

- [fireWeapon](mta://scripting/client/functions/fireweapon.md)

- [getWeaponFiringRate](mta://scripting/client/functions/getweaponfiringrate.md)

- [getWeaponClipAmmo](mta://scripting/client/functions/getweaponclipammo.md)

- [getWeaponAmmo](mta://scripting/client/functions/getweaponammo.md)

- getWeaponFlags

- [getWeaponState](mta://scripting/client/functions/getweaponstate.md)

- [getWeaponTarget](mta://scripting/client/functions/getweapontarget.md)

- [resetWeaponFiringRate](mta://scripting/client/functions/resetweaponfiringrate.md)

- [setWeaponClipAmmo](mta://scripting/client/functions/setweaponclipammo.md)

- [setWeaponFiringRate](mta://scripting/client/functions/setweaponfiringrate.md)

- [setWeaponFlags](mta://scripting/client/functions/setweaponflags.md)

- [setWeaponState](mta://scripting/client/functions/setweaponstate.md)

- [setWeaponTarget](mta://scripting/client/functions/setweapontarget.md)

---
doc_id: "mta-wiki:2761"
title: "SetWeaponAmmo"
source_title: "SetWeaponAmmo"
source_url: "https://wiki.multitheftauto.com/wiki/SetWeaponAmmo"
revision_id: 81014
language: "en"
categories: ["Utility_templates", "Server_functions", "Client_functions"]
---

# SetWeaponAmmo

Click to collapse [-]
setWeaponAmmo

Sets the ammo to a certain amount for a specified weapon (if they already have it), regardless of current ammo.

## Syntax

```
bool setWeaponAmmo ( player thePlayer, int weapon, int totalAmmo [, int ammoInClip = 0 ] )
```

### Required Arguments

- **thePlayer:** A [player](https://wiki.multitheftauto.com/index.php?search=player) object referencing the specified player

- **weapon:** A whole number integer that refers to a [weapon](https://wiki.multitheftauto.com/index.php?search=weapon) ID.

- **totalAmmo:** A whole number integer serving as the total ammo amount for the given weapon (including ammo in clip).

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **ammoInClip:** The amount of ammo to set in the player's clip.  This will be taken from the main ammo.  If left unspecified or set to 0, the current clip will remain.

## Returns

Returns a boolean value *true* or *false* that tells you if it was successful or not.

## Example

```
local randPlayer = getRandomPlayer() -- Get a random player
giveWeapon(randPlayer,35,100) -- Give them a rocket launcher with 100 rockets.
setWeaponAmmo(randPlayer,35,50) -- Decide we're only going to give them 50 rockets.
```

Click to collapse [-]
setWeaponAmmo (custom weapons)

Set the ammo of a custom weapon which was created through [createWeapon](mta://scripting/client/functions/createweapon.md). By default, a custom weapon has 9999 ammo (which means infinite ammo).

## Syntax

```
bool setWeaponAmmo ( weapon theWeapon, int ammo )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[weapon](mta://reference/misc/element-weapon.md):setAmmo(...)*

**Variable**: *.ammo*

**Counterpart**: *[getWeaponAmmo](mta://scripting/client/functions/getweaponammo.md)*

### Required arguments

- **theWeapon:** The weapon to set the ammo of.

- **ammo:** The total ammo amount for the given weapon (including ammo in clip).

## Returns

Returns *true* on success, *false* otherwise.

## Example

```
local weapon = createWeapon ("deagle",0, 0, 10) -- Create the weapon
setWeaponAmmo(weapon,5000)
```

## See also

- [getWeaponProperty](mta://scripting/shared/functions/getweaponproperty.md)

- [getOriginalWeaponProperty](mta://scripting/shared/functions/getoriginalweaponproperty.md)

- [getSlotFromWeapon](mta://scripting/shared/functions/getslotfromweapon.md)

- [getWeaponIDFromName](mta://scripting/shared/functions/getweaponidfromname.md)

- [getWeaponNameFromID](mta://scripting/shared/functions/getweaponnamefromid.md)

- setWeaponAmmo

- [setWeaponProperty](mta://scripting/shared/functions/setweaponproperty.md)

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

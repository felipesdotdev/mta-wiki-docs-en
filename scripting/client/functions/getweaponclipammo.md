---
doc_id: "mta-wiki:6721"
title: "GetWeaponClipAmmo"
source_title: "GetWeaponClipAmmo"
source_url: "https://wiki.multitheftauto.com/wiki/GetWeaponClipAmmo"
revision_id: 50885
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:15:30.034294+00:00"
---

# GetWeaponClipAmmo

This function gets the amount of ammo left in a [custom weapon](mta://reference/misc/element-weapon.md)'s magazine/clip.

## Syntax

```
int getWeaponClipAmmo ( weapon theWeapon )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[weapon](mta://reference/misc/element-weapon.md):getClipAmmo(...)*

**Variable**: *.clipAmmo*

**Counterpart**: *[setWeaponClipAmmo](mta://scripting/client/functions/setweaponclipammo.md)*

### Required Arguments

- **theWeapon:** the [weapon](mta://reference/misc/weapon.md) to get the clip ammo of.

### Returns

Returns the amount of ammo in the [custom weapon](mta://reference/misc/element-weapon.md)'s clip, *false* if an error occured.

### Example

This function outputs the remaining ammo in clip of a specific weapon using the command */getammoinclip*.

```
local customWeapon

addEventHandler( "onClientResourceStart", resourceRoot,
    function()
        local x, y, z = getElementPosition(localPlayer) -- Get player position
        customWeapon = createWeapon("m4", x, y, z + 1) -- Create a M4
        setWeaponClipAmmo(customWeapon, 99999) -- Set the ammo in clip of the weapon to 99999, so it never should reload
        setWeaponState(customWeapon, "firing") -- Fire it permanently
        -- Add the 'getammoinclip' command to get the remaining ammo in clip of the weapon
        addCommandHandler("getammoinclip", getM4WeaponAmmo)
    end
)

function getM4WeaponAmmo()
    if customWeapon then
        -- Tell the player the remaining ammo in clip
        outputChatBox(getWeaponClipAmmo(customWeapon))
    else
        -- Weapon was not created, give an error
        outputChatBox("There is no weapon to get clip ammo of.")
    end
end
```

## See also

- [createWeapon](mta://scripting/client/functions/createweapon.md)

- [fireWeapon](mta://scripting/client/functions/fireweapon.md)

- [getWeaponFiringRate](mta://scripting/client/functions/getweaponfiringrate.md)

- getWeaponClipAmmo

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

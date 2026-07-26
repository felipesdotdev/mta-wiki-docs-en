---
doc_id: "mta-wiki:6719"
title: "GetWeaponAmmo"
source_title: "GetWeaponAmmo"
source_url: "https://wiki.multitheftauto.com/wiki/GetWeaponAmmo"
revision_id: 81127
language: "en"
categories: ["Client_functions"]
---

# GetWeaponAmmo

This function gets the total ammo a [custom weapon](mta://reference/misc/element-weapon.md) has.

## Syntax

```
int getWeaponAmmo ( weapon theWeapon )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[weapon](mta://reference/misc/element-weapon.md):getAmmo(...)*

**Variable**: *.ammo*

**Counterpart**: *[setWeaponAmmo](mta://scripting/shared/functions/setweaponammo.md)*

### Required arguments

- **theWeapon**: The weapon to get the ammo of.

### Returns

Returns an [integer](mta://reference/misc/int.md) containing how many ammo left has the weapon. Returns *false* if an error occured.

## Example

This example gets the ammo of the custom weapon and outputs it to the chatbox.

```
function createCustomWeapon()
   local position = Vector3(getElementPosition(localPlayer)) -- get the localPlayer position
   local weapon = createWeapon ("m4",position.x,position.y,position.z) -- Create the weapon
     if weapon then -- If the weapon exist then
       setWeaponAmmo(weapon,5000) 
       local ammo = getWeaponAmmo(weapon)  
       outputChatBox("Total ammo: "..ammo) -- output to the chatbox
    end 
end 
addCommandHandler("weapon",createCustomWeapon)
```

## See also

- [createWeapon](mta://scripting/client/functions/createweapon.md)

- [fireWeapon](mta://scripting/client/functions/fireweapon.md)

- [getWeaponFiringRate](mta://scripting/client/functions/getweaponfiringrate.md)

- [getWeaponClipAmmo](mta://scripting/client/functions/getweaponclipammo.md)

- getWeaponAmmo

- [getWeaponFlags](mta://scripting/client/functions/getweaponflags.md)

- [getWeaponState](mta://scripting/client/functions/getweaponstate.md)

- [getWeaponTarget](mta://scripting/client/functions/getweapontarget.md)

- [resetWeaponFiringRate](mta://scripting/client/functions/resetweaponfiringrate.md)

- [setWeaponClipAmmo](mta://scripting/client/functions/setweaponclipammo.md)

- [setWeaponFiringRate](mta://scripting/client/functions/setweaponfiringrate.md)

- [setWeaponFlags](mta://scripting/client/functions/setweaponflags.md)

- [setWeaponState](mta://scripting/client/functions/setweaponstate.md)

- [setWeaponTarget](mta://scripting/client/functions/setweapontarget.md)

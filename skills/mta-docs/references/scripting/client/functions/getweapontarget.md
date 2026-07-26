---
doc_id: "mta-wiki:6772"
title: "GetWeaponTarget"
source_title: "GetWeaponTarget"
source_url: "https://wiki.multitheftauto.com/wiki/GetWeaponTarget"
revision_id: 81145
language: "en"
categories: ["Client_functions"]
---

# GetWeaponTarget

This functions gets the target of a [custom weapon](mta://reference/misc/element-weapon.md).

## Syntax

```
nil/element/float getWeaponTarget ( weapon theWeapon )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *Variable is read only.*

**Method**: *[weapon](mta://reference/misc/element-weapon.md):getTarget(...)*

**Variable**: *.target*

**Counterpart**: *[setWeaponTarget](mta://scripting/client/functions/setweapontarget.md)*

### Required Arguments

- **theWeapon:** The weapon to get the target of.

### Returns

- Returns the *target* of the [custom weapon](mta://reference/misc/element-weapon.md), which can be:

- *[nil](mta://reference/misc/nil.md)* if the weapon is in rotation based targeting.

- 3 [floats](mta://reference/misc/float.md) if the weapon is firing at a fixed point.

- an [element](mta://reference/misc/element.md) if the weapon is firing an entity.

- Returns *false* if the weapon element is not valid.

## Example

This example gets the weapon target when the player hit the colshape and outputs it to the chatbox.

```
local col = createColSphere(1647.33984375,1785.03125,10.671875,8) -- Create col sphere near to LV hospital
local weapon = createWeapon ("m4",1647.33984375,1785.03125,10.671875) -- Create the weapon

function onClientColShapeHit(element, matchDim )
   if (element == getLocalPlayer()) then  -- Checks whether the entering element is the local player 
     if weapon then -- if the weapon exist then
        setWeaponTarget (weapon,element,8) -- Set the weapon target to the localPlayer 
        local target = getWeaponTarget (weapon) -- get weapon target
          if target and isElement(target) and getElementType(target) == "player" then 
            outputChatBox("The target of the custom weapon: "..getPlayerName(target)) -- output to the chatbox
          end 
       end 
    end 
end
addEventHandler("onClientColShapeHit",col,onClientColShapeHit)
```

## See also

- [createWeapon](mta://scripting/client/functions/createweapon.md)

- [fireWeapon](mta://scripting/client/functions/fireweapon.md)

- [getWeaponFiringRate](mta://scripting/client/functions/getweaponfiringrate.md)

- [getWeaponClipAmmo](mta://scripting/client/functions/getweaponclipammo.md)

- [getWeaponAmmo](mta://scripting/client/functions/getweaponammo.md)

- [getWeaponFlags](mta://scripting/client/functions/getweaponflags.md)

- [getWeaponState](mta://scripting/client/functions/getweaponstate.md)

- getWeaponTarget

- [resetWeaponFiringRate](mta://scripting/client/functions/resetweaponfiringrate.md)

- [setWeaponClipAmmo](mta://scripting/client/functions/setweaponclipammo.md)

- [setWeaponFiringRate](mta://scripting/client/functions/setweaponfiringrate.md)

- [setWeaponFlags](mta://scripting/client/functions/setweaponflags.md)

- [setWeaponState](mta://scripting/client/functions/setweaponstate.md)

- [setWeaponTarget](mta://scripting/client/functions/setweapontarget.md)

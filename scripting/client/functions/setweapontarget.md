---
doc_id: "mta-wiki:6729"
title: "SetWeaponTarget"
source_title: "SetWeaponTarget"
source_url: "https://wiki.multitheftauto.com/wiki/SetWeaponTarget"
revision_id: 81136
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:49.833080+00:00"
---

# SetWeaponTarget

This function sets the target of a [custom weapon](mta://reference/misc/element-weapon.md). There are 3 different targeting modes, which are explained below.

| [[{{{image}}}\|link=\|]] | Note: Custom weapons fire targets with no recoil (so they never miss a shot). If you want a custom weapon to take into account recoil, you will have to script it by firing at fixed coordinates. |
| --- | --- |
|  |  |

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *Variable is read only.*

**Method**: *[weapon](mta://reference/misc/element-weapon.md):setTarget(...)*

**Variable**: *.target*

**Counterpart**: *[getWeaponTarget](mta://scripting/client/functions/getweapontarget.md)*

## Syntax (target an element)

Fires the weapon at a physical [element](mta://reference/misc/element.md).

```
bool setWeaponTarget ( weapon theWeapon, element theTarget [, int theComponent = 255 ] )
```

### Required arguments

- **theWeapon:** The weapon to set the target of.

- **theTarget:** The [element](mta://reference/misc/element.md) to shoot at. It can be a [player](mta://reference/misc/player.md), [ped](mta://reference/misc/ped.md), [vehicle](mta://reference/misc/vehicle.md) or [object](mta://reference/misc/object.md).

### Optional arguments

- **theComponent:** The component of the target to shoot at. This argument is only relevant when used in the following element types:

- **[Vehicles](mta://reference/misc/vehicle.md)**:

- **0**: front left tire.

- **1**: front right tire.

- **2**: rear left tire.

- **3**: rear right tire.

- **255**: center of the car (position returned by [getElementPosition](mta://scripting/shared/functions/getelementposition.md)).

- **[Peds](mta://reference/misc/ped.md)** (players **not** included; see [getPedBonePosition](mta://scripting/client/functions/getpedboneposition.md) to know where each bone is located):

- **1:** *BONE_PELVIS1* position.

- **2:** *BONE_PELVIS* position.

- **3:** *BONE_SPINE1* position.

- **4:** *BONE_UPPERTORSO* position.

- **5:** *BONE_NECK* position.

- **6:** *BONE_HEAD2* position.

- **7:** *BONE_HEAD1* position.

- **8:** *BONE_HEAD* position.

- **21:** *BONE_RIGHTUPPERTORSO* position.

- **22:** *BONE_RIGHTSHOULDER* position.

- **23:** *BONE_RIGHTELBOW* position.

- **24:** *BONE_RIGHTWRIST* position.

- **25:** *BONE_RIGHTHAND* position.

- **26:** *BONE_RIGHTTHUMB* position.

- **31:** *BONE_LEFTUPPERTORSO* position.

- **32:** *BONE_LEFTSHOULDER* position.

- **33:** *BONE_LEFTELBOW* position.

- **34:** *BONE_LEFTWRIST* position.

- **35:** *BONE_LEFTHAND* position.

- **36:** *BONE_LEFTTHUMB* position.

- **41:** *BONE_LEFTHIP* position.

- **42:** *BONE_LEFTKNEE* position.

- **43:** *BONE_LEFTANKLE* position.

- **44:** *BONE_LEFTFOOT* position.

- **51:** *BONE_RIGHTHIP* position.

- **52:** *BONE_RIGHTKNEE* position.

- **53:** *BONE_RIGHTANKLE* position.

- **54:** *BONE_RIGHTFOOT* position.

- **255**: center of the ped (position returned by [getElementPosition](mta://scripting/shared/functions/getelementposition.md)).

### Returns

Returns *true* on success, *false* otherwise.

## Syntax (target a position)

Fires the weapon at the specified position.

```
bool setWeaponTarget ( weapon theWeapon, float targetX, float targetY, float targetZ )
```

### Required arguments

- **theWeapon:** The weapon to set the target of.

- **targetX:** The target X.

- **targetY:** The target Y.

- **targetZ:** The target Z.

### Returns

Returns *true* on success, *false* otherwise.

## Syntax (rotational target)

Sets the weapon back to rotation based targeting. It will fire to its front.

```
bool setWeaponTarget ( weapon theWeapon, nil )
```

### Required arguments

- **theWeapon:** The weapon to clear the target of.

### Returns

Returns *true* on success, *false* otherwise.

## Example

This example creates a Uzi and a pedestrian in the center of the map when the resource which contains it starts and makes the weapon fire the new ped's head non-stop.

```
local function createWeaponFiringPedHead()
    -- Create the weapon and set a flag of it
    local weapon = createWeapon("uzi", 0, 0, 10)
    setWeaponFlags(weapon, "instant_reload", true)
    -- Set the weapon target to a ped and fire it forever
    setWeaponTarget(weapon, createPed(8, 0, 0, 5), 8)
    setWeaponState(weapon, "firing")
end
addEventHandler("onClientResourceStart", resourceRoot, createWeaponFiringPedHead)
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

- setWeaponTarget

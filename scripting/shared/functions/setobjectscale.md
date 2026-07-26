---
doc_id: "mta-wiki:3370"
title: "SetObjectScale"
source_title: "SetObjectScale"
source_url: "https://wiki.multitheftauto.com/wiki/SetObjectScale"
revision_id: 75462
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:16:41.745259+00:00"
---

# SetObjectScale

This function changes the visible size of an object.

| [[{{{image}}}\|link=\|]] | Note: setObjectScale does not affect the collision models for the object, as such is unsuitable for use for interaction with players, vehicles or other objects. |
| --- | --- |
|  |  |

## Syntax

```
bool setObjectScale ( object theObject, float scale [, float scaleY = scale, float scaleZ = scale ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[object](mta://reference/misc/object.md):setScale(...)*

**Variable**: *.scale*

**Counterpart**: *[getObjectScale](mta://scripting/shared/functions/getobjectscale.md)*

### Required Arguments

- **theObject**: the [object](mta://reference/misc/object.md) you wish to change the scale of.

- **scale**: a float containing the new scale. 1.0 is the standard scale, with 0.5 being half the size and 2.0 being twice the size. If the scaleY is set, this will be scaleX.

### Optional Arguments

- **scaleY**: a float containing the new scale on the Y axis

- **scaleZ**: a float containing the new scale on the Z axis

### Returns

- *true* if the scale was set properly.

- *false* otherwise.

## Example

This example creates an antenna, and changes the size of it.

Click to collapse [-]
Client

```
-- Get the position of the player

local x, y, z = getElementPosition(localPlayer)

-- Create the object

local antennaObject = createObject(1595, x + 2, y, z)

if antennaObject then -- If it was created
	-- Set the scale to half the normal scale

	setObjectScale(antennaObject, 0.5)

	-- Remove the collision

	setElementCollisionsEnabled(antennaObject, false)
end
```

## See Also

- [createObject](mta://scripting/shared/functions/createobject.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22489](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22489):

- [breakObject](mta://scripting/shared/functions/breakobject.md)

- [getObjectScale](mta://scripting/shared/functions/getobjectscale.md)

- [moveObject](mta://scripting/shared/functions/moveobject.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22708](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22708):

- [respawnObject](mta://scripting/shared/functions/respawnobject.md)

- [toggleObjectRespawn](mta://scripting/shared/functions/toggleobjectrespawn.md)

- [isObjectRespawnable](mta://scripting/shared/functions/isobjectrespawnable.md)

- setObjectScale

ADDED/UPDATED IN VERSION 1.6.0 [r22430](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22430):

- [isObjectMoving](mta://scripting/shared/functions/isobjectmoving.md)

ADDED/UPDATED IN VERSION 1.6.0 [r21765](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21765):

- [isObjectBreakable](mta://scripting/shared/functions/isobjectbreakable.md)

- [setObjectBreakable](mta://scripting/shared/functions/setobjectbreakable.md)

- [stopObject](mta://scripting/shared/functions/stopobject.md)

- [getObjectMass](mta://scripting/client/functions/getobjectmass.md)

- [getObjectProperty](mta://scripting/client/functions/getobjectproperty.md)

- [setObjectMass](mta://scripting/client/functions/setobjectmass.md)

- [setObjectProperty](mta://scripting/client/functions/setobjectproperty.md)

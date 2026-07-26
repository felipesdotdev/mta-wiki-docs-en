---
doc_id: "mta-wiki:10971"
title: "GetObjectProperty"
source_title: "GetObjectProperty"
source_url: "https://wiki.multitheftauto.com/wiki/GetObjectProperty"
revision_id: 72969
language: "en"
categories: ["Client_functions", "Changes_in_1.5.6"]
generated_at: "2026-07-26T16:15:16.229075+00:00"
---

# GetObjectProperty

This function gets a property of the specified [object](mta://reference/misc/object.md).

## Syntax

```
mixed getObjectProperty ( object theObject, string property )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[object](mta://reference/misc/object.md):getProperty(...)*

**Counterpart**: *[setProperty](https://wiki.multitheftauto.com/index.php?title=SetProperty&action=edit&redlink=1)*

### Required Arguments

- **theObject:** the [object](mta://reference/misc/object.md) you wish to get a property of.

- **property:** the property you want to get the value of:

- "all" - *table* with values of all properties below (OOP method: *getProperties*)

- "mass" - *float*

- "turn_mass" - *float*

- "air_resistance" - *float*

- "elasticity" - *float*

- "center_of_mass" - *Vector3D* - **(x, y, z)**

- "buoyancy" - *float*

### Returns

On success: [table](mta://reference/misc/table.md) for **all**, 3 [floats](mta://reference/misc/float.md) for **center_of_mass** or [float](mta://reference/misc/float.md) for other properties

On failure: *false*

## Example

Click to collapse [-]
Client

```
addEventHandler("onClientResourceStart", resourceRoot, function()
	local theObject = createObject(980, 0, 0, 0) -- create an object
	if theObject then
		setObjectProperty(theObject, "center_of_mass", 0, -1, 0) -- set its center of mass

		local x, y, z = getObjectProperty(theObject, "center_of_mass") -- get its center of mass
		outputChatBox("Object's center of mass: "..tostring(x)..", "..tostring(y)..", "..tostring(z))
	end
end)
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

- [setObjectScale](mta://scripting/shared/functions/setobjectscale.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22430](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22430):

- [isObjectMoving](mta://scripting/shared/functions/isobjectmoving.md)

ADDED/UPDATED IN VERSION 1.6.0 [r21765](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21765):

- [isObjectBreakable](mta://scripting/shared/functions/isobjectbreakable.md)

- [setObjectBreakable](mta://scripting/shared/functions/setobjectbreakable.md)

- [stopObject](mta://scripting/shared/functions/stopobject.md)

- [getObjectMass](mta://scripting/client/functions/getobjectmass.md)

- getObjectProperty

- [setObjectMass](mta://scripting/client/functions/setobjectmass.md)

- [setObjectProperty](mta://scripting/client/functions/setobjectproperty.md)

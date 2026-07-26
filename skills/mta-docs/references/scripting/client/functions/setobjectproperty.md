---
doc_id: "mta-wiki:10970"
title: "SetObjectProperty"
source_title: "SetObjectProperty"
source_url: "https://wiki.multitheftauto.com/wiki/SetObjectProperty"
revision_id: 72968
language: "en"
categories: ["Client_functions", "Changes_in_1.5.6"]
---

# SetObjectProperty

This function sets a property of the specified [object](https://wiki.multitheftauto.com/index.php?search=object).

## Syntax

```
bool setObjectProperty ( object theObject, string property, var value )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[object](https://wiki.multitheftauto.com/index.php?search=object):setProperty(...)*

**Counterpart**: *[getProperty](https://wiki.multitheftauto.com/index.php?title=GetProperty&action=edit&redlink=1)*

### Required Arguments

- **theObject:** the [object](https://wiki.multitheftauto.com/index.php?search=object) you wish to change a property of.

- **property:** the property you want to set the value of:

- "mass" - *float*

- "turn_mass" - *float*

- "air_resistance" - *float*

- "elasticity" - *float*

- "center_of_mass" - *Vector3D* - **(x, y, z)**

- "buoyancy" - *float*

- **value:** the new value for the property.

### Returns

Returns *true* if the property was set successfully, *false* otherwise.

## Example

Click to collapse [-]
Client

```
addEventHandler("onClientResourceStart", resourceRoot, function()
	local theObject = createObject(980, 0, 0, 0) -- create an object
	if theObject then
		setObjectProperty(theObject, "center_of_mass", 0, -1, 0) -- set its center of mass
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

- [getObjectProperty](mta://scripting/client/functions/getobjectproperty.md)

- [setObjectMass](mta://scripting/client/functions/setobjectmass.md)

- setObjectProperty

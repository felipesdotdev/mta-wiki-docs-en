---
doc_id: "mta-wiki:5457"
title: "GetObjectScale"
source_title: "GetObjectScale"
source_url: "https://wiki.multitheftauto.com/wiki/GetObjectScale"
revision_id: 68483
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetObjectScale

This function returns the visible size of an object.

## Syntax

```
float, float, float getObjectScale ( object theObject )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Object](https://wiki.multitheftauto.com/index.php?search=Object):getScale(...)*

**Variable**: *.scale*

**Counterpart**: *[setObjectScale](mta://scripting/shared/functions/setobjectscale.md)*

### Required Arguments

- **theObject**: the [object](https://wiki.multitheftauto.com/index.php?search=object) you wish to return the scale of.

### Returns

- Three [float](mta://reference/misc/float.md) values indicating the scale of the object on the x, y, and z axis if successful, *false* otherwise.

## Example

Click to collapse [-]
Client-only Example

This example adds a command named *getscale* which creates an object and prints out the scale of it.

```
addCommandHandler("getscale",
    function()
	local theObject = createObject(1337, getElementPosition(localPlayer))
	local x, y, z = getObjectScale(theObject)
	outputChatBox("Object scale: X: "..x..", Y: "..y.." Z: "..z.."")
    end
)
```

## See Also

- [createObject](mta://scripting/shared/functions/createobject.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22489](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22489):

- [breakObject](mta://scripting/shared/functions/breakobject.md)

- getObjectScale

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

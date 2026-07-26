---
doc_id: "mta-wiki:6829"
title: "IsObjectMoving"
source_title: "IsObjectMoving"
source_url: "https://wiki.multitheftauto.com/wiki/IsObjectMoving"
revision_id: 81151
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.6.0"]
---

# IsObjectMoving

This function checks if an [object](https://wiki.multitheftauto.com/index.php?search=object) is moving.

ADDED/UPDATED IN VERSION 1.6.0 [r22430](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22430):

This function is now also available on the server side. 

## Syntax

```
bool isObjectMoving ( object theObject )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[object](https://wiki.multitheftauto.com/index.php?search=object):isMoving(...)*

**Variable**: *.moving*

### Required Arguments

- **theObject:** The [object](https://wiki.multitheftauto.com/index.php?search=object) [element](mta://reference/misc/element.md).

### Returns

- Returns *true* if the [object](https://wiki.multitheftauto.com/index.php?search=object) is moving, *false* otherwise.

## Example

This example creates an object when the resource starts and checks if the object is moving:

```
addEventHandler ("onClientResourceStart", resourceRoot,
    function ()
        local x, y, z = getElementPosition (localPlayer)
        object = createObject (1239, x, y, z)

        moveObject (object, 5000, x, y, z + 5)
    end
)

addCommandHandler ("getmoving",
    function (commandName)
        outputChatBox ("Is object "..(isObjectMoving(object) and "moving" or "not moving"))
    end
)
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

- isObjectMoving

ADDED/UPDATED IN VERSION 1.6.0 [r21765](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21765):

- [isObjectBreakable](mta://scripting/shared/functions/isobjectbreakable.md)

- [setObjectBreakable](mta://scripting/shared/functions/setobjectbreakable.md)

- [stopObject](mta://scripting/shared/functions/stopobject.md)

- [getObjectMass](mta://scripting/client/functions/getobjectmass.md)

- [getObjectProperty](mta://scripting/client/functions/getobjectproperty.md)

- [setObjectMass](mta://scripting/client/functions/setobjectmass.md)

- [setObjectProperty](mta://scripting/client/functions/setobjectproperty.md)

---
doc_id: "mta-wiki:6957"
title: "BreakObject"
source_title: "BreakObject"
source_url: "https://wiki.multitheftauto.com/wiki/BreakObject"
revision_id: 79515
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:11:45.966833+00:00"
---

# BreakObject

This function breaks a specific object.

ADDED/UPDATED IN VERSION 1.6.0 [r22489](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22489):

This function is now also available on the server side. 

| [[{{{image}}}\|link=\|]] | Note: Only breakable objects can be broken. |
| --- | --- |
|  |  |

## Syntax

```
bool breakObject ( object theObject )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[object](mta://reference/misc/object.md):break(...)*

### Required Arguments

- **theObject:** an [object](mta://reference/misc/object.md) element

### Returns

- *true* if the object was successfully broken.

- *false* if the object is not breakable, or a wrong object was given.

## Example

This example checks if the object created is breakable and if it is then breaks it.

```
addCommandHandler("createObj",
function(command, id)
    local x, y, z = getElementPosition(localPlayer)
    local object = createObject (id, x, y, z)
    if (id) then
        if isObjectBreakable(object) then
            breakObject(object)
        end
    end
end
)
```

## See Also

- [createObject](mta://scripting/shared/functions/createobject.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22489](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22489):

- breakObject

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

- [setObjectProperty](mta://scripting/client/functions/setobjectproperty.md)

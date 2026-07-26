---
doc_id: "mta-wiki:6214"
title: "IsObjectBreakable"
source_title: "IsObjectBreakable"
source_url: "https://wiki.multitheftauto.com/wiki/IsObjectBreakable"
revision_id: 81112
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:15:57.509192+00:00"
---

# IsObjectBreakable

ADDED/UPDATED IN VERSION 1.6.0 [r21765](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21765):

Added also as a server-side function. Previously only available as a client-side function. 

This function checks if an object / model ID is breakable.

## Syntax

```
bool isObjectBreakable ( object theObject / int modelId )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[object](mta://reference/misc/object.md):isBreakable(...)*

**Variable**: *.breakable*

**Counterpart**: *[setObjectBreakable](mta://scripting/shared/functions/setobjectbreakable.md)*

### Required Arguments

- **theObject / modelId:** The [object](mta://reference/misc/object.md) / model ID that's being checked.

### Returns

- *true* if the object is breakable.

- *false* if the object is not breakable.

## Example

This example creates an object when the resource starts and checks if the object is breakable.

```
addEventHandler("onClientResourceStart", resourceRoot, function()
    local object = createObject(1337, 5540.6654, 1020.55122, 1240.545)
    if isObjectBreakable(object) then
        outputChatBox("Yes, the object is breakable.")
    else
        outputChatBox("No, the object is not breakable")
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

- isObjectBreakable

- [setObjectBreakable](mta://scripting/shared/functions/setobjectbreakable.md)

- [stopObject](mta://scripting/shared/functions/stopobject.md)

- [getObjectMass](mta://scripting/client/functions/getobjectmass.md)

- [getObjectProperty](mta://scripting/client/functions/getobjectproperty.md)

- [setObjectMass](mta://scripting/client/functions/setobjectmass.md)

- [setObjectProperty](mta://scripting/client/functions/setobjectproperty.md)

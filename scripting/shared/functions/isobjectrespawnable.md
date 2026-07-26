---
doc_id: "mta-wiki:14405"
title: "IsObjectRespawnable"
source_title: "IsObjectRespawnable"
source_url: "https://wiki.multitheftauto.com/wiki/IsObjectRespawnable"
revision_id: 80108
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:15:57.563782+00:00"
---

# IsObjectRespawnable

ADDED/UPDATED IN VERSION 1.6.0 [r22708](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22708):

This function checks if the object has respawn enabled, which can be toggled using [toggleObjectRespawn](mta://scripting/shared/functions/toggleobjectrespawn.md). 

## Syntax

```
bool isObjectRespawnable( object theObject )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[object](mta://reference/misc/object.md):isRespawnable(...)*

### Required Arguments

- **theObject:** an [object](mta://reference/misc/object.md) element.

### Returns

Returns true if the object has respawning enabled, false otherwise.

## Example

```
addCommandHandler('checkobjects', function()
    local count = 0
    for k,v in ipairs(getElementsByType('object')) do
        if (isObjectRespawnable(v)) then
            count = count + 1
        end
    end

    outputChatBox(count..' objects on map are respawnable!')
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

- isObjectRespawnable

- [setObjectScale](mta://scripting/shared/functions/setobjectscale.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22430](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22430):

- [isObjectMoving](mta://scripting/shared/functions/isobjectmoving.md)

ADDED/UPDATED IN VERSION 1.6.0 [r21765](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21765):

- [isObjectBreakable](mta://scripting/shared/functions/isobjectbreakable.md)

- [setObjectBreakable](mta://scripting/shared/functions/setobjectbreakable.md)

- [stopObject](mta://scripting/shared/functions/stopobject.md)

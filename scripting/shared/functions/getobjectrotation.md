---
doc_id: "mta-wiki:1554"
title: "GetObjectRotation"
source_title: "GetObjectRotation"
source_url: "https://wiki.multitheftauto.com/wiki/GetObjectRotation"
revision_id: 67679
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated"]
generated_at: "2026-07-26T16:15:16.244881+00:00"
---

# GetObjectRotation

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getElementRotation instead. |  |

Object rotation can be retrieved from objects in mapfiles or objects that are created in scripts.

## Syntax

```
float float float getObjectRotation ( object theObject )
```

### Required Arguments

- **theObject:** The object whose rotation will be retrieved

### Returns

Returns three *float*s if object exists, *false* in the first variable and *nil* in the other two if it's invalid.

## Example

If a player points at an object with a gun, its rotation will appear in the chat box.

Click to collapse [-]
Server

```
function onPlayerTargeted ( targetElem )
    if ( isElement(targetElem) and getElementType(targetElem) == "object" ) then
        local x,y,z = getObjectRotation ( targetElem )
        outputChatBox ( "Object rotation: " .. x .. " " .. y .. " " .. z, source )
    end
end
addEventHandler ( "onPlayerTarget", root, onPlayerTargeted )
```

Click to expand [+]
Client

```
function onPlayerTargeted ( targetElem )
    if ( isElement(targetElem) and getElementType (targetElem) == "object" ) then
        local x,y,z = getObjectRotation ( targetElem )
        outputChatBox ( "Object rotation: " .. x .. " " .. y .. " " .. z )
    end
end
addEventHandler ( "onClientPlayerTarget", root, onPlayerTargeted )
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

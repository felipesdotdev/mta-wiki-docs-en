---
doc_id: "mta-wiki:1553"
title: "GetObjectModel"
source_title: "GetObjectModel"
source_url: "https://wiki.multitheftauto.com/wiki/GetObjectModel"
revision_id: 67678
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated"]
---

# GetObjectModel

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getElementModel instead. |  |

This function retrieves the model ID of a specified object.

## Syntax

```
int getObjectModel ( object theObject )
```

### Required Arguments

- **theObject:** The object which you wish to retrieve the model ID of

### Returns

Returns an *int* with the object model id, or *false* if it isn't a valid object.

## Example

This example destroys a haystack when a player targets it.

```
function onPlayerTargeted ( targetElem )
    if ( getElementType ( targetElem ) == "object" ) and ( getObjectModel ( targetElem ) == 3374 ) then
        destroyElement ( targetElem )
    end
end
addEventHandler ( "onPlayerTarget", root, onPlayerTargeted )
```

This example outputs the model id of objects the player is targeting.

```
function onPlayerTargeted ( targetElem )
    if ( getElementType ( targetElem ) == "object") then
        outputChatBox ( getObjectModel(targetElem) )
    end
end
addEventHandler ( "onPlayerTarget", root, onPlayerTargeted )
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

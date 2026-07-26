---
doc_id: "mta-wiki:6958"
title: "RespawnObject"
source_title: "RespawnObject"
source_url: "https://wiki.multitheftauto.com/wiki/RespawnObject"
revision_id: 80104
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.6.0"]
---

# RespawnObject

This function respawns a specific object.

ADDED/UPDATED IN VERSION 1.6.0 [r22708](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22708):

This function is now also available on the server side. 

## Syntax

```
bool respawnObject ( object theObject )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[object](https://wiki.multitheftauto.com/index.php?search=object):respawn(...)*

### Required Arguments

- **theObject:** an [object](https://wiki.multitheftauto.com/index.php?search=object) element

### Returns

- *true* if the object was sucessfully respawned.

- *false* if the object is not breakable, or a wrong object was given.

## Example

This example prevents objects from despawning. When an object breaks, it gets respawned right away.

```
addEventHandler ( "onClientObjectBreak", getRootElement(),
    function ()
        respawnObject ( source )
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

- respawnObject

- [toggleObjectRespawn](mta://scripting/shared/functions/toggleobjectrespawn.md)

- [isObjectRespawnable](mta://scripting/shared/functions/isobjectrespawnable.md)

- [setObjectScale](mta://scripting/shared/functions/setobjectscale.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22430](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22430):

- [isObjectMoving](mta://scripting/shared/functions/isobjectmoving.md)

ADDED/UPDATED IN VERSION 1.6.0 [r21765](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21765):

- [isObjectBreakable](mta://scripting/shared/functions/isobjectbreakable.md)

- [setObjectBreakable](mta://scripting/shared/functions/setobjectbreakable.md)

- [stopObject](mta://scripting/shared/functions/stopobject.md)

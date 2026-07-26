---
doc_id: "mta-wiki:1556"
title: "SetObjectRotation"
source_title: "SetObjectRotation"
source_url: "https://wiki.multitheftauto.com/wiki/SetObjectRotation"
revision_id: 44564
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated"]
---

# SetObjectRotation

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use setElementRotation instead. |  |

Allows you to change an object's rotation while playing a map. The object can be from the map file or created in a script.

## Syntax

```
bool setObjectRotation ( object theObject, float rotX, float rotY, float rotZ )
```

### Required Arguments

- **theObject:** The object to be rotated

- **rotX:** Rotation around the X axis

- **rotY:** Rotation around the Y axis

- **rotZ:** Rotation around the Z axis

### Returns

Returns *true* if successful, *false* otherwise.

## Example

In this example, I refer to an object in the map file with the ID "pirateship":

```
<object id="pirateship" posX="-1627.319092" posY="128.543411" posZ="6.581001" rotX="-0.760854" rotY="2.421000" rotZ="0.851000" model="8493"/>
```

```
function onResourceStart ( name, root )
    -- predefined variables, needed for the math code below
    rotX = 0
    rotY = 0
    rotZ = 0
    -- assign element named 'pirateship' in map file to variable
    pirateship = getElementByID ( "pirateship" )
end

function chatboxShipRotateLeft ( playerSource, commandName ) -- On console command 'increaserotations'
    outputChatBox ( "Rotational values increased" )
    -- rotations = rotations + 10
    rotX = rotX + 10
    rotY = rotY + 10
    rotZ = rotZ + 10
    -- Changed rotation is applied
    setObjectRotation ( pirateship, rotX, rotY, rotZ )
end     

function chatboxShipRotateRight ( playerSource, commandName ) -- On console command 'decreaserotations'
    outputChatBox ( "Rotational values decreased" )
    -- rotations = rotations - 10
    rotX = rotX - 10
    rotY = rotY - 10
    rotZ = rotZ - 10
    -- Changed rotation is applied
    setObjectRotation ( pirateship, rotX, rotY, rotZ )
end

-- Set up event and command handlers
addEventHandler ( "onResourceStart", resourceRoot, onResourceStart )

addCommandHandler ( "increaserotations", chatboxShipRotateLeft )
addCommandHandler ( "decreaserotations", chatboxShipRotateRight )
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

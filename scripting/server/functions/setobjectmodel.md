---
doc_id: "mta-wiki:1555"
title: "SetObjectModel"
source_title: "SetObjectModel"
source_url: "https://wiki.multitheftauto.com/wiki/SetObjectModel"
revision_id: 60580
language: "en"
categories: ["Deprecated", "Server_functions"]
generated_at: "2026-07-26T16:16:41.681295+00:00"
---

# SetObjectModel

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use setElementModel instead. |  |

This sets a new object model to the specified element.

## Syntax

```
bool setObjectModel ( object theObject, int id )
```

### Required Arguments

- **theObject:** A valid [object](mta://reference/misc/object.md).

- **id:** An [int](mta://reference/misc/int.md) specifying the model id.

### Returns

Returns *true* if the model change was successful, *false* otherwise.

## Example

Click to collapse [-]
Server

This will continually change an object model every 2.5 seconds at the location -1084.52, -1634.81, 76.36 (Truth's farm).

```
myobject = createObject ( 5822, -1084.52, -1634.81, 76.36 )
-- We create an initial object element. I choose object model 5822 to begin with.

function objectRandomization ()  
    local randomobjectnumber = math.random(1, 18000)
    -- Choose a random number between 1 and 18000 as a whole integer and assign it to
    -- the variable 'randomobjectnumber'
    setObjectModel ( myobject, randomobjectnumber )
    -- Change our object appearance by applying a new model ID
end

setTimer ( objectRandomization, 2500, 0 )
-- Every 2.5 seconds, the function 'objectRandomization' is called by this timer.
-- Each time the function runs, it changes the object model by applying a new whole-
-- integer random object ID. This timer is called an infinite amount of times since  
-- its repeat value is set to 0.
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

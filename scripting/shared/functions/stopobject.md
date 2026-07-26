---
doc_id: "mta-wiki:2618"
title: "StopObject"
source_title: "StopObject"
source_url: "https://wiki.multitheftauto.com/wiki/StopObject"
revision_id: 78500
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:16:52.534459+00:00"
---

# StopObject

This will allow you to stop an object that is currently moving.

## Syntax

```
bool stopObject ( object theObject )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[object](mta://reference/misc/object.md):stop(...)*

### Required Arguments

- **theObject:** the [object](mta://reference/misc/object.md) whose movement you wish to stop

### Returns

- *true* if successful.

- *false* otherwise.

## Example

This will allow you to toggle the random movement of a staircase object model using a *randomObjectMovement* function and stop it immediately with the stopObject command.  This is achieved by using a "toggleobjectmove" command with a "on" or "off" parameter.

```
function objectMoveControl ( thePlayer, commandName, state )
    -- On "toggleobjectmove" in console, activate this command, which also asks the player to define the value for the varible 'state'. 
    if state == "on" then
        outputChatBox ( "Moving object randomly" )
        mytimer = setTimer ( randomObjectMovement, 2250, 0 )
        -- if the player types "on" for the state variable, turn on the timer, which triggers a function
        -- called randomObjectMovement that moves the object whenever it is called (not included for
        -- this example). The timer runs every 2 1/4 seconds for 0 times, which means it runs infinitely.
    elseif state == "off" then
        outputChatBox ( "Stopping object movement" )
        killTimer ( mytimer )
        stopObject ( myobject )
        -- if the player typed "off" for state, stop the object movement immediately and kill the
        -- randomObjectMovement timer
    else
        outputChatBox ( "must define object state as 'on' or 'off'" )
        -- if the player typed something besides "on" or "off" for state, do nothing
    end
end
addCommandHandler ( "toggleobjectmove", objectMoveControl )
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

- stopObject

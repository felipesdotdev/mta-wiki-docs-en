---
doc_id: "mta-wiki:1391"
title: "MoveObject"
source_title: "MoveObject"
source_url: "https://wiki.multitheftauto.com/wiki/MoveObject"
revision_id: 75293
language: "en"
categories: ["Server_functions", "Client_functions", "Functions_and_events_with_issues"]
---

# MoveObject

This function will smoothly move an object from its current position to a specified rotation and position.

## Syntax

```
bool moveObject ( object theObject, int time, float targetx, float targety, float targetz, [ float moverx, float movery, float moverz, string strEasingType, float fEasingPeriod, float fEasingAmplitude, float fEasingOvershoot ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[object](https://wiki.multitheftauto.com/index.php?search=object):move(...)*

### Required Arguments

- **theObject:** the object that will be moved.

- **time:** the time in milliseconds the object will arrive at the destination.

- **targetx:** the X value of the target position

- **targety:** the Y value of the target position

- **targetz:** the Z value of the target position

### Optional Arguments

- **moverx:** the rotation along the X axis **relative** to its current rotation, which is its starting angle.

- **movery:** the rotation along the Y axis **relative** to its current rotation, which is its starting angle.

- **moverz:** the rotation along the Z axis **relative** to its current rotation, which is its starting angle.

- **strEasingType:** the [easing function](mta://reference/misc/easing.md) to use for the interpolation (default is "Linear")

- **fEasingPeriod:** the period of the [easing function](mta://reference/misc/easing.md) (only some easing functions use this parameter)

- **fEasingAmplitude:** the amplitude of the [easing function](mta://reference/misc/easing.md) (only some easing functions use this parameter)

- **fEasingOvershoot:** the overshoot of the [easing function](mta://reference/misc/easing.md) (only some easing functions use this parameter)

### Returns

- *true* if the function moved the object succesfully.

- *false* otherwise.

## Examples

Click to collapse [-]
Server

**Example 1:** This example moves every object in the game up 100 units in ten seconds.

```
allObjects = getElementsByType ( "object" )
for key, theObject in ipairs ( allObjects ) do
	local origX, origY, origZ = getElementPosition ( theObject ) --get the original position
	local newZ = origZ + 100 -- make a new z position
	moveObject ( theObject, 10000, origX, origY, newZ ) --move the object to this position in 10 seconds.
end
```

Click to collapse [-]
Server

**Example 2:** This example created a model (of a bed) near a player called *someguy*, if they exist in the game. It will then move the model towards the player over 3 seconds.

```
-- Find a player called 'someguy'
someGuy = getPlayerFromName ( "someguy" )
-- If a player called someguy was found then
if ( someGuy ) then
	-- Get the player's position
	x, y, z = getElementPosition ( someGuy )
	-- Create a bed (1700) object near to the player
	bed = createObject ( 1700, x + 5, y, z )
	-- Move the bed towards the player over 3 seconds (3000 milliseconds)
	moveObject ( bed, 3000, x, y, z )
	-- Tell the player in the chat box
	outputChatBox ( "Moving a bed towards you!", someGuy )
else
	-- Tell everyone that a player called 'someguy' could not be found
	outputChatBox ( "Player someguy doesn't exist" )
end
```

Click to collapse [-]
Server

**Example 3:** This example creates a ball moving (in front of CJ's house in Grove Street) using easing functions. Test command is "/smove" for instance "/smove OutBounce". This example is a serverside code but the same could be done clientside (adapting the command handler)

```
local START_POS = {2497.203125, -1672.4864501953, 12.640947341919}
local STOP_POS = {2480.2595214844, -1666.521484375, 12.640114784241}
local MOTION_DURATION = 5000
local WAIT_DURATION = 1000

addCommandHandler("smove",
function (player, cmd, strEasingType, period, amplitude, overshoot)
	local x, y, z = unpack(START_POS)
	local object = createObject(1598, x, y, z)
	x, y, z = unpack(STOP_POS)
	
	period = period or 0.3
	amplitude = amplitude or 1.0
	overshoot = overshoot or 1.70158
	
	outputChatBox(string.format("Server Easing %s %s %s %s", strEasingType, tostring(period), tostring(amplitude), tostring(overshoot)))
	moveObject(object, MOTION_DURATION, x, y, z, 0, 0, 360, strEasingType, period, amplitude, overshoot)
	setTimer(destroyElement, MOTION_DURATION+WAIT_DURATION, 1, object)
end)
```

Click to collapse [-]
Server

**Example 4:** This example move a gate with easing.

```
local x,y,z = 2096.3, 1721, 12.7
local easing = "OutBounce"
local time = 2000
local gate = createObject(980, x,y,z, 0, 0, 63)
local marker = createMarker(x,y,z, "cylinder", 12, 0, 0, 0, 0)
 
function moveGate(hitPlayer, matchingDimension)
        moveObject(gate, time, x+4.9, y+9.6, z, 0, 0, 0, easing)
end
addEventHandler("onMarkerHit", marker, moveGate)
 
function moveBack()
    moveObject(gate, time, x, y, z, 0, 0, 0, easing)
end
addEventHandler("onMarkerLeave", marker, moveBack)
```

## Issues

| Issue ID | Description |
| --- | --- |
| #549 | Object rotation is wrong after moveObject serverside |

## See Also

- [createObject](mta://scripting/shared/functions/createobject.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22489](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22489):

- [breakObject](mta://scripting/shared/functions/breakobject.md)

- [getObjectScale](mta://scripting/shared/functions/getobjectscale.md)

- moveObject

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

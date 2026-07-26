---
doc_id: "mta-wiki:2392"
title: "AttachElementToElement"
source_title: "AttachElementToElement"
source_url: "https://wiki.multitheftauto.com/wiki/AttachElementToElement"
revision_id: 44591
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated", "Utility_templates"]
generated_at: "2026-07-26T16:10:26.574273+00:00"
---

# AttachElementToElement

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use attachElements instead. |  |

This function attaches one element to another, so that the first one follows the second whenever it moves.

If an attempt is made to attach two elements that are already attached the opposite way (eg theElement becomes theAttachToElement and vice versa), the 1st attachment order is automatically detached in favor of the 2nd attachment order. For example, if carA was attached to carB, now carB is attached to carA. Also, an element cannot be attached to two separate elements at one time. For example, two cars can be attached to one single car, but one single car cannot be attached to two separate cars. If you attempt to do this, the existing attachment will automatically be dropped in favor of the new attachment. For example, if carA is asked to attached to carB then carC, it is only attached to carC.

This is not compatible with all elements.  The following elements are compatible:

- [Markers](mta://reference/misc/marker.md)

- [Blips](mta://reference/misc/blip.md)

- [Objects](mta://reference/misc/object.md)

- [Players](mta://reference/misc/player.md)

- [Vehicles](mta://reference/misc/vehicle.md)

## Syntax

```
bool attachElementToElement ( element theElement, element theAttachToElement, [ float xPosOffset, float yPosOffset, float zPosOffset, float xRotOffset, float yRotOffset, float zRotOffset ] )
```

### Required Arguments

- **theElement:** The element to be attached.

- **theAttachToElement:** The element to attach the first to.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **xPosOffset:** The x offset, if you want the elements to be a certain distance from one another (default 0).

- **yPosOffset:** The y offset (default 0).

- **zPosOffset:** The z offset (default 0).

- **xRotOffset:** The x rotation offset (default 0).

- **yRotOffset:** The y rotation offset (default 0).

- **zRotOffset:** The z rotation offset (default 0).

### Returns

Returns *true* if the attaching process was successful, *false* otherwise.

## Example

Click to collapse [-]
Server

**Example 1:** This example attaches a marker to the player who steals the Mr. Whoopee:

```
-- create the vehicle
local vehicleMrWhoopee = createVehicle ( 423, 237.472 -54.225 1.518, 0, 354.488, 0 )

function onMrWhoopeeEnter ( thePlayer, seat, jackedPlayer )
    outputChatBox ( getClientName ( thePlayer ) .. " stole the Whoopee!", getRootElement (), 255, 0, 0 )
    -- create the marker to attach
    local arrowMarker = createMarker ( 0, 0, 0, "arrow", .75, 255, 0, 0, 170 )
    -- attach the marker to the player with a vertical offset of 2 units
    attachElementToElement ( arrowMarker, thePlayer, 0, 0, 2 )
end

-- attach it to an event
addEventHandler ( "onVehicleEnter", vehicleMrWhoopee, onMrWhoopeeEnter )
```

**Example 2:** This function adds a tank on top of a player (for extra defense):

```
function tankHat( source, commandName )
      local x, y, z = getElementPosition( source ) --Get the players position
      local tank = createVehicle( 432, x, y, z + 5 ) --Create a tank
      attachElementToElement( tank, source, 0, 0, 5 ) --Attach the tank to the player.
end
addCommandHandler( "hat", tankHat )
```

Click to expand [+]
Client

**Example 3:** This function adds a tank on top of a player (for extra defense), clientside.  This means it will be invisible to other players.

```
function tankHat( commandName )
      local x, y, z = getElementPosition( source ) --Get the players position
      local tank = createVehicle( 432, x, y, z + 5 ) --Create a tank
      attachElementToElement( tank, source, 0, 0, 5 ) --Attach the tank to the player.
end
addCommandHandler( "hat", tankHat )
```

## See Also

- [attachElements](mta://scripting/shared/functions/attachelements.md)

- [createElement](mta://scripting/shared/functions/createelement.md)

- [destroyElement](mta://scripting/shared/functions/destroyelement.md)

- [detachElements](mta://scripting/shared/functions/detachelements.md)

- [getAttachedElements](mta://scripting/shared/functions/getattachedelements.md)

- [getElementAlpha](mta://scripting/shared/functions/getelementalpha.md)

- [getElementAttachedOffsets](mta://scripting/shared/functions/getelementattachedoffsets.md)

- [getElementAttachedTo](mta://scripting/shared/functions/getelementattachedto.md)

- [getElementByIndex](mta://scripting/shared/functions/getelementbyindex.md)

- [getElementByID](mta://scripting/shared/functions/getelementbyid.md)

- [getElementChild](mta://scripting/shared/functions/getelementchild.md)

- [getElementChildren](mta://scripting/shared/functions/getelementchildren.md)

- [getElementChildrenCount](mta://scripting/shared/functions/getelementchildrencount.md)

- [getElementCollisionsEnabled](mta://scripting/shared/functions/getelementcollisionsenabled.md)

- [getElementColShape](mta://scripting/shared/functions/getelementcolshape.md)

- [getElementData](mta://scripting/shared/functions/getelementdata.md)

- [getAllElementData](mta://scripting/shared/functions/getallelementdata.md)

- [hasElementData](mta://scripting/shared/functions/haselementdata.md)

- [getElementDimension](mta://scripting/shared/functions/getelementdimension.md)

- [getElementHealth](mta://scripting/shared/functions/getelementhealth.md)

- [getElementID](mta://scripting/shared/functions/getelementid.md)

- [getElementInterior](mta://scripting/shared/functions/getelementinterior.md)

- [getElementMatrix](mta://scripting/shared/functions/getelementmatrix.md)

- [getElementModel](mta://scripting/shared/functions/getelementmodel.md)

- [getElementParent](mta://scripting/shared/functions/getelementparent.md)

- [getElementPosition](mta://scripting/shared/functions/getelementposition.md)

- [getElementRotation](mta://scripting/shared/functions/getelementrotation.md)

- [getElementsByType](mta://scripting/shared/functions/getelementsbytype.md)

- [getElementsWithinColShape](mta://scripting/shared/functions/getelementswithincolshape.md)

- [getElementsWithinRange](mta://scripting/shared/functions/getelementswithinrange.md)

- [getElementType](mta://scripting/shared/functions/getelementtype.md)

- [getElementVelocity](mta://scripting/shared/functions/getelementvelocity.md)

- [getLowLODElement](mta://scripting/shared/functions/getlowlodelement.md)

- [getRootElement](mta://scripting/shared/functions/getrootelement.md)

- [isElement](mta://scripting/shared/functions/iselement.md)

- [isElementAttached](mta://scripting/shared/functions/iselementattached.md)

- [isElementCallPropagationEnabled](mta://scripting/shared/functions/iselementcallpropagationenabled.md)

- [isElementDoubleSided](mta://scripting/shared/functions/iselementdoublesided.md)

- [isElementFrozen](mta://scripting/shared/functions/iselementfrozen.md)

- [isElementInWater](mta://scripting/shared/functions/iselementinwater.md)

- [isElementLowLOD](mta://scripting/shared/functions/iselementlowlod.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22864](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22864):

- [isElementOnFire](mta://scripting/shared/functions/iselementonfire.md)

- [isElementWithinColShape](mta://scripting/shared/functions/iselementwithincolshape.md)

- [isElementWithinMarker](mta://scripting/shared/functions/iselementwithinmarker.md)

- [setElementAlpha](mta://scripting/shared/functions/setelementalpha.md)

- [setElementAngularVelocity](mta://scripting/shared/functions/setelementangularvelocity.md)

- [getElementAngularVelocity](mta://scripting/shared/functions/getelementangularvelocity.md)

- [setElementAttachedOffsets](mta://scripting/shared/functions/setelementattachedoffsets.md)

- [setElementCallPropagationEnabled](mta://scripting/shared/functions/setelementcallpropagationenabled.md)

- [setElementCollisionsEnabled](mta://scripting/shared/functions/setelementcollisionsenabled.md)

- [setElementData](mta://scripting/shared/functions/setelementdata.md)

- [setElementDimension](mta://scripting/shared/functions/setelementdimension.md)

- [setElementDoubleSided](mta://scripting/shared/functions/setelementdoublesided.md)

- [setElementFrozen](mta://scripting/shared/functions/setelementfrozen.md)

- [setElementHealth](mta://scripting/shared/functions/setelementhealth.md)

- [setElementID](mta://scripting/shared/functions/setelementid.md)

- [setElementInterior](mta://scripting/shared/functions/setelementinterior.md)

- [setElementModel](mta://scripting/shared/functions/setelementmodel.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22864](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22864):

- [setElementOnFire](mta://scripting/shared/functions/setelementonfire.md)

- [setElementParent](mta://scripting/shared/functions/setelementparent.md)

- [setElementPosition](mta://scripting/shared/functions/setelementposition.md)

- [setElementRotation](mta://scripting/shared/functions/setelementrotation.md)

- [setElementVelocity](mta://scripting/shared/functions/setelementvelocity.md)

- [setLowLODElement](mta://scripting/shared/functions/setlowlodelement.md)

---
doc_id: "mta-wiki:1730"
title: "SetElementVelocity"
source_title: "SetElementVelocity"
source_url: "https://wiki.multitheftauto.com/wiki/SetElementVelocity"
revision_id: 80786
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.4"]
generated_at: "2026-07-26T16:16:40.613495+00:00"
---

# SetElementVelocity

This function sets the velocity (movement speeds) along each axis, for an element.

This is not compatible with all elements. Only the following element types are compatible:

- [Ped](mta://reference/misc/ped.md)

- [Vehicle](mta://reference/misc/vehicle.md)

- [Object](mta://reference/misc/object.md)

- [Projectile](mta://reference/misc/projectile.md)

## Syntax

```
bool setElementVelocity ( element theElement, float speedX, float speedY, float speedZ )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[element](mta://reference/misc/element.md):setVelocity(...)*

**Variable**: *.velocity*

**Counterpart**: *[getElementVelocity](mta://scripting/shared/functions/getelementvelocity.md)*

### Required Arguments

- **theElement:** The [element](mta://reference/misc/element.md) you wish to set the velocity of.

- **speedX:** A floating point value determining the speed along the X axis.

- **speedY:** A floating point value determining the speed along the Y axis.

- **speedZ:** A floating point value determining the speed along the Z axis.

### Returns

Returns *true* if the speed was set successfully, *false* if a bad element was specified or other bad arguments.

## Example

Click to collapse [-]
Server

This example adds a function which copies the speed of a random player to another random player. If there are less than 2 players it returns *false*.

```
function equalTwoRandomPlayersVelocity()
    if getPlayerCount() < 2 then -- If there's only one player (or no players) this doesn't make sense
        return false
    end
    local randomPlayer1, randomPlayer2 = getRandomPlayer(), getRandomPlayer() -- Get two random players
    while randomPlayer1 == randomPlayer2 do -- Make sure the two players are different
        randomPlayer2 = getRandomPlayer()
    end
    local speedx, speedy, speedz = getElementVelocity (randomPlayer1) -- Get the velocity of the first random player
    setElementVelocity(randomPlayer2, speedx, speedy, speedz) -- Copy that velocity to the second random player
    outputChatBox("Now " .. getPlayerName(randomPlayer2) .. " runs as fast as " .. getPlayerName(randomPlayer1) .. "!", root, 255, 128, 0)
    return true
end
```

Click to collapse [-]
Client

This example lets players jump their vehicle into the air (if they are the driver).

```
function initBind()
	bindKey("lshift", "down", jumpKey)
end
addEventHandler("onClientResourceStart", resourceRoot, initBind)

function jumpKey()
	if not isPedInVehicle(localPlayer) then return end

	local vehicle = getPedOccupiedVehicle(localPlayer)
	if vehicle and getVehicleController(vehicle) == localPlayer then
		local vehType = getVehicleType(vehicle)
		if vehType == "Plane" or vehType == "Helicopter" then return end
		local sx, sy, sz = getElementVelocity(vehicle)
		setElementVelocity(vehicle, sx, sy, sz + 0.33) -- The jump effect is achieved by raising the Z axis (height) coordinate
	end
end
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

- setElementVelocity

- [setLowLODElement](mta://scripting/shared/functions/setlowlodelement.md)

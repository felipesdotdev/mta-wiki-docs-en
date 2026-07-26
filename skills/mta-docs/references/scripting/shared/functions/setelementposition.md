---
doc_id: "mta-wiki:1728"
title: "SetElementPosition"
source_title: "SetElementPosition"
source_url: "https://wiki.multitheftauto.com/wiki/SetElementPosition"
revision_id: 82440
language: "en"
categories: ["Server_functions", "Client_functions", "Functions_and_events_with_issues"]
---

# SetElementPosition

This function sets the position of an element to the specified coordinates.

| [[\|link=\|]] | Warning: Do not use this function to spawn a player . It will cause problems with other functions like warpPedIntoVehicle . Use spawnPlayer instead. |
| --- | --- |
|  |  |

## Syntax

```
bool setElementPosition ( element theElement, float x, float y, float z [, bool warp = true ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[element](mta://reference/misc/element.md):setPosition(...)*

**Variable**: *.position*

**Counterpart**: *[getElementPosition](mta://scripting/shared/functions/getelementposition.md)*

### Required Arguments

- **theElement:** A valid [element](mta://reference/misc/element.md) to be moved.

- **x:** The x coordinate of the destination.

- **y:** The y coordinate of the destination.

- **z:** The z coordinate of the destination.

### Optional Arguments

- **warp:** teleports players, resetting any animations they were doing. Setting this to *false* preserves the current animation.

### Returns

Returns *true* if the function was successful, *false* otherwise.

## Example

Click to collapse [-]
Server

This example lets admins teleport 5 random players to themselves

```
function randomPlayersToLocation(p)
    if not isPlayerStaff(p) then return end

	local playersOnline = getElementsByType("player")
	local amount = #playersOnline

	if amount == 0 then return end

	for index = 1,(amount > 5 and 5 or amount) do
		local player = playersOnline[index]
		setElementPosition(player, getElementPosition(p))
	end
end
addCommandHandler("randomtp", randomPlayersToLocation)
addCommandHandler("playershere", randomPlayersToLocation)

-- Utility function
local staffACLs = {
    aclGetGroup("Admin"),
    aclGetGroup("Moderator")
}

function isPlayerStaff(p)
	if isElement(p) and getElementType(p) == "player" and not isGuestAccount(getPlayerAccount(p)) then
		local object = getAccountName(getPlayerAccount(p))

		for _, group in ipairs(staffACLs) do
			if isObjectInACLGroup("user." .. object, group) then
				return true
			end
		end
	end
	return false
end
```

If you want to put a vehicle or player out of the water or simulate the position-resetting behaviour if CJ goes below the ground too far, then you need to retrieve a recommended coordinate on ground to place the element at. Take a look at [this MTA forums post](https://forum.mtasa.com/topic/132891-important-helprespawn-vehicle/?do=findComment&comment=1003198) for steps in the right direction.

## Issues

| Issue ID | Description |
| --- | --- |
| #539 | Changing player position when he/she has a jetpack will remove the jetpack and bug when skin is changed |
| #529 | Player falls from his bike when its teleported by setElementPosition |

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

- setElementPosition

- [setElementRotation](mta://scripting/shared/functions/setelementrotation.md)

- [setElementVelocity](mta://scripting/shared/functions/setelementvelocity.md)

- [setLowLODElement](mta://scripting/shared/functions/setlowlodelement.md)

---
doc_id: "mta-wiki:10507"
title: "GetElementsWithinRange"
source_title: "GetElementsWithinRange"
source_url: "https://wiki.multitheftauto.com/wiki/GetElementsWithinRange"
revision_id: 79283
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.9"]
generated_at: "2026-07-26T16:15:13.084652+00:00"
---

# GetElementsWithinRange

This function is used to retrieve a list of all elements of specified type within a range of 3D coordinates.

BEFORE VERSION 1.5.9 [r21438](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21438):

- Z argument isn't in use currently, but make your scripts like it is for future compatibility reasons.

- Z argument is now being taken into consideration when checking for elements.

| [[{{{image}}}\|link=\|]] | Note: This function checks if elements are in a box, not in a sphere. This function doesn't work with elements which are created by createElement. |
| --- | --- |
|  |  |

## Syntax

```
table getElementsWithinRange ( float x, float y, float z, float range [, string elemType = "", int interior, int dimension ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Element](mta://reference/misc/element.md).getWithinRange(...)*

### Required Arguments

- **x:** the x coordinate at which to retrieve elements.

- **y:** the y coordinate at which to retrieve elements.

- **z:** the z coordinate at which to retrieve elements.

- **range:** the range at the coordinates in which to retrieve elements.

### Optional Arguments

- **elemType:** The type of element you want a list of. This can be any element type, such as:

- **"player":** A player connected to the server.

- **"ped":** A ped.

- **"vehicle":** A vehicle.

- **"object":** An object.

- **"pickup":** A pickup.

- **"marker":** A marker.

- **interior:** The [interior](mta://reference/misc/interior.md) you want to limit the search to. If not specified, it can return elements in any interior.

- **dimension:** The [dimension](mta://reference/misc/dimension.md) you want to limit the search to. If not specified, it can return elements in any dimension.

### Returns

Returns a [table](mta://reference/misc/table.md) containing all the elements of the specified type within range. Returns an empty [table](mta://reference/misc/table.md) if there are no elements within range. Returns *false* if the arguments are invalid.

## Example

This example allows admins to destroy all vehicles in close proximity.

```
function deleteNearbyVehicles(playerElement)
	local playerAccount = getPlayerAccount(playerElement)

	if (not playerAccount) then
		return false
	end

	local guestAccount = isGuestAccount(playerAccount)

	if (guestAccount) then
		return false
	end

	local accountName = getAccountName(playerAccount)
	local aclObject = "user."..accountName
	local adminGroup = aclGetGroup("Admin")
	local playerAdmin = isObjectInACLGroup(aclObject, adminGroup)

	if (not playerAdmin) then
		return false
	end

	local playerX, playerY, playerZ = getElementPosition(playerElement)
	local playerInterior = getElementInterior(playerElement)
	local playerDimension = getElementDimension(playerElement)
	local searchRange = 300
	local nearbyVehicles = getElementsWithinRange(playerX, playerY, playerZ, searchRange, "vehicle", playerInterior, playerDimension)

	for vehicleID = 1, #nearbyVehicles do
		local vehicleElement = nearbyVehicles[vehicleID]
		local validElement = isElement(vehicleElement)

		if (validElement) then
			destroyElement(vehicleElement)
		end
	end
end
addCommandHandler("deletenearbyvehs", deleteNearbyVehicles)
```

## Example

This example retrieves a table of players within range of the 3D coordinates and prints their name to the chat.

```
local playersTable = getElementsWithinRange(0, 0, 3, 20, "player") -- get all player elements within 20 units of 0, 0, 3

for _, playerElement in pairs(playersTable) do -- use a generic for loop to step through each player
	local playerName = getPlayerName(playerElement) -- get player name

	outputChatBox(playerName.." is within range") -- print their name to the chat
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

- getElementsWithinRange

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

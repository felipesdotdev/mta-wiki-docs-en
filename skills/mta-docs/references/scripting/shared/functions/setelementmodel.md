---
doc_id: "mta-wiki:3945"
title: "SetElementModel"
source_title: "SetElementModel"
source_url: "https://wiki.multitheftauto.com/wiki/SetElementModel"
revision_id: 74784
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# SetElementModel

Sets the model of a given element. This allows you to change the model of a player (or ped), a vehicle or an object.

## Syntax

```
bool setElementModel ( element theElement, int model )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[element](mta://reference/misc/element.md):setModel(...)*

**Variable**: *.model*

**Counterpart**: *[getElementModel](mta://scripting/shared/functions/getelementmodel.md)*

### Required Arguments

- **theElement:** the element you want to change.

- **model:** the model ID to set.

- For players/peds: A GTASA player model (skin) ID. See [Character Skins](mta://reference/misc/character-skins.md).

- For vehicles: The [vehicle ID](mta://reference/misc/vehicle-ids.md) of the vehicle being changed.

- For objects/projectiles/weapons: An [int](mta://reference/misc/int.md) specifying the model id.

### Returns

Returns *true* if successful, *false* otherwise.

## Example

Click to collapse [-]
Example 1 (Server)

This example allows players to change their own skin with a command (/skin [ID])

```
local spam = {}

function setSkin(player, cmd, skin)
    if spam[player] and getTickCount() - spam[player] < 4000 then
        return outputChatBox("You cannot change skin that often!", player, 255, 0, 0)
    end

    skin = skin and tonumber(skin)

    if getElementModel(player) == skin or isPedDead(player) then
        return
    end

    if skin and skin <= 99999 then -- what do we know about dynamic ped ID range?
        setElementModel(player, skin)
        spam[player] = getTickCount()
    else
        outputChatBox("Invalid skin ID!", player, 255, 0, 0)
    end
end
addCommandHandler("skin", setSkin)

function cleanUp()
    if spam[source] then
        spam[source] = nil
    end
end
addEventHandler("onPlayerQuit", root, cleanUp)
```

Click to collapse [-]
Example 2 (Server)

This example allows players to transform their current vehicle into another vehicle model.

```
local spam = {}

function changeMyVehicle(player, command, newModel)
	if spam[player] and getTickCount() - spam[player] < 2500 then
		return outputChatBox("Don't spam vehicle changes!", player, 255, 0, 0)
	end

	local theVehicle = getPedOccupiedVehicle(player)
	
	if not (theVehicle and getVehicleController(theVehicle) == player) then
		return outputChatBox("You must be driving a vehicle in order to change it!", player, 255, 0, 0)
	end

	if isValidModel(newModel) and isElement(theVehicle) then
		setElementModel(theVehicle, newModel)
		spam[player] = getTickCount()
	else
		outputChatBox("Invalid vehicle ID!", player, 255, 0, 0)
	end
end
addCommandHandler("changeveh", changeMyVehicle)

function isValidModel(modelID)
	modelID = tonumber(modelID)
	if modelID and modelID >= 400 and modelID <= 611 then
		return true
	end
	return false
end

function cleanUp()
	if spam[source] then
		spam[source] = nil
	end
end
addEventHandler("onPlayerQuit", root, cleanUp)
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

- setElementModel

ADDED/UPDATED IN VERSION 1.6.0 [r22864](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22864):

- [setElementOnFire](mta://scripting/shared/functions/setelementonfire.md)

- [setElementParent](mta://scripting/shared/functions/setelementparent.md)

- [setElementPosition](mta://scripting/shared/functions/setelementposition.md)

- [setElementRotation](mta://scripting/shared/functions/setelementrotation.md)

- [setElementVelocity](mta://scripting/shared/functions/setelementvelocity.md)

- [setLowLODElement](mta://scripting/shared/functions/setlowlodelement.md)

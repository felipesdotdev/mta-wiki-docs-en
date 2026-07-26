---
doc_id: "mta-wiki:1489"
title: "DestroyElement"
source_title: "DestroyElement"
source_url: "https://wiki.multitheftauto.com/wiki/DestroyElement"
revision_id: 73037
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:11:20.923344+00:00"
---

# DestroyElement

This function destroys an [element](mta://reference/misc/element.md) and all elements within it in the hierarchy (its children, the children of those children etc). [Player](mta://reference/misc/player.md) elements cannot be destroyed using this function. A player can only be removed from the hierarchy when they quit or are kicked. The root element also cannot be destroyed, however, passing the root as an argument will wipe all elements from the server, except for the players and clients, which will become direct descendants of the root node, and other elements that cannot be destroyed, such as resource root elements.

| [[{{{image}}}\|link=\|]] | Note: There is bug when you try to destroy webbrowser that returned from guiGetBrowser so instead of that destroy the gui-element one that returned from guiCreateBrowser otherwise the game will be crushed (By Master_MTA). |
| --- | --- |
|  |  |

Players are not the only elements that cannot be deleted. This list also includes remote clients and console elements.

| [[{{{image}}}\|link=\|]] | Note: As element ids are eventually recycled, always make sure you nil variables containing the element after calling this function |
| --- | --- |
|  |  |

## Syntax

```
bool destroyElement ( element elementToDestroy )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[element](mta://reference/misc/element.md):destroy(...)*

### Required Arguments

- **elementToDestroy:** The element you wish to destroy.

### Returns

Returns *true* if the element was destroyed successfully, *false* if either the element passed to it was invalid or it could not be destroyed for some other reason (for example, clientside destroyElement can't destroy serverside elements).

## Remarks

If a streamed-in element is destroyed then it is NOT streamed out, i.e. the [onClientElementStreamOut](mta://scripting/client/events/onclientelementstreamout.md) client-side event is NOT triggered. Thus it is wrong to assume a clean stream-in and stream-out sequence on the client-side. Additionally to onClientElementStreamOut use a [onClientElementDestroy](mta://scripting/client/events/onclientelementdestroy.md) event handler to detect the destruction of streamed-in elements.

## Example

**Example 1:** This example would destroy every element in the map, with the exception of players and the root element itself.

```
-- Destroy all its children, except players.
destroyElement ( root )
```

**Example 2:** This example destroys all vehicles of the specified model:

```
function destroyVehiclesOfModel(modelID)
	-- get a table of all the vehicles that exist and loop through it
	local vehicles = getElementsByType("vehicle")
	for i,v in ipairs(vehicles) do
		-- if the vehicle's ID is the one provided, destroy it
		if (getElementModel(v) == modelID) then
			destroyElement(v)
		end
	end
end

destroyVehiclesOfModel(445)
```

**Example 3:** This example allows creation of claymores, which trigger and explode.  When they explode, the colshape and object for the claymore are destroyed.

```
function createClaymore ( x,y,z, creator )
	local claymoreObject = createObject ( 1945, x, y, z - 1, 0, 0, 90 )  -- create an object which looks like a claymore
	local claymoreCol = createColSphere ( x, y, z, 1 )                   -- create a col sphere with radius 1
	setElementData ( claymoreCol, "object", claymoreObject )             -- store the object of the claymore
	setElementData ( claymoreCol, "creatorPlayer", creator )             -- store the person who created it
	addEventHandler ( "onColShapeHit", claymoreCol, claymoreHit )        -- add an event handler to the colshape
end

function claymoreHit ( thePlayer, matchingDimension )
	-- retrieve the object associated to the claymore, and who created it
	local claymoreObject = getElementData ( source, "object" )
	local claymoreCreator = getElementData ( source, "creatorPlayer" )
	-- get the position of the claymore
	local x,y,z = getElementPosition ( source )
	createExplosion ( x,y,z, 12, claymoreCreator ) -- create an explosion, associated to the creator, of a small size at the col's position
	-- remove the event handler for the colshape
	removeEventHandler ( "onColShapeHit", source, claymoreHit )
	-- destroy the claymore object, and the col shape so it doesn't trigger again.
	destroyElement ( claymoreObject )
	destroyElement ( source )
end
```

**Example 4:** This example destroys all vehicles, regardless of ID, name, etc:

```
function allvehiclesaredoomed()
	-- get a table of all the vehicles that exist and loop through it
	vehicles = getElementsByType("vehicle")
	for i,v in ipairs(vehicles) do
		-- destroy every vehicle.
		destroyElement(v)
	end
end
--The command handler below will destroy all vehicles once
--you enter /vdoom in the chat box or vdoom in the game console.
addCommandHandler("vdoom", allvehiclesaredoomed)
--This is very useful if you use the freeroam resource and some
--heartless players start spawn spamming.
--You can also set it on a timer to have your server clear all
--vehicles ever 60 minutes, (1 hour).  Timer below:
setTimer(allvehiclesaredoomed, 3600000, 0)
```

## See Also

- [attachElements](mta://scripting/shared/functions/attachelements.md)

- [createElement](mta://scripting/shared/functions/createelement.md)

- destroyElement

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

---
doc_id: "mta-wiki:1725"
title: "SetElementVisibleTo"
source_title: "SetElementVisibleTo"
source_url: "https://wiki.multitheftauto.com/wiki/SetElementVisibleTo"
revision_id: 80365
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:40.642548+00:00"
---

# SetElementVisibleTo

This function can change an [element](mta://reference/misc/element.md)'s [visibility](mta://reference/misc/visibility.md).

This function only works with the following elements.

- [Markers](mta://reference/misc/marker.md)

- [Blips](mta://reference/misc/blip.md)

- [Radarareas](mta://reference/misc/radararea.md)

Visibility settings of lower elements in the element tree override higher ones - if visibility for root is set to false and for a player is set to true, it will be visible to the player.

If you want to clear all visibility settings of an [element](mta://reference/misc/element.md), try [clearElementVisibleTo](mta://scripting/server/functions/clearelementvisibleto.md)

Setting visibility for one element will also set visibility for all of its children.  

Order of **setElementVisibleTo** calls doesn't matter.

## Syntax

```
bool setElementVisibleTo ( element theElement, element visibleTo, bool visible )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[element](mta://reference/misc/element.md):setVisibleTo(...)*

**Counterpart**: *[isElementVisibleTo](mta://scripting/server/functions/iselementvisibleto.md)*

### Required Arguments

- **theElement:** The element you want to control the visibility of.

- **visibleTo:** The element you wish the element to be visible or invisible to. Any child elements that are players will also be able to see the element. See [visibility](mta://reference/misc/visibility.md).

- **visible:** Whether you are making it visible or invisible to the player.

### Returns

Returns *true* if the element's visibility was changed successfully, *false* otherwise, for example if you are trying to change the visibility of a vehicle, player or object.

## Example

This example creates a marker and makes it only visibile to the player called 'someguy'.

```
-- Find the player called someguy
local someguy = getPlayerFromName ( "someguy" )
-- If the player was found then
if ( someguy ) then
	-- Get the player's position into the variables x, y and z
	x, y, z = getElementPosition ( someguy )
	-- Create a marker at the player's position
	myMarker = createMarker ( x, y, z )
	
	-- Then make the marker invisible to the whole dimension (root for the first)
	setElementVisibleTo ( myMarker, root, false )
	-- Set marker visibility to true for someguy
	setElementVisibleTo ( myMarker, someguy, true )
	
	-- The order in which you do the visibility changes does not matter, but ideally trues should be set before falses in order to prevent a momentary flicker.
end
```

The following example shows how to make the marker visible to everyone except anotherguy

```
-- Find the player called someguy
local someguy = getPlayerFromName ( "someguy" )
local anotherguy = getPlayerFromName ( "anotherguy" )
-- If the player was found then
if ( someguy ) then
	-- Get the player's position into the variables x, y and z
	x, y, z = getElementPosition ( someguy )
	-- Create a marker at the player's position
	myMarker = createMarker ( x, y, z )
	attachElements(myMarker, someguy)

	-- First make sure everyone is able to see the marker, this line is unnecessary in this case as root visibility is set to true by default behaviour
	setElementVisibleTo ( myMarker, root, true )

	-- Then hide it from anotherguy
	setElementVisibleTo ( myMarker, anotherguy, false )
end
```

## See Also

- [addElementDataSubscriber](mta://scripting/server/functions/addelementdatasubscriber.md)

- [clearElementVisibleTo](mta://scripting/server/functions/clearelementvisibleto.md)

- [cloneElement](mta://scripting/server/functions/cloneelement.md)

- [getElementSyncer](mta://scripting/server/functions/getelementsyncer.md)

- [getElementZoneName](mta://scripting/server/functions/getelementzonename.md)

- [hasElementDataSubscriber](mta://scripting/server/functions/haselementdatasubscriber.md)

- [isElementVisibleTo](mta://scripting/server/functions/iselementvisibleto.md)

- [removeElementData](mta://scripting/server/functions/removeelementdata.md)

- [removeElementDataSubscriber](mta://scripting/server/functions/removeelementdatasubscriber.md)

- [setElementSyncer](mta://scripting/server/functions/setelementsyncer.md)

- setElementVisibleTo
  

- **Shared**

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

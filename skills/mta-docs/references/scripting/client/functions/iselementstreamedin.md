---
doc_id: "mta-wiki:3653"
title: "IsElementStreamedIn"
source_title: "IsElementStreamedIn"
source_url: "https://wiki.multitheftauto.com/wiki/IsElementStreamedIn"
revision_id: 77642
language: "en"
categories: ["Client_functions", "Changes_in_1.0", "Changes_in_1.6.0"]
---

# IsElementStreamedIn

This function checks whether an [element](mta://reference/misc/element.md) is currently streamed in (not virtualized) and are actual GTA objects in the world. You can force an element to be streamed in using [setElementStreamable](mta://scripting/client/functions/setelementstreamable.md).

## Syntax

```
bool isElementStreamedIn ( element theElement )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[element](mta://reference/misc/element.md):isStreamedIn(...)*

**Variable**: *.streamedIn*

### Required Arguments

- **theElement**: The [element](mta://reference/misc/element.md) to check whether is streamed in or not.

### Returns

Returns *true* if the passed element is currently streamed in, *false* if it is virtualized.

## Example

This command shows you how many objects you have streamed in.

```
function checkTheObjects ( cmd )
	local amount = 0 -- When starting the command, we don't have any objects looped.
	for k,v in ipairs ( getElementsByType ( "object" ) ) do -- Looping all the objects in the server
		if isElementStreamedIn ( v ) then -- If the object is streamed in
			amount = amount + 1 -- It's an object more streamed in
		end
	end
	outputChatBox ( "You have currently " ..amount.. " objects streamed in." ) -- Send the player the amount of objects that are streamed in
end
addCommandHandler ( "checkobjects", checkTheObjects )
```

Note: Objects can already stream from a very long distance, so even when you can't see some objects, they can still be returned.

## See Also

- [getElementBoneMatrix](mta://scripting/client/functions/getelementbonematrix.md)

- [getElementBonePosition](mta://scripting/client/functions/getelementboneposition.md)

- [getElementBoneRotation](mta://scripting/client/functions/getelementbonerotation.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22741](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22741):

- [getElementBoneQuaternion](mta://scripting/client/functions/getelementbonequaternion.md) 

- [getElementBoundingBox](mta://scripting/client/functions/getelementboundingbox.md)

- [getElementDistanceFromCentreOfMassToBaseOfModel](mta://scripting/client/functions/getelementdistancefromcentreofmasstobaseofmodel.md)

- [getElementLighting](mta://scripting/client/functions/getelementlighting.md)

- [getElementRadius](mta://scripting/client/functions/getelementradius.md)

- [isElementCollidableWith](mta://scripting/client/functions/iselementcollidablewith.md)

- [isElementLocal](mta://scripting/client/functions/iselementlocal.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22862](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22862):

- [setElementLighting](mta://scripting/client/functions/setelementlighting.md)

- [isElementOnScreen](mta://scripting/client/functions/iselementonscreen.md)

- [isElementStreamable](mta://scripting/client/functions/iselementstreamable.md)

- isElementStreamedIn

- [isElementSyncer](mta://scripting/client/functions/iselementsyncer.md)

- [isElementWaitingForGroundToLoad](mta://scripting/client/functions/iselementwaitingforgroundtoload.md)

- [setElementBoneMatrix](mta://scripting/client/functions/setelementbonematrix.md)

- [setElementBonePosition](mta://scripting/client/functions/setelementboneposition.md)

- [setElementBoneRotation](mta://scripting/client/functions/setelementbonerotation.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22741](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22741):

- [setElementBoneQuaternion](mta://scripting/client/functions/setelementbonequaternion.md) 

- [setElementCollidableWith](mta://scripting/client/functions/setelementcollidablewith.md)

- [setElementStreamable](mta://scripting/client/functions/setelementstreamable.md)

- [updateElementRpHAnim](mta://scripting/client/functions/updateelementrphanim.md)
  

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

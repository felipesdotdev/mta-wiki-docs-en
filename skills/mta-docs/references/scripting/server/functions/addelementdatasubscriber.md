---
doc_id: "mta-wiki:12424"
title: "AddElementDataSubscriber"
source_title: "AddElementDataSubscriber"
source_url: "https://wiki.multitheftauto.com/wiki/AddElementDataSubscriber"
revision_id: 81239
language: "en"
categories: ["Server_functions"]
---

# AddElementDataSubscriber

This function subscribes a [player](https://wiki.multitheftauto.com/index.php?search=player) to specific [element data](mta://reference/misc/element-data--975d1ea3.md).
This function is used together with [setElementData](mta://scripting/shared/functions/setelementdata.md) in *"subscribe"* mode.

| [[{{{image}}}\|link=\|]] | Note: Before using this function you need to setup an initial value of element data in "subscribe" mode, otherwise the subscriber will not be added. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: Calling removeElementData or setElementData with other sync mode will automatically remove all subscribers of specified element data. |
| --- | --- |
|  |  |

## Syntax

```
bool addElementDataSubscriber ( element theElement, string key, player thePlayer )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[element](mta://reference/misc/element.md):addDataSubscriber(...)*

**Counterpart**: *[removeElementDataSubscriber](mta://scripting/server/functions/removeelementdatasubscriber.md)*

### Required Arguments

- **theElement:** The [element](mta://reference/misc/element.md) you wish to subscribe the [player](https://wiki.multitheftauto.com/index.php?search=player) to.

- **key:** The key you wish to subscribe the player to.

- **thePlayer:** The [player](https://wiki.multitheftauto.com/index.php?search=player) you wish to subscribe.

### Returns

Returns *true* if the player was subscribed, *false* otherwise.

## Example

Click to collapse [-]
Server

```
addEventHandler("onVehicleEnter", getRootElement(), function(thePlayer, seat)
   if seat==0 then -- if the player is a driver
      addElementDataSubscriber(source, "id", thePlayer) -- subscribe the player to element
   end
end)
```

## See Also

- addElementDataSubscriber

- [clearElementVisibleTo](mta://scripting/server/functions/clearelementvisibleto.md)

- [cloneElement](mta://scripting/server/functions/cloneelement.md)

- [getElementSyncer](mta://scripting/server/functions/getelementsyncer.md)

- [getElementZoneName](mta://scripting/server/functions/getelementzonename.md)

- [hasElementDataSubscriber](mta://scripting/server/functions/haselementdatasubscriber.md)

- [isElementVisibleTo](mta://scripting/server/functions/iselementvisibleto.md)

- [removeElementData](mta://scripting/server/functions/removeelementdata.md)

- [removeElementDataSubscriber](mta://scripting/server/functions/removeelementdatasubscriber.md)

- [setElementSyncer](mta://scripting/server/functions/setelementsyncer.md)

- [setElementVisibleTo](mta://scripting/server/functions/setelementvisibleto.md)
  

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

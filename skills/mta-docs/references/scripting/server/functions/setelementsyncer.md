---
doc_id: "mta-wiki:5144"
title: "SetElementSyncer"
source_title: "SetElementSyncer"
source_url: "https://wiki.multitheftauto.com/wiki/SetElementSyncer"
revision_id: 80363
language: "en"
categories: ["Server_functions"]
---

# SetElementSyncer

This function can be used to change the syncer ([player](https://wiki.multitheftauto.com/index.php?search=player)) of an element. The syncer is the player who is responsible for informing the server about the state of that element - it's position, orientation and other state information. The function can be also used to remove an element's syncer.

Only [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle) and [ped](https://wiki.multitheftauto.com/index.php?search=ped) elements can have a syncer, other element types are not currently automatically synced by MTA.

Please note that using this function to change an element's syncer will only last as long as the element is within syncable range of the player unless persist is set to true. This is within 140 units for vehicles and 100 units for peds. As soon as it becomes impossible for your chosen player to sync the element, another player (or no player) will be automatically selected, and your setting will be lost. With vehicles, the last occupant to leave a vehicle will be selected as the syncer and override any setting you may have made.

Using this function to remove an element's syncer, means no player will be assigned to syncing the element. That will not be changed until setElementSyncer is called again.
It should also be noted that certain network changes to an element do not require a syncer. Actions such as destroying an element or explicitly setting the element's position (in a server side script), will still be updated on all clients regardless of this setting.

## Syntax

```
bool setElementSyncer ( element theElement, player thePlayer[, bool persist=false ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[element](mta://reference/misc/element.md):setSyncer(...)*

**Variable**: *.syncer*

**Counterpart**: *[getElementSyncer](mta://scripting/server/functions/getelementsyncer.md)*

### Required Arguments

- **theElement:** The [element](mta://reference/misc/element.md) whose syncer you wish to change.

- **thePlayer:** The [player](https://wiki.multitheftauto.com/index.php?search=player) who should be the new syncer of the element. If set to *false*, this element will not have a syncer. If set to *true*, MTA will pick automatically the nearest or most relevant player to that element.

### Optional Arguments

- **persist:** If *true*, the server will not automatically change the syncer. If set to *false*, default syncer behavior resumes.

### Returns

Returns *true* if the syncer was changed successfully, *false* if the element passed was not a ped or vehicle.

## Example

```
addCommandHandler ( "createMyVehicle", function ( player, command )
    local x, y, z = getElementPosition ( player )
    local myVehicle = createVehicle ( 411, x, y, z )
    setElementSyncer ( myVehicle, player )
end
)
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

- setElementSyncer

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

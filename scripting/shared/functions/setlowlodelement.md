---
doc_id: "mta-wiki:6003"
title: "SetLowLODElement"
source_title: "SetLowLODElement"
source_url: "https://wiki.multitheftauto.com/wiki/SetLowLODElement"
revision_id: 82126
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:16:41.259486+00:00"
---

# SetLowLODElement

This function assigns a low LOD element to an element. The low LOD element is displayed when its associated element is not fully visible. If a low LOD element is assigned to several elements, it will be displayed when any of these elements are not fully visible.

| [[{{{image}}}\|link=\|]] | Note: The only valid elements types for assigning LODs with this function are Object and Building . |
| --- | --- |
|  |  |

## Syntax

```
bool setLowLODElement ( element theElement, element lowLODElement )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[element](mta://reference/misc/element.md):setLowLOD(...)*

**Variable**: *.lowLOD*

**Counterpart**: *[getLowLODElement](mta://scripting/shared/functions/getlowlodelement.md)*

### Required Arguments

- **theElement:** The [element](mta://reference/misc/element.md) whose low LOD version we want to change.

- **lowLODElement :** A low LOD element to display when the first element is not fully visible.

### Returns

Returns *true* if the assignment was successful, *false* otherwise.

## Examples

Click to collapse [-]
Clientside

This example shows how to create and link a normal and low LOD object:

```
-- Create a normal object
    local objNormal = createObject ( 3620, x,y,z,0,0,0 )

    -- Create a low LOD object
    local objLowLOD = createObject ( 5154, x,y,z,0,0,0,true )

    -- Assign the LOD object with the Normal object
    setLowLODElement ( objNormal, objLowLOD )
    -- Set the LOD object's parent to the Normal object so it is destroyed together
    setElementParent( objLowLOD, objNormal )

    -- Set the draw distance for the model we are using for low LOD to maximum
    engineSetModelLODDistance ( 5154, 300 )
```

Click to collapse [-]
Serverside

This example shows how to create and link a composite object

```
-- Create composite object
    objMainBit = createObject ( 3620, x,y,z )
    objLeftBit = createObject ( 5158, x,y,z )
    objRightBit = createObject ( 5158, x,y,z )
    objDetailBit1 = createObject ( 1337, x,y,z )
    objDetailBit2 = createObject ( 1337, x,y,z )
    objInternalBit = createObject ( 1337, x,y,z )
    attachElements ( objLeftBit, objMainBit, -10, 0, 0 )
    attachElements ( objRightBit, objMainBit, 10, 0, 0 )
    attachElements ( objDetailBit1, objMainBit, 5, 0, 0 )
    attachElements ( objDetailBit2, objLeftBit, 5, 5, 0 )
    attachElements ( objInternalBit, objRightBit, 5, 7, 0 )

    -- Create low LOD object (which represents the whole composite model)
    objlowLOD = createObject ( 5154, x,y,z, 0, 0, 0, true )

    -- Attach low LOD object so it moves with the main model
    attachElements ( objlowLOD, objMainBit, 0, 0, 0 )

    -- Set the low LOD object's parent to the main object so it is destroyed together
    setElementParent( objLowLOD, objMainBit )

    -- Set associations so the low LOD model is displayed when the main parts are not full visible
    setLowLODElement ( objMainBit, objlowLOD )
    setLowLODElement ( objLeftBit, objlowLOD )
    setLowLODElement ( objRightBit, objlowLOD )

    -- Note that the detail and internal parts have not been associated to the low LOD object

    -- Set the draw distance for the model we are using for low LOD to maximum
    triggerClientEvent("onClientChangeModelLODDistance", resourceRoot, 5154, 300 )
```

Click to collapse [-]
Clientside

Changing the draw distance for a model has to be done on the client:

```
addEvent("onClientChangeModelLODDistance",true)
addEventHandler("onClientChangeModelLODDistance", resourceRoot,
    function(model,distance)
        engineSetModelLODDistance ( model, distance )
    end
)
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

- setLowLODElement

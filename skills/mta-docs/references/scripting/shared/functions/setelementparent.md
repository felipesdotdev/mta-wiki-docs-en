---
doc_id: "mta-wiki:1538"
title: "SetElementParent"
source_title: "SetElementParent"
source_url: "https://wiki.multitheftauto.com/wiki/SetElementParent"
revision_id: 48696
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# SetElementParent

This function is used for setting an element as the parent of another element.

| [[{{{image}}}\|link=\|]] | Important Note: The client-side version of this function can only be used on client-created elements. It cannot be used to modify the parent of server side elements. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: This function does not change when an element will be destroyed - Elements are always destroyed when the resource that created them is stopped. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: When an element is destroyed, its parent becomes the new parent of its children. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: setElementParent only works if new parent is the root element, map root, or ancestor of map root |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Tip: This function does not affect the child elements position. To attach elements use the function attachElements . |
| --- | --- |
|  |  |

## Syntax

```
bool setElementParent ( element theElement, element parent )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[element](mta://reference/misc/element.md):setParent(...)*

**Variable**: *.parent*

**Counterpart**: *[getElementParent](mta://scripting/shared/functions/getelementparent.md)*

### Required Arguments

- **theElement:** The element that you wish to set the parent of.

- **parent:** The element you wish to be the parent of *theElement*.

### Returns

Returns *true* if both [elements](mta://reference/misc/element.md) are valid, *false* otherwise.

## Example

Click to collapse [-]
Server

This example sets the parent of each spawnpoint to a dummy element:

```
dummyElem = createElement ( "spawngroup", "Group of spawn points" ) -- create a dummy element
local spawnpoints = getElementsByType ( "spawnpoint" ) -- get a table of spawn point elements
for k,v in ipairs (spawnpoints) do -- loop through the table of spawn points
   setElementParent ( v, dummyElem ) -- set the dummy element as the parent of the spawn point
end
-- all of the spawn points are now children of 'dummyElem'
```

This is the equivalent of:

```
<spawngroup id="Group of spawn points">
   <spawnpoint id="spawnpoint_0" posX="2507.8715820313" posY="2772.6071777344" posZ="10.8203125" rot="270" skin="285"/>
   <spawnpoint id="spawnpoint_1" posX="2508.060546875" posY="2780.3647460938" posZ="10.8203125" rot="270" skin="285"/>
   <spawnpoint id="spawnpoint_2" posX="2508.0053710938" posY="2776.2897949219" posZ="10.8203125" rot="270" skin="285"/>
   <spawnpoint id="spawnpoint_3" posX="2510.6899414063" posY="2778.3745117188" posZ="10.8203125" rot="270" skin="285"/>
</spawngroup>
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

- setElementParent

- [setElementPosition](mta://scripting/shared/functions/setelementposition.md)

- [setElementRotation](mta://scripting/shared/functions/setelementrotation.md)

- [setElementVelocity](mta://scripting/shared/functions/setelementvelocity.md)

- [setLowLODElement](mta://scripting/shared/functions/setlowlodelement.md)

---
doc_id: "mta-wiki:12584"
title: "GetElementBoneMatrix"
source_title: "GetElementBoneMatrix"
source_url: "https://wiki.multitheftauto.com/wiki/GetElementBoneMatrix"
revision_id: 81269
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:15:10.678878+00:00"
---

# GetElementBoneMatrix

This function returns the transformation matrix of a specific bone. Currently the [Player](mta://reference/misc/element-player.md) and [Ped](mta://reference/misc/element-ped.md) element types are accepted.

| [[{{{image}}}\|link=\|]] | Tip: If you want to attach an element to a bone, see attachElementToBone . |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Tip: For matrix manipulation which goes beyond the basic examples given on this page, see the Lua matrix library . Using the built-in matrix class is also recommended. |
| --- | --- |
|  |  |

## Syntax

```
table getElementBoneMatrix ( element theElement, int boneId )
```

### Required Arguments

- **theElement:** the [element](mta://reference/misc/element.md) to get the bone matrix on.

- **boneId:** the ID of the bone to get the matrix of. See [Bone IDs](mta://reference/misc/bone-ids.md).

### Returns

Returns a multi-dimensional array (which can be transformed into a proper [matrix](mta://reference/misc/matrix.md) class using *Matrix.create* method) containing a 4x4 matrix. Returns *false* if invalid arguments were passed.

## Example

this example will output bone position and rotation for id 5.

```
local boneMatrix = getElementBoneMatrix(localPlayer, 5) -- get the bone matrix for localPlayer, id: 5
if boneMatrix then
    -- extract position and rotation from the matrix
    local posX, posY, posZ = boneMatrix[4][1], boneMatrix[4][2], boneMatrix[4][3]
    local rotX, rotY, rotZ = math.deg(math.asin(-boneMatrix[3][2])), math.deg(math.atan2(boneMatrix[3][1], boneMatrix[3][3])), math.deg(math.atan2(boneMatrix[1][2], boneMatrix[2][2]))

    outputChatBox("Bone position: (" .. posX .. ", " .. posY .. ", " .. posZ .. ")")
    outputChatBox("Bone rotation: (" .. rotX .. ", " .. rotY .. ", " .. rotZ .. ")")
else
    outputChatBox("Invalid element or bone ID.")
end
```

## See Also

- getElementBoneMatrix

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

- [isElementStreamedIn](mta://scripting/client/functions/iselementstreamedin.md)

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

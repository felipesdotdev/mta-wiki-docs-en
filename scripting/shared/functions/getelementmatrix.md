---
doc_id: "mta-wiki:4543"
title: "GetElementMatrix"
source_title: "GetElementMatrix"
source_url: "https://wiki.multitheftauto.com/wiki/GetElementMatrix"
revision_id: 68107
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:15:11.549992+00:00"
---

# GetElementMatrix

This function gets an [element](mta://reference/misc/element.md)'s transform [matrix](mta://reference/misc/matrix.md). This contains 16 float values that multiplied to a point will give you the point transformed. It is most useful for matrix calculations such as calculating offsets. For further information, please refer to a tutorial of matrices in computer graphics programming.

| [[{{{image}}}\|link=\|]] | Note: The matrix returned by this function is not setup correctly for some calculations unless the legacy argument is set to false . |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Tip: For matrix manipulation which goes beyond the basic examples given on this page, see the Lua matrix library . If you are using MTA: SA 1.4 or higher, using the built-in matrix class is also recommended. |
| --- | --- |
|  |  |

## Syntax

```
table getElementMatrix ( element theElement [, bool legacy = true ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[element](mta://reference/misc/element.md):getMatrix(...)*

**Variable**: *.matrix*

**Counterpart**: *[setElementMatrix](mta://scripting/shared/functions/setelementmatrix.md)*

### Required Arguments

- **theElement:** The [element](mta://reference/misc/element.md) which you wish to retrieve the [matrix](mta://reference/misc/matrix.md) for.

### Optional Arguments

- **legacy:** Set to *false* to return correctly setup [matrix](mta://reference/misc/matrix.md) (i.e. Last column in the first 3 rows set to zero).

### Returns

Returns a multi-dimensional array (which can be transformed into a proper [matrix](mta://reference/misc/matrix.md) class using *Matrix.create* method) containing a 4x4 matrix. Returns *false* if the element is not streamed in, and not a [vehicle](mta://reference/misc/vehicle.md), [ped](mta://reference/misc/ped.md) or [object](mta://reference/misc/object.md).

## Example

This example creates a utility function that turns an offset into a position that is relative to the specified element.

```
function getPositionFromElementOffset(element,offX,offY,offZ)
    local m = getElementMatrix ( element )  -- Get the matrix
    local x = offX * m[1][1] + offY * m[2][1] + offZ * m[3][1] + m[4][1]  -- Apply transform
    local y = offX * m[1][2] + offY * m[2][2] + offZ * m[3][2] + m[4][2]
    local z = offX * m[1][3] + offY * m[2][3] + offZ * m[3][3] + m[4][3]
    return x, y, z                               -- Return the transformed point
end

-- Get the position of a point 3 units to the right of the element:
x,y,z = getPositionFromElementOffset(element,3,0,0)

-- Get the position of a point 2 units in front of the element:
x,y,z = getPositionFromElementOffset(element,0,2,0)

-- Get the position of a point 1 unit above the element:
x,y,z = getPositionFromElementOffset(element,0,0,1)
```

This example creates some more matrix utility functions

```
function getMatrixLeft(m)
    return m[1][1], m[1][2], m[1][3]
end
function getMatrixForward(m)
    return m[2][1], m[2][2], m[2][3]
end
function getMatrixUp(m)
    return m[3][1], m[3][2], m[3][3]
end
function getMatrixPosition(m)
    return m[4][1], m[4][2], m[4][3]
end

local mat = getElementMatrix(element)  -- Get the matrix
x,y,z = getMatrixLeft(mat)     -- Get the matrix left direction
x,y,z = getMatrixForward(mat)  -- Get the matrix forward direction
x,y,z = getMatrixUp(mat)       -- Get the matrix up direction
```

This example function allows you to get the element matrix of an element that is not streamed in.

```
function getElementMatrix(element)
    local rx, ry, rz = getElementRotation(element, "ZXY")
    rx, ry, rz = math.rad(rx), math.rad(ry), math.rad(rz)
    local matrix = {}
    matrix[1] = {}
    matrix[1][1] = math.cos(rz)*math.cos(ry) - math.sin(rz)*math.sin(rx)*math.sin(ry)
    matrix[1][2] = math.cos(ry)*math.sin(rz) + math.cos(rz)*math.sin(rx)*math.sin(ry)
    matrix[1][3] = -math.cos(rx)*math.sin(ry)
    matrix[1][4] = 1
    
    matrix[2] = {}
    matrix[2][1] = -math.cos(rx)*math.sin(rz)
    matrix[2][2] = math.cos(rz)*math.cos(rx)
    matrix[2][3] = math.sin(rx)
    matrix[2][4] = 1
	
    matrix[3] = {}
    matrix[3][1] = math.cos(rz)*math.sin(ry) + math.cos(ry)*math.sin(rz)*math.sin(rx)
    matrix[3][2] = math.sin(rz)*math.sin(ry) - math.cos(rz)*math.cos(ry)*math.sin(rx)
    matrix[3][3] = math.cos(rx)*math.cos(ry)
    matrix[3][4] = 1
	
    matrix[4] = {}
    matrix[4][1], matrix[4][2], matrix[4][3] = getElementPosition(element)
    matrix[4][4] = 1
	
    return matrix
end
```

Click to collapse [-]
Server side: Front to Front

-- create a Ped (0, 0, 5, 0) and put the player to 10 m of distance, front to front

```
function startedThisResource (res)
	if getThisResource() == res then
		local thePed = createPed ( 287, 0, 0, 5, 0)
		local matrix = getElementMatrix(thePed)
		nx = 0 * matrix[1][1] + 10 * matrix[2][1] + 0 * matrix[3][1] + 1 * matrix[4][1]
		ny = 0 * matrix[1][2] + 10 * matrix[2][2] + 0 * matrix[3][2] + 1 * matrix[4][2]
		nz = 0 * matrix[1][3] + 10 * matrix[2][3] + 0 * matrix[3][3] + 1 * matrix[4][3]
		for a, z in ipairs(getElementsByType("player")) do
			setElementPosition (z, nx, ny, nz)
			local playerX, playerY, playerZ = getElementPosition(z)
			local pedX, pedY, pedZ = getElementPosition(thePed)
			local rotZ = findRotation( playerX, playerY, pedX, pedY ) 
			setElementRotation(z, 0, 0, rotZ)
		end
	end
end
addEventHandler("onResourceStart", getRootElement(), startedThisResource)

function findRotation( x1, y1, x2, y2 ) 
    local t = -math.deg( math.atan2( x2 - x1, y2 - y1 ) )
    return t < 0 and t + 360 or t
end
```

## Changelog

| Version | Description |
| --- | --- |

| 1.3.0-9.04186 | Added legacy argument |
| --- | --- |

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

- getElementMatrix

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

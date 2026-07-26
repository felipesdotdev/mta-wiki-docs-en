---
doc_id: "mta-wiki:12695"
title: "GetColPolygonHeight"
source_title: "GetColPolygonHeight"
source_url: "https://wiki.multitheftauto.com/wiki/GetColPolygonHeight"
revision_id: 81297
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:08.619903+00:00"
---

# GetColPolygonHeight

This function is used to get the height of an existing [colshape polygon](mta://scripting/shared/functions/createcolpolygon.md).
By default, a colshape polygon is infinitely tall.

## Syntax

```
float, float getColPolygonHeight ( colshape shape )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[colshape](mta://reference/misc/colshape.md):getHeight(...)*

### Required Arguments

- **shape:** The [colshape](mta://reference/misc/colshape.md) polygon.

### Returns

Returns two [floats](mta://reference/misc/float.md), indicating the floor and ceiling of the colshape height, *false* if invalid arguments were passed.

## Example

Click to collapse [-]
Server

This example creates a polygon colshape and show height of it with command 'getpolyheight'.

```
-- Creates polygon colshape at 0, 0, 4
 local colPoly = createColPolygon ( -1.08, -0.05, 2.92, -0.05, -1.08, -4.05, -5.08, -0.05, -1.08, 3.95 )
 -- Set its height to 4 unit
 setColPolygonHeight ( colPoly, 2.32, 7.12 )
 
 function showPolyHeight ( player, command )
     -- Get element position
     local x, y = getElementPosition ( colPoly )
     -- Get table floor and ceil of the colshape height and unpack it
     local z, z1 = unpack ( getColPolygonHeight ( colPoly ) )
     local heights = z1 - z
     -- Output it in his chatbox
     outputChatBox( "The Polygon Colshape at "..x..", "..y.." height is "..heights, player, 255, 255, 0)
 end
 addCommandHandler ( "getpolyheight", showPolyHeight )
```

## See Also

- [addColPolygonPoint](mta://scripting/shared/functions/addcolpolygonpoint.md)

- [createColCircle](mta://scripting/shared/functions/createcolcircle.md)

- [createColCuboid](mta://scripting/shared/functions/createcolcuboid.md)

- [createColPolygon](mta://scripting/shared/functions/createcolpolygon.md)

- [createColRectangle](mta://scripting/shared/functions/createcolrectangle.md)

- [createColSphere](mta://scripting/shared/functions/createcolsphere.md)

- [createColTube](mta://scripting/shared/functions/createcoltube.md)

- getColPolygonHeight

- [getColPolygonPoints](mta://scripting/shared/functions/getcolpolygonpoints.md)

- [getColPolygonPointPosition](mta://scripting/shared/functions/getcolpolygonpointposition.md)

- [getColShapeType](mta://scripting/shared/functions/getcolshapetype.md)

- [getColShapeRadius](mta://scripting/shared/functions/getcolshaperadius.md)

- [getColShapeSize](mta://scripting/shared/functions/getcolshapesize.md)

- [isInsideColShape](mta://scripting/shared/functions/isinsidecolshape.md)

- [removeColPolygonPoint](mta://scripting/shared/functions/removecolpolygonpoint.md)

- [setColPolygonHeight](mta://scripting/shared/functions/setcolpolygonheight.md)

- [setColPolygonPointPosition](mta://scripting/shared/functions/setcolpolygonpointposition.md)

- [setColShapeRadius](mta://scripting/shared/functions/setcolshaperadius.md)

- [setColShapeSize](mta://scripting/shared/functions/setcolshapesize.md)

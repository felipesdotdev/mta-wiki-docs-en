---
doc_id: "mta-wiki:10225"
title: "GetColShapeType"
source_title: "GetColShapeType"
source_url: "https://wiki.multitheftauto.com/wiki/GetColShapeType"
revision_id: 63058
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.5"]
generated_at: "2026-07-26T16:15:08.697000+00:00"
---

# GetColShapeType

This function is used to retrieve the type of an colshape.

## Syntax

```
int getColShapeType ( colshape shape )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[colshape](mta://reference/misc/colshape.md):getShapeType(...)*

**Variable**: *.shapeType*

### Required Arguments

- **shape:** The [colshape](mta://reference/misc/colshape.md) you wish to get the type of.

### Returns

Returns *false* if invalid arguments were passed, or an [integer](mta://reference/misc/int.md) of the type of the colshape, which include:

- **0:** circle

- **1:** cuboid

- **2:** sphere

- **3:** rectangle

- **4:** polygon

- **5:** tube

## Example

This example outputs the type of all colshapes.

```
local circle = createColCircle(0, 0, 1)
local cubboid = createColCuboid(0, 0, 0, 0, 0, 0)
local sphere = createColSphere(0, 0, 0, 0)
local rectangle = createColRectangle(0, 0, 0, 0)
local polygon = createColPolygon(0, 0, 0, 0, 0, 0, 0, 0)
local tube = createColTube(0, 0, 0, 0, 0)

iprint("circle", getColShapeType(circle), circle:getShapeType(), circle.shapeType)
iprint("cubboid", getColShapeType(cubboid), cubboid:getShapeType(), cubboid.shapeType)
iprint("sphere", getColShapeType(sphere), sphere:getShapeType(), sphere.shapeType)
iprint("rectangle", getColShapeType(rectangle), rectangle:getShapeType(), rectangle.shapeType)
iprint("polygon", getColShapeType(polygon), polygon:getShapeType(), polygon.shapeType)
iprint("tube", getColShapeType(tube), tube:getShapeType(), tube.shapeType)
```

## See Also

- [addColPolygonPoint](mta://scripting/shared/functions/addcolpolygonpoint.md)

- [createColCircle](mta://scripting/shared/functions/createcolcircle.md)

- [createColCuboid](mta://scripting/shared/functions/createcolcuboid.md)

- [createColPolygon](mta://scripting/shared/functions/createcolpolygon.md)

- [createColRectangle](mta://scripting/shared/functions/createcolrectangle.md)

- [createColSphere](mta://scripting/shared/functions/createcolsphere.md)

- [createColTube](mta://scripting/shared/functions/createcoltube.md)

- [getColPolygonHeight](mta://scripting/shared/functions/getcolpolygonheight.md)

- [getColPolygonPoints](mta://scripting/shared/functions/getcolpolygonpoints.md)

- [getColPolygonPointPosition](mta://scripting/shared/functions/getcolpolygonpointposition.md)

- getColShapeType

- [getColShapeRadius](mta://scripting/shared/functions/getcolshaperadius.md)

- [getColShapeSize](mta://scripting/shared/functions/getcolshapesize.md)

- [isInsideColShape](mta://scripting/shared/functions/isinsidecolshape.md)

- [removeColPolygonPoint](mta://scripting/shared/functions/removecolpolygonpoint.md)

- [setColPolygonHeight](mta://scripting/shared/functions/setcolpolygonheight.md)

- [setColPolygonPointPosition](mta://scripting/shared/functions/setcolpolygonpointposition.md)

- [setColShapeRadius](mta://scripting/shared/functions/setcolshaperadius.md)

- [setColShapeSize](mta://scripting/shared/functions/setcolshapesize.md)

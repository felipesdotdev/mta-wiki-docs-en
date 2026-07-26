---
doc_id: "mta-wiki:12429"
title: "GetColShapeRadius"
source_title: "GetColShapeRadius"
source_url: "https://wiki.multitheftauto.com/wiki/GetColShapeRadius"
revision_id: 81244
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.7"]
generated_at: "2026-07-26T16:15:08.661377+00:00"
---

# GetColShapeRadius

This function is used to get the radius of a colshape. Valid types are [circle](mta://scripting/shared/functions/createcolcircle.md), [sphere](mta://scripting/shared/functions/createcolsphere.md) and [tube](mta://scripting/shared/functions/createcoltube.md).

## Syntax

```
float getColShapeRadius ( colshape shape )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[colshape](mta://reference/misc/colshape.md):getRadius(...)*

**Counterpart**: *[setColShapeRadius](mta://scripting/shared/functions/setcolshaperadius.md)*

### Required Arguments

- **shape:** The [colshape](mta://reference/misc/colshape.md) you wish to get the radius of.

### Returns

Returns a [float](mta://reference/misc/float.md) containing the radius of the colshape, *false* if an invalid colshape was passed.

## Example

```
TODO
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

- [getColShapeType](mta://scripting/shared/functions/getcolshapetype.md)

- getColShapeRadius

- [getColShapeSize](mta://scripting/shared/functions/getcolshapesize.md)

- [isInsideColShape](mta://scripting/shared/functions/isinsidecolshape.md)

- [removeColPolygonPoint](mta://scripting/shared/functions/removecolpolygonpoint.md)

- [setColPolygonHeight](mta://scripting/shared/functions/setcolpolygonheight.md)

- [setColPolygonPointPosition](mta://scripting/shared/functions/setcolpolygonpointposition.md)

- [setColShapeRadius](mta://scripting/shared/functions/setcolshaperadius.md)

- [setColShapeSize](mta://scripting/shared/functions/setcolshapesize.md)

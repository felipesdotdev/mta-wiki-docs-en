---
doc_id: "mta-wiki:12432"
title: "GetColShapeSize"
source_title: "GetColShapeSize"
source_url: "https://wiki.multitheftauto.com/wiki/GetColShapeSize"
revision_id: 81246
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.7"]
generated_at: "2026-07-26T16:15:08.677282+00:00"
---

# GetColShapeSize

This function is used to get the size of a colshape. Valid types are [rectangle](mta://scripting/shared/functions/createcolrectangle.md), [cuboid](mta://scripting/shared/functions/createcolcuboid.md) and [tube](mta://scripting/shared/functions/createcoltube.md).

## Syntax

```
float, float, float getColShapeSize ( colshape shape )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[colshape](mta://reference/misc/colshape.md):getSize(...)*

**Counterpart**: *[setColShapeSize](mta://scripting/shared/functions/setcolshapesize.md)*

### Required Arguments

- **shape:** The [colshape](mta://reference/misc/colshape.md) you wish to get the size of.

### Returns

Returns up to 3 [floats](mta://reference/misc/float.md) depending on the colshape type (see below), *false* if invalid arguments were passed.

- *cuboid:* width, depth, height.

- *rectangle:* width, height.

- *tube:* height.

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

- [getColShapeRadius](mta://scripting/shared/functions/getcolshaperadius.md)

- getColShapeSize

- [isInsideColShape](mta://scripting/shared/functions/isinsidecolshape.md)

- [removeColPolygonPoint](mta://scripting/shared/functions/removecolpolygonpoint.md)

- [setColPolygonHeight](mta://scripting/shared/functions/setcolpolygonheight.md)

- [setColPolygonPointPosition](mta://scripting/shared/functions/setcolpolygonpointposition.md)

- [setColShapeRadius](mta://scripting/shared/functions/setcolshaperadius.md)

- [setColShapeSize](mta://scripting/shared/functions/setcolshapesize.md)

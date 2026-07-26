---
doc_id: "mta-wiki:12444"
title: "GetColPolygonPoints"
source_title: "GetColPolygonPoints"
source_url: "https://wiki.multitheftauto.com/wiki/GetColPolygonPoints"
revision_id: 81251
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.7"]
---

# GetColPolygonPoints

This function is used to get all bound points in a [colshape polygon](mta://scripting/shared/functions/createcolpolygon.md).

## Syntax

```
table getColPolygonPoints ( colshape shape )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[colshape](https://wiki.multitheftauto.com/index.php?search=colshape):getPoints(...)*

### Required Arguments

- **shape:** The [colshape](https://wiki.multitheftauto.com/index.php?search=colshape) polygon you wish to get the points of.

### Returns

Returns a [table](mta://reference/misc/table.md) of coordinates, each coordinate being a [table](mta://reference/misc/table.md) containing the x and y position of a bound point, *false* if invalid arguments were passed.

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

- getColPolygonPoints

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

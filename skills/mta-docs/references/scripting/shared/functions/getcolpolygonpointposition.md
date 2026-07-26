---
doc_id: "mta-wiki:12443"
title: "GetColPolygonPointPosition"
source_title: "GetColPolygonPointPosition"
source_url: "https://wiki.multitheftauto.com/wiki/GetColPolygonPointPosition"
revision_id: 81250
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.7"]
---

# GetColPolygonPointPosition

This function is used to get the position of a bound point in a [colshape polygon](mta://scripting/shared/functions/createcolpolygon.md).

## Syntax

```
float, float getColPolygonPointPosition ( colshape shape, int index )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[colshape](https://wiki.multitheftauto.com/index.php?search=colshape):getPointPosition(...)*

**Counterpart**: *[setColPolygonPointPosition](mta://scripting/shared/functions/setcolpolygonpointposition.md)*

### Required Arguments

- **shape:** The [colshape](https://wiki.multitheftauto.com/index.php?search=colshape) polygon you wish to change.

- **index:** The index of the point you wish to retrieve. The points are indexed in order, with 1 being the first bound point.

### Returns

Returns two [floats](mta://reference/misc/float.md), x and y, indicating the position of the point, *false* if invalid arguments were passed.

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

- getColPolygonPointPosition

- [getColShapeType](mta://scripting/shared/functions/getcolshapetype.md)

- [getColShapeRadius](mta://scripting/shared/functions/getcolshaperadius.md)

- [getColShapeSize](mta://scripting/shared/functions/getcolshapesize.md)

- [isInsideColShape](mta://scripting/shared/functions/isinsidecolshape.md)

- [removeColPolygonPoint](mta://scripting/shared/functions/removecolpolygonpoint.md)

- [setColPolygonHeight](mta://scripting/shared/functions/setcolpolygonheight.md)

- [setColPolygonPointPosition](mta://scripting/shared/functions/setcolpolygonpointposition.md)

- [setColShapeRadius](mta://scripting/shared/functions/setcolshaperadius.md)

- [setColShapeSize](mta://scripting/shared/functions/setcolshapesize.md)

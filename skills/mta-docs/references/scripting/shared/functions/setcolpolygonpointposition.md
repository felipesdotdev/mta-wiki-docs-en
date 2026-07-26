---
doc_id: "mta-wiki:12442"
title: "SetColPolygonPointPosition"
source_title: "SetColPolygonPointPosition"
source_url: "https://wiki.multitheftauto.com/wiki/SetColPolygonPointPosition"
revision_id: 81249
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.7"]
---

# SetColPolygonPointPosition

This function is used to set the position of a bound point in a [colshape polygon](mta://scripting/shared/functions/createcolpolygon.md).

## Syntax

```
bool setColPolygonPointPosition ( colshape shape, int index, float fX, float fY )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[colshape](https://wiki.multitheftauto.com/index.php?search=colshape):setPointPosition(...)*

**Counterpart**: *[getColPolygonPointPosition](mta://scripting/shared/functions/getcolpolygonpointposition.md)*

### Required Arguments

- **shape:** The [colshape](https://wiki.multitheftauto.com/index.php?search=colshape) polygon you wish to change.

- **index:** The index of the point you wish to change. The points are indexed in order, with 1 being the first bound point.

- **fX:** The new X position of the bound point.

- **fY:** The new Y position of the bound point.

### Returns

Returns *true* if the polygon was changed, *false* if invalid arguments were passed.

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

- [getColShapeSize](mta://scripting/shared/functions/getcolshapesize.md)

- [isInsideColShape](mta://scripting/shared/functions/isinsidecolshape.md)

- [removeColPolygonPoint](mta://scripting/shared/functions/removecolpolygonpoint.md)

- [setColPolygonHeight](mta://scripting/shared/functions/setcolpolygonheight.md)

- setColPolygonPointPosition

- [setColShapeRadius](mta://scripting/shared/functions/setcolshaperadius.md)

- [setColShapeSize](mta://scripting/shared/functions/setcolshapesize.md)

---
doc_id: "mta-wiki:12428"
title: "SetColShapeRadius"
source_title: "SetColShapeRadius"
source_url: "https://wiki.multitheftauto.com/wiki/SetColShapeRadius"
revision_id: 81243
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.7"]
---

# SetColShapeRadius

This function is used to set the radius of a colshape. Valid types are [circle](mta://scripting/shared/functions/createcolcircle.md), [sphere](mta://scripting/shared/functions/createcolsphere.md) and [tube](mta://scripting/shared/functions/createcoltube.md).

## Syntax

```
bool setColShapeRadius ( colshape shape, float radius )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[colshape](https://wiki.multitheftauto.com/index.php?search=colshape):setRadius(...)*

**Counterpart**: *[getColShapeRadius](mta://scripting/shared/functions/getcolshaperadius.md)*

### Required Arguments

- **shape:** The [colshape](https://wiki.multitheftauto.com/index.php?search=colshape) you wish to change the radius of.

- **radius:** The radius you want to set.

### Returns

Returns *true* if the radius was changed, or *false* if invalid arguments were passed.

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

- [setColPolygonPointPosition](mta://scripting/shared/functions/setcolpolygonpointposition.md)

- setColShapeRadius

- [setColShapeSize](mta://scripting/shared/functions/setcolshapesize.md)

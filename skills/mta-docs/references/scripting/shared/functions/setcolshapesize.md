---
doc_id: "mta-wiki:12430"
title: "SetColShapeSize"
source_title: "SetColShapeSize"
source_url: "https://wiki.multitheftauto.com/wiki/SetColShapeSize"
revision_id: 81245
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.7"]
---

# SetColShapeSize

This function is used to set the size of a colshape. Valid types are [rectangle](mta://scripting/shared/functions/createcolrectangle.md), [cuboid](mta://scripting/shared/functions/createcolcuboid.md) and [tube](mta://scripting/shared/functions/createcoltube.md).

## Syntax (Cuboid)

```
bool setColShapeSize ( colshape shape, float width, float depth, float height )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[colshape](https://wiki.multitheftauto.com/index.php?search=colshape):setSize(...)*

**Counterpart**: *[getColShapeSize](mta://scripting/shared/functions/getcolshapesize.md)*

### Required Arguments

- **shape:** The [colshape](https://wiki.multitheftauto.com/index.php?search=colshape) you wish to change the size of.

- **width:** The collision cuboid's width.

- **depth:** The collision cuboid's depth.

- **height:** The collision cuboid's height.

## Syntax (Rectangle)

```
bool setColShapeSize ( colshape shape, float width, float height )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[colshape](https://wiki.multitheftauto.com/index.php?search=colshape):setSize(...)*

**Counterpart**: *[getColShapeSize](mta://scripting/shared/functions/getcolshapesize.md)*

### Required Arguments

- **shape:** The [colshape](https://wiki.multitheftauto.com/index.php?search=colshape) you wish to change the size of.

- **width:** The collision rectangle's width.

- **height:** The collision rectangle's height.

## Syntax (Tube)

```
bool setColShapeSize ( colshape shape, float height )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[colshape](https://wiki.multitheftauto.com/index.php?search=colshape):setSize(...)*

**Counterpart**: *[getColShapeSize](mta://scripting/shared/functions/getcolshapesize.md)*

### Required Arguments

- **height:** The collision tubes's height.

### Returns

Returns *true* if the size was changed, *false* if invalid arguments were passed.

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

- [setColShapeRadius](mta://scripting/shared/functions/setcolshaperadius.md)

- setColShapeSize

---
doc_id: "mta-wiki:12668"
title: "SetColPolygonHeight"
source_title: "SetColPolygonHeight"
source_url: "https://wiki.multitheftauto.com/wiki/SetColPolygonHeight"
revision_id: 81283
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# SetColPolygonHeight

This function is used to change the height of an existing [colshape polygon](mta://scripting/shared/functions/createcolpolygon.md).
By default, a colshape polygon is infinitely tall.

## Syntax

```
bool setColPolygonHeight( colshape shape, float floor, float ceil )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[colshape](https://wiki.multitheftauto.com/index.php?search=colshape):setHeight(...)*

### Required Arguments

- **shape:** The [colshape](https://wiki.multitheftauto.com/index.php?search=colshape) polygon.

- **floor:** The polygon floor (lowest Z coordinate). Parse *false* to reset this value to 0.

- **ceil:** The polygon ceiling (highest Z coordinate). Parse *false* to reset this value to infinitely tall.

### Returns

Returns *true* if the polygon was changed, *false* if invalid arguments were passed.

## Example

This example sets every polygon colshape's max heigh to 50 units once resource starts.

Click to collapse [-]
Server

```
function setPolygonsHeight ()
    for i, v in ipairs (getElementsByType ("colshape")) do
        if (getColShapeType (v) == 4) then -- if it's a polygon colshape do it otherwise don't
            setColPolygonHeight (v, false, 50)
        end
    end
end
addEventHandler ("onResourceStart", resourceRoot, setPolygonsHeight)
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

- setColPolygonHeight

- [setColPolygonPointPosition](mta://scripting/shared/functions/setcolpolygonpointposition.md)

- [setColShapeRadius](mta://scripting/shared/functions/setcolshaperadius.md)

- [setColShapeSize](mta://scripting/shared/functions/setcolshapesize.md)

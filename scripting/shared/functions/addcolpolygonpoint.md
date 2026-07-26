---
doc_id: "mta-wiki:12433"
title: "AddColPolygonPoint"
source_title: "AddColPolygonPoint"
source_url: "https://wiki.multitheftauto.com/wiki/AddColPolygonPoint"
revision_id: 81247
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.7", "Utility_templates"]
generated_at: "2026-07-26T16:10:20.062192+00:00"
---

# AddColPolygonPoint

This function is used to add a new point to an existing [colshape polygon](mta://scripting/shared/functions/createcolpolygon.md).

## Syntax

```
bool addColPolygonPoint ( colshape shape, float fX, float fY [, int index = 0 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[colshape](mta://reference/misc/colshape.md):addPoint(...)*

**Counterpart**: *[removeColPolygonPoint](mta://scripting/shared/functions/removecolpolygonpoint.md)*

### Required Arguments

- **shape:** The [colshape](mta://reference/misc/colshape.md) polygon you wish add a point to.

- **fX:** The X position of the new bound point.

- **fY:** The Y position of the new bound point.

## Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **index:** The index where the new point will be inserted in the polygon. The points are indexed in order, with 1 being the first bound point. Passing 0 will insert the point as the last one in the polygon.

### Returns

Returns *true* if the polygon was changed, *false* if invalid arguments were passed.

### Example

Click to collapse [-]
Server

This examples adds a point to an existing polygon shape by a command.

```
local shape = createColPolygon(2, 2, 5, 5, 6, 6, 8, 8) -- Somewhere in the map
function addPointToPolygon(plr, cmd, fX, fY, index)
    if (not fX or not fY) then
        outputChatBox("Correct syntax: /addpoint <fX fY>", plr, 255, 25, 25)
        return false
    end
    if (not index or index == 0) then
        addColPolygonPoint(shape, fX, fY)
    else
        addColPolygonPoint(shape, fX, fY, index)
    end
    outputChatBox("Point added", plr, 0, 255, 0)
end
addCommandHandler("addpoint", addPointToPolygon)
```

## See Also

- addColPolygonPoint

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

- [setColShapeSize](mta://scripting/shared/functions/setcolshapesize.md)

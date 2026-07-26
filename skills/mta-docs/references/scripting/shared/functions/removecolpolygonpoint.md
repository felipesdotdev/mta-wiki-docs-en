---
doc_id: "mta-wiki:12441"
title: "RemoveColPolygonPoint"
source_title: "RemoveColPolygonPoint"
source_url: "https://wiki.multitheftauto.com/wiki/RemoveColPolygonPoint"
revision_id: 81248
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.7"]
---

# RemoveColPolygonPoint

This function is used to remove a point from an existing [colshape polygon](mta://scripting/shared/functions/createcolpolygon.md).

## Syntax

```
bool removeColPolygonPoint ( colshape shape, int index )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[colshape](https://wiki.multitheftauto.com/index.php?search=colshape):removePoint(...)*

**Counterpart**: *[addColPolygonPoint](mta://scripting/shared/functions/addcolpolygonpoint.md)*

### Required Arguments

- **shape:** The [colshape](https://wiki.multitheftauto.com/index.php?search=colshape) polygon you wish to remove a point from.

- **index:** The index of the point you wish to remove. The points are indexed in order, with 1 being the first bound point. You can't remove the last 3 points.

### Returns

Returns *true* if the polygon was changed, *false* if invalid arguments were passed.

## Example

Click to collapse [-]
Server

This example remove a polygon colshape point by command 'removepoint'.

```
-- Creates polygon colshape at 0, 0, 4
local shape = createColPolygon ( -1.08, -0.05, 2.92, -0.05, -1.08, -4.05, -5.08, -0.05, -1.08, 3.95 )
function removePointToPolygon ( plr, cmd, index )
    if ( not index ) then
        -- if index argument after command is not there
        outputChatBox ( "Correct syntax: /removepoint <index>", plr, 255, 25, 25 )
        return false
    end
    -- Convert string to number 'index'
    local index = tonumber ( index )
    -- Get all polygon colshape points
    local indexes = #getColPolygonPoints ( shape )
    if ( index > indexes ) then
        outputChatBox("Index point is greater than last index "..indexes, plr, 255, 25, 25)
        return false
    else
        -- Remove polygon point at index
        removeColPolygonPoint(shape, index)
    end
    outputChatBox ( "Point at index "..index.." removed", plr, 0, 255, 0 )
end
addCommandHandler ( "removepoint", removePointToPolygon )
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

- removeColPolygonPoint

- [setColPolygonHeight](mta://scripting/shared/functions/setcolpolygonheight.md)

- [setColPolygonPointPosition](mta://scripting/shared/functions/setcolpolygonpointposition.md)

- [setColShapeRadius](mta://scripting/shared/functions/setcolshaperadius.md)

- [setColShapeSize](mta://scripting/shared/functions/setcolshapesize.md)

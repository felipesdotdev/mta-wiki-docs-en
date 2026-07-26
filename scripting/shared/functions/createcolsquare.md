---
doc_id: "mta-wiki:3302"
title: "CreateColRectangle"
source_title: "CreateColSquare"
source_url: "https://wiki.multitheftauto.com/wiki/CreateColSquare"
revision_id: 78549
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:10:38.121171+00:00"
---

# CreateColRectangle

This function creates a collision rectangle. This is a shape that has a position and a width and a depth. See [Rectangle](http://en.wikipedia.org/wiki/Rectangle) for a definition of a rectangle. XY marks on the south west corner of the colshape.

| [[{{{image}}}\|link=\|]] | Tip: To visualize a colshape when writing scripts, use the client console command showcol |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: Attaching a rectangle colshape to another element may give unexpected results as the origin is not at the rectangle centre. Try using a collision circle for attaching instead |
| --- | --- |
|  |  |

## Syntax

```
colshape createColRectangle ( float fX, float fY, float fWidth, float fHeight )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *ColShape.Rectangle(...)*

### Required Arguments

- **fX:** The X position of the collision rectangle's west side.

- **fY:** The Y position of the collision rectangle's south side.

- **fWidth:** The collision rectangle's width.

- **fHeight:** The collision rectangle's height.

### Returns

Returns a [colshape](mta://reference/misc/colshape.md) element if successful, *false* if invalid arguments were passed to the function.

## Example

Click to collapse [-]
Server

This example displays a chat message when a player enters the colshape and allows the colshape to be created using a console function *set_zone*.

```
local theZone

function shapeHit(thePlayer)
    outputChatBox(getPlayerName(thePlayer).. " is in the zone!")
end

function setZone(playerSource, commandName, fX, fY, fWidth, fHeight)
    local fX, fY, fWidth, fHeight = tonumber(fX), tonumber(fY), tonumber(fWidth), tonumber(fHeight)
    if (not fX) or (not fY) or (not fWidth) or (not fHeight) then
        outputChatBox("Syntax: /"..commandName.." [X] [Y] [Width] [Height]", playerSource)
    else
        if (theZone ~= nil) then
            destroyElement(theZone)
        end
        local tempCol = createColRectangle(fX, fY, fWidth, fHeight)
        addEventHandler("onColShapeHit", tempCol, shapeHit)
        outputChatBox("Zone has "..(theZone ~= nil and "moved" or "created").."!", playerSource)
        theZone = tempCol
    end
end
addCommandHandler("set_zone", setZone, false, false)
```

## See Also

- [addColPolygonPoint](mta://scripting/shared/functions/addcolpolygonpoint.md)

- [createColCircle](mta://scripting/shared/functions/createcolcircle.md)

- [createColCuboid](mta://scripting/shared/functions/createcolcuboid.md)

- [createColPolygon](mta://scripting/shared/functions/createcolpolygon.md)

- createColRectangle

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

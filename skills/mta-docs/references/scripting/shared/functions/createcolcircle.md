---
doc_id: "mta-wiki:1803"
title: "CreateColCircle"
source_title: "CreateColCircle"
source_url: "https://wiki.multitheftauto.com/wiki/CreateColCircle"
revision_id: 78557
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# CreateColCircle

This function creates a collision circle. This is a shape that has a position and a radius and infinite height that you can use to detect a player's presence. Events will be triggered when a player enters or leaves it.

| [[{{{image}}}\|link=\|]] | Tip: To visualize a colshape when writing scripts, use the client console command showcol |
| --- | --- |
|  |  |

## Syntax

```
colshape createColCircle ( float fX, float fY, float radius )
```

 

example

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *ColShape.Circle(...)*

### Required Arguments

- **fX:** The collision circle's center point's X axis position.

- **fY:** The collision circle's center point's Y axis position.

- **radius:** The radius of the collision circle. Can not be smaller than 0.1.

### Returns

Returns a [colshape](https://wiki.multitheftauto.com/index.php?search=colshape) element if successful, *false* if invalid arguments were passed to the function.

## Example

Click to collapse [-]
Server

This example displays a chat message when a player enters the colshape and allows the colshape to be created using a console function *set_zone*.

```
local theZone

function shapeHit(thePlayer)
    outputChatBox(getPlayerName(thePlayer).. " is in the zone!")
end

function setZone(playerSource, commandName, fX, fY, fRadius)
    local fX, fY, fRadius = tonumber(fX), tonumber(fY), tonumber(fRadius)
    if (not fX) or (not fY) or (not fRadius) then
        outputChatBox("Syntax: /"..commandName.." [X] [Y] [Radius]", playerSource)
    else
        if (theZone ~= nil) then
            destroyElement(theZone)
        end
        local tempCol = createColCircle(fX, fY, fRadius)
        addEventHandler("onColShapeHit", tempCol, shapeHit)
        outputChatBox("Zone has "..(theZone ~= nil and "moved" or "created").."!", playerSource)
        theZone = tempCol
    end
end
addCommandHandler("set_zone", setZone, false, false)
```

## See Also

- [addColPolygonPoint](mta://scripting/shared/functions/addcolpolygonpoint.md)

- createColCircle

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

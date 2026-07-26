---
doc_id: "mta-wiki:1807"
title: "CreateColTube"
source_title: "CreateColTube"
source_url: "https://wiki.multitheftauto.com/wiki/CreateColTube"
revision_id: 78556
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# CreateColTube

This function creates a collision tube. This is a shape that has a position and a 2D (X/Y) radius and a height. See [Cylinder](http://en.wikipedia.org/wiki/Cylinder_(geometry)) for a definition of a tube. A tube is similar to a colcircle, except that it has a limited height, this means you can limit the distance above the position defined by (fX, fY, fZ) that the collision is detected.

| [[{{{image}}}\|link=\|]] | Tip: To visualize a colshape when writing scripts, use the client console command showcol |
| --- | --- |
|  |  |

## Syntax

```
colshape createColTube ( float fX, float fY, float fZ, float fRadius, float fHeight )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *ColShape.Tube(...)*

### Required Arguments

- **fX:** The position of the base of the tube's center on the X axis.

- **fY:** The position of the base of the tube's center on the Y axis.

- **fZ:** The position of the base of the tube's center on the Z axis.

- **fRadius:** The collision tube's radius.

- **fHeight:** The collision tube's height.

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

function setZone(playerSource, commandName, fX, fY, fZ, fRadius, fHeight)
    local fX, fY, fZ, fRadius, fHeight = tonumber(fX), tonumber(fY), tonumber(fZ), tonumber(fRadius), tonumber(fHeight)
    if (not fX) or (not fY) or (not fZ) or (not fRadius) or (not fHeight) then
        outputChatBox("Syntax: /"..commandName.." [X] [Y] [Z] [Radius] [Height]", playerSource)
    else
        if (theZone ~= nil) then
            destroyElement(theZone)
        end
        local tempCol = createColTube(fX, fY, fZ, fRaduis, fHeight)
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

- [createColRectangle](mta://scripting/shared/functions/createcolrectangle.md)

- [createColSphere](mta://scripting/shared/functions/createcolsphere.md)

- createColTube

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

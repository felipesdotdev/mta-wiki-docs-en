---
doc_id: "mta-wiki:1858"
title: "CreateColCuboid"
source_title: "CreateColCuboid"
source_url: "https://wiki.multitheftauto.com/wiki/CreateColCuboid"
revision_id: 78788
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# CreateColCuboid

This function creates a collision cuboid. This is a shape that has a position, width, depth and height. See [Wikipedia](http://en.wikipedia.org/wiki/Cuboid) for a definition of a cuboid. The XYZ of the col starts at the southwest bottom corner of the shape.

| [[{{{image}}}\|link=\|]] | Tip: To visualize a colshape when writing scripts, use the client console command showcol |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: Attaching a cuboid colshape to another element may give unexpected results as the origin is not at the cuboid centre. Try using a collision sphere for attaching instead |
| --- | --- |
|  |  |

## Syntax

```
colshape createColCuboid ( float fX, float fY, float fZ, float fWidth, float fDepth, float fHeight )
```

 

A cuboid created using this function

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *ColShape.Cuboid(...)*

### Required Arguments

- **fX:** The X position of the collision cuboid's western side.

- **fY:** The Y position of the collision cuboid's southern side.

- **fZ:** The Z position of the collision cuboid's lowest side.

- **fWidth:** The collision cuboid's width.

- **fDepth:** The collision cuboid's depth.

- **fHeight:** The collision cuboid's height.

### Returns

Returns a [colshape](https://wiki.multitheftauto.com/index.php?search=colshape) element if successful, *false* if invalid arguments were passed to the function.

## Examples

Click to collapse [-]
Server

This example displays a chat message when a player enters the colshape and allows the colshape to be created using a console function *set_zone*.

```
local theZone

function shapeHit(thePlayer)
    outputChatBox(getPlayerName(thePlayer).. " is in the zone!")
end

function setZone(playerSource, commandName, fX, fY, fZ, fWidth, fDepth, fHeight)
    local fX, fY, fZ, fWidth, fDepth, fHeight = tonumber(fX), tonumber(fY), tonumber(fZ), tonumber(fWidth), tonumber(fDepth), tonumber(fHeight)
    if (not fX) or (not fY) or (not fZ) or (not fWidth) or (not fDepth) or (not fHeight) then
        outputChatBox("Syntax: /"..commandName.." [X] [Y] [Z] [Width] [Depth] [Height]", playerSource)
    else
        if (theZone ~= nil) then
            destroyElement(theZone)
        end
        local tempCol = createColCuboid(fX, fY, fZ, fWidth, fDepth, fHeight)
        addEventHandler("onColShapeHit", tempCol, shapeHit)
        outputChatBox("Zone has "..(theZone ~= nil and "moved" or "created").."!", playerSource)
        theZone = tempCol
    end
end
addCommandHandler("set_zone", setZone, false, false)
```

Click to collapse [-]
Server

This function creates a cuboid and centers it to given coordinates

```
addCommandHandler('createCenteredCuboid', function(player, cmd, posX, posY, posZ, sizeX, sizeY, sizeZ)
	posX = posX - sizeX / 2
	posY = posY - sizeY / 2
	posZ = posZ - sizeZ / 2
	createCuboid(posX, posY, posZ, sizeX, sizeY, sizeZ)
end)
```

## See Also

- [addColPolygonPoint](mta://scripting/shared/functions/addcolpolygonpoint.md)

- [createColCircle](mta://scripting/shared/functions/createcolcircle.md)

- createColCuboid

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

---
doc_id: "mta-wiki:4292"
title: "CreateColPolygon"
source_title: "CreateColPolygon"
source_url: "https://wiki.multitheftauto.com/wiki/CreateColPolygon"
revision_id: 73872
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# CreateColPolygon

| [[{{{image}}}\|link=\|]] | Note: For this function to work correctly, get/set your bound points in an anti-clockwise fashion. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: Even though this is a 2D colshape, isElementWithinColShape returns false if an element is in the area but below 0 Z height. |
| --- | --- |
|  |  |

This function creates a collision polygon. See [Wikipedia](http://en.wikipedia.org/wiki/Polygon) for a definition of a polygon. The first set of X Y of this shape is not part of the colshape bounds, so can set anywhere in the game world, however for performance, place it as close to the centre of the polygon as you can. It should be noted this shape is **2D**. There should be at least 3 bound points set.

| [[{{{image}}}\|link=\|]] | Tip: To visualize a colshape when writing scripts, use the client console command showcol |
| --- | --- |
|  |  |

## Syntax

```
colshape createColPolygon ( float fCenterX, float fCenterY, float fX1, float fY1, float fX2, float fY2, float fX3, float fY3, ... )
```

 

example

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *ColShape.Polygon(...)*

### Required Arguments

- **fCenterX:** The X position of the collision polygon's position - the position that will be returned from [getElementPosition](mta://scripting/shared/functions/getelementposition.md).

- **fCenterY:** The Y position of the collision polygon's position - the position that will be returned from [getElementPosition](mta://scripting/shared/functions/getelementposition.md).

- **fX1:** The 1st X position of the collision polygon's bound point

- **fY1:** The 1st Y position of the collision polygon's bound point

- **fX2:** The 2nd X position of the collision polygon's bound point

- **fY2:** The 2nd Y position of the collision polygon's bound point

- **fX3:** The 3rd X position of the collision polygon's bound point

- **fY3:** The 3rd Y position of the collision polygon's bound point

- **... :** From the 3rd position you can have as many points as you require to create the colshape.

### Returns

Returns a [colshape](https://wiki.multitheftauto.com/index.php?search=colshape) element if successful, *false* if invalid arguments were passed to the function.

## Example

Click to collapse [-]
Server

This example displays a chat message when any element hits the colshape and allows the colshape to be created using a console function *set_zone*.

```
local theZone = false

function shapeHit( element )
    local descriptor = "undefined"

    if getElementType( element ) == "player" then
        -- Use the player's name
        descriptor = getPlayerName( element )
    elseif getElementType( element ) == "vehicle" then
        -- Use the vehicle's model name
        descriptor = getVehicleName( element ) or descriptor
    end

    -- Output a message in the chat box for everyone on the server
    outputChatBox( descriptor .. " is in the zone!" )
end

function createZoneCommandHandler( playerSource, commandName, fX, fY, fX1, fY1, fX2, fY2, fX3, fY3, ... )
    -- Verify the player has given us the minimum amount of bound points
    if not ( fY and fX and fX1 and fY1 and fX2 and fX3 and fY3 ) then
        return outputChatBox( "Syntax: set_zone <X> <Y> <X1> <Y1> <X2> <Y2> <X3> <Y3> [<Xn> <Yn> ...]", playerSource, 255, 100, 100 )
    end

    -- Create the collision shape with the numbers from the arguments
    local tempCol = createColPolygon( fX, fY, fX1, fY1, fX2, fY2, fX3, fY3, ... )

    if not tempCol then
        return outputChatBox( "Error: Couldn't create collision polygon", playerSource, 255, 100, 100 )
    end

    -- Destroy the previous collision polygon shape in case we already have one
    if isElement( theZone ) then
        destroyElement( theZone )
    end

    -- Use a variable out-of-scope to keep track of the most recently created collision shape element
    theZone = tempCol

    -- Attach an event handler to the element to get notified whenever an element hits our collision shape
    addEventHandler( "onColShapeHit", tempCol, shapeHit, false )

    outputChatBox( "Success: Collision shape has been created!", playerSource, 100, 255, 100 )
end
addCommandHandler( "set_zone", createZoneCommandHandler )
```

Click to expand [+]
Server

This example displays a chat message when any element hits the colshape and allows the colshape to be created using a console function *set_wall*.

```
local theWall = false

function shapeHit( element )
    local descriptor = "undefined"

    if getElementType( element ) == "player" then
        -- Use the player's name
        descriptor = getPlayerName( element )
    elseif getElementType( element ) == "vehicle" then
        -- Use the vehicle's model name
        descriptor = getVehicleName( element ) or descriptor
    end

    -- Output a message in the chat box for everyone on the server
    outputChatBox( descriptor .. " is in the zone!" )
end

function createWallCommandHandler( playerSource, commandName, fromX, fromY, toX, toY )
    -- Verify the player has given us the minimum amount of bound points
    if not ( fromX and fromY and  toX and toY ) then
        return outputChatBox( "Syntax: set_wall <fromX> <fromY> <toX> <toY>", playerSource, 255, 100, 100 )
    end

    -- Calculate the 90° angle for the line between the two coordinates from the arguments
    local radian90DegreeAngle = math.atan2(toY - fromY, toX - fromX) + math.pi / 2

    -- Depth/width of the wall
    local depth = 1

    -- Pre-calculate the cosinus/sinus distances
    local cosinusDepth = math.cos(radian90DegreeAngle) * depth / 2
    local sinusDepth = math.sin(radian90DegreeAngle) * depth / 2

    -- Calculate the points in the game world
    local x1, y1 = fromX - cosinusDepth, fromY - sinusDepth
    local x2, y2 = toX - cosinusDepth, toY - sinusDepth
    local x3, y3 = toX + cosinusDepth, toY + sinusDepth
    local x4, y4 = fromX + cosinusDepth, fromY + sinusDepth

    -- Create the collision shape with the calculated numbers
    local tempCol = createColPolygon( fromX + (toX - fromX) / 2, fromY + (toY - fromY) / 2, x1, y1, x2, y2, x3, y3, x4, y4 )

    if not tempCol then
        return outputChatBox( "Error: Couldn't create collision polygon", playerSource, 255, 100, 100 )
    end

    -- Destroy the previous collision polygon shape in case we already have one
    if isElement( theWall ) then
        destroyElement( theWall )
    end

    -- Use a variable out-of-scope to keep track of the most recently created collision shape element
    theWall = tempCol

    -- Attach an event handler to the element to get notified whenever an element hits our collision shape
    addEventHandler( "onColShapeHit", tempCol, shapeHit, false )

    outputChatBox( "Success: Collision shape has been created!", playerSource, 100, 255, 100 )
end
addCommandHandler( "set_wall", createWallCommandHandler )
```

## See Also

- [addColPolygonPoint](mta://scripting/shared/functions/addcolpolygonpoint.md)

- [createColCircle](mta://scripting/shared/functions/createcolcircle.md)

- [createColCuboid](mta://scripting/shared/functions/createcolcuboid.md)

- createColPolygon

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

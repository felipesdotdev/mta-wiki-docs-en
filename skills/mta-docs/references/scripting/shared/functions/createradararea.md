---
doc_id: "mta-wiki:1568"
title: "CreateRadarArea"
source_title: "CreateRadarArea"
source_url: "https://wiki.multitheftauto.com/wiki/CreateRadarArea"
revision_id: 79913
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
---

# CreateRadarArea

This function can be used to create custom radar areas on the radar.

## Syntax

Click to collapse [-]
Server

```
radararea createRadarArea ( float startPosX, float startPosY, float sizeX, float sizeY, [ int r = 255, int g = 0, int b = 0, int a = 255, element visibleTo = root ] )
```

Click to collapse [-]
Client

```
radararea createRadarArea ( float startPosX, float startPosY, float sizeX, float sizeY, [ int r = 255, int g = 0, int b = 0, int a = 255 ] )
```

 

Radar Area on map

 

 

Radar Area on minimap

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[RadarArea](https://wiki.multitheftauto.com/index.php?search=RadarArea)(...)*

### Required Arguments

- **startPosX:** A float representing the origin 'x' position of the radar area.

- **startPosY:** A float representing the origin 'y' position of the radar area.

- **sizeX:** A float representing the width of the radar area.

- **sizeY:** A float representing the height of the radar area.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **r:** An integer representing the amount of red in the color.  Maximum value is 255

- **g:** An integer representing the amount of green in the color.  Maximum value is 255

- **b:** An integer representing the amount of blue in the color.  Maximum value is 255

- **a:** An integer representing the amount of alpha in the color.  This allows setting the transparency of the radar area.  255 is opaque and 0 is transparent.

- **visibleTo:** An [element](mta://reference/misc/element.md) that you wish to restrict the [visibility](mta://reference/misc/visibility.md) of the radar area to. (Server function only)

## Example

Click to collapse [-]
Server

This example creates a radar area for the King of the hill script, and a colsquare. When the player enters the radar area it flashes, and stops flashing when a player leaves it.

```
-- create our hill area for our gamemode
local hillArea = createColRectangle ( -2171.0678710938, 678.17950439453, 15, 15 )
local hillRadar = createRadarArea ( -2183.5678710938, 705.67950439453, 40, -40, 0, 255, 0, 175 )

-- add hill_Enter as a handler for when a player enters the hill area
function hill_Enter ( thePlayer, matchingDimension )
        -- announce to everyone that the player entered the hill
        if (getElementType(thePlayer) == "player") then
                outputChatBox( getPlayerName(thePlayer) .. " entered the zone!", root, 255, 255, 109 )
                setRadarAreaFlashing ( hillRadar, true )
        end
end
addEventHandler ( "onColShapeHit", hillArea, hill_Enter )

-- add hill_Enter as a handler for when a player leaves the hill area
function hill_Exit ( thePlayer, matchingDimension )
        -- check if the player is not dead
        if (getElementType(thePlayer) == "player") then
                if isPedDead ( thePlayer ) ~= true then
                        -- if he was alive, announce to everyone that the player has left the hill
                        outputChatBox ( getPlayerName(thePlayer) .. " left the zone!", root, 255, 255, 109 )
                        setRadarAreaFlashing ( hillRadar, false )
                end
        end
end
addEventHandler ( "onColShapeLeave", hillArea, hill_Exit )
```

## See Also

- createRadarArea

- [getRadarAreaColor](mta://scripting/shared/functions/getradarareacolor.md)

- [getRadarAreaSize](mta://scripting/shared/functions/getradarareasize.md)

- [isInsideRadarArea](mta://scripting/shared/functions/isinsideradararea.md)

- [isRadarAreaFlashing](mta://scripting/shared/functions/isradarareaflashing.md)

- [setRadarAreaColor](mta://scripting/shared/functions/setradarareacolor.md)

- [setRadarAreaFlashing](mta://scripting/shared/functions/setradarareaflashing.md)

- [setRadarAreaSize](mta://scripting/shared/functions/setradarareasize.md)

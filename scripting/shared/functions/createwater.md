---
doc_id: "mta-wiki:4337"
title: "CreateWater"
source_title: "CreateWater"
source_url: "https://wiki.multitheftauto.com/wiki/CreateWater"
revision_id: 73878
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:10:56.266866+00:00"
---

# CreateWater

Creates an area of [water](mta://reference/misc/water.md).

The largest possible size of a water area is 5996×5996. Also be aware that the function will change all x and y coordinates you specify into even integer numbers if necessary: this is because of a limitation of San Andreas.

You are able to give the water a shallow water effect, which practically changes the water invisible to the eye. However, all elements still work the same way as without the shallow effect - allowing swimming, diving, vehicles to sink, etc.

| [[{{{image}}}\|link=\|]] | Note: X and Y positions will be changed to an even integer. i.e. -2, 0, 2, 4 etc. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Important Note: If you're working with dimensions, be sure to apply it by using setElementDimension . |
| --- | --- |
|  |  |

## Syntax

```
water createWater ( float x1, float y1, float z1, float x2, float y2, float z2, float x3, float y3, float z3 [, float x4, float y4, float z4 ] [, bool bShallow = false ] )
```

 

Example of water quadrant.

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Water](mta://reference/misc/water.md)(...)*

### Required Arguments

- **x1, y1, z1:** position of bottom left (south-west) corner.

- **x2, y2, z2:** position of bottom right (south-east) corner.

- **x3, y3, z3:** position of top left (north-west) corner.

*Note: Only 3 coords creates a triangle*

### Optional Arguments

- **x4, y4, z4:** position of top right (north-east) corner.

- **bShallow:** gives the water a shallow water effect.

### Returns

Returns a water element if successful, *false* otherwise. The water element can be repositioned with [setElementPosition](mta://scripting/shared/functions/setelementposition.md) and destroyed with [destroyElement](mta://scripting/shared/functions/destroyelement.md).

## Example

Click to collapse [-]
Client

Example code for creating a water area to cover the entire San Andreas Map (flood the cities). Also, [setWaterLevel](mta://scripting/shared/functions/setwaterlevel.md) is used to raise the existing rivers and lakes.

```
-- Setting water properties.
height = 40
SizeVal = 2998
-- Defining variables.
southWest_X = -SizeVal
southWest_Y = -SizeVal
southEast_X = SizeVal
southEast_Y = -SizeVal
northWest_X = -SizeVal
northWest_Y = SizeVal
northEast_X = SizeVal
northEast_Y = SizeVal

-- OnClientResourceStart function that creates the water.
function thaResourceStarting( )
    water = createWater ( southWest_X, southWest_Y, height, southEast_X, southEast_Y, height, northWest_X, northWest_Y, height, northEast_X, northEast_Y, height )
    setWaterLevel ( height )
end
addEventHandler("onClientResourceStart", resourceRoot, thaResourceStarting)
```

Click to collapse [-]
Client

This example creates water at the given coordinates and sets the height of the water level to 20 for when the client joins.

```
function thaResourceStarting( )
    water = createWater ( 1866, -1444, 10, 1968, -1442, 10, 1866, -1372, 10, 1968, -1370, 10 )
    setWaterLevel ( water, 20 )
end
addEventHandler("onClientResourceStart", resourceRoot, thaResourceStarting)
```

Click to collapse [-]
Server

This example fills the Easter Basin with water.

```
function fillDock()
    waters = {
        createWater (-1612, 108, 0, -1550, 108, 0, -1612, 170, 0),
        createWater (-1733, 48, 0, -1612, 48, 0, -1612, 170, 0),
        createWater (-1673, 48, 0, -1612, 48, 0, -1673, -13, 0),
        createWater (-1612, 86, 0, -1574, 86, 0, -1612, 48, 0),
        createWater (-1612, 86, 0, -1574, 86, 0, -1612, 108, 0, -1574, 108, 0), -- Rectangle
        createWater (-1610, 168, 0, -1600, 168, 0, -1610, 170, 0, -1600, 170, 0), -- Rectangle
        createWater (-1612, 170, 0, -1610, 170, 0, -1610, 168, 0),
    }
end
addEventHandler ("onResourceStart", resourceRoot, fillDock)
```

## See Also

- [getWaterLevel](mta://scripting/client/functions/getwaterlevel.md)

- [isWaterDrawnLast](mta://scripting/client/functions/iswaterdrawnlast.md)

- [setWaterDrawnLast](mta://scripting/client/functions/setwaterdrawnlast.md)
  

- **Shared**

- createWater

- [getWaterColor](mta://scripting/shared/functions/getwatercolor.md)

- [getWaterVertexPosition](mta://scripting/shared/functions/getwatervertexposition.md)

- [getWaveHeight](mta://scripting/shared/functions/getwaveheight.md)

- [resetWaterColor](mta://scripting/shared/functions/resetwatercolor.md)

- [resetWaterLevel](mta://scripting/shared/functions/resetwaterlevel.md)

- [setWaterColor](mta://scripting/shared/functions/setwatercolor.md)

- [setWaterLevel](mta://scripting/shared/functions/setwaterlevel.md)

- [setWaterVertexPosition](mta://scripting/shared/functions/setwatervertexposition.md)

- [setWaveHeight](mta://scripting/shared/functions/setwaveheight.md)

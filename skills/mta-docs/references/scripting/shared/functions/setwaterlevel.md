---
doc_id: "mta-wiki:4333"
title: "SetWaterLevel"
source_title: "SetWaterLevel"
source_url: "https://wiki.multitheftauto.com/wiki/SetWaterLevel"
revision_id: 78313
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.2"]
---

# SetWaterLevel

Sets the height of some or all the water in the game world.

| [[{{{image}}}\|link=\|]] | Note: When the water level is 0, the standard GTA rendering is performed so that water is visible when viewed through translucent surfaces, such as vehicle windows. However, some MTA custom objects placed underwater will appear in front of the water. Setting the water level to any non-zero value (i.e. setWaterLevel(0.001) ) forces alternative rendering and MTA custom objects placed underwater will be drawn correctly. |
| --- | --- |
|  |  |

## Syntax

```
bool setWaterLevel ( [ water theWater, ] float level )
```

```
bool setWaterLevel ( float level [, bool includeWaterFeatures = true, bool includeWaterElements = true, bool includeWorldSea = true, bool includeOutsideWorldSea = false ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[water](https://wiki.multitheftauto.com/index.php?search=water):setLevel(...)*

**Variable**: *.level*

**Counterpart**: *[getWaterLevel](mta://scripting/client/functions/getwaterlevel.md)*

### Required Arguments

- **level:** the new Z coordinate of the water surface. All water in the game world is set to this height.

### Optional Arguments

- **theWater:** the water element to change.

*or:*

- **includeWaterFeatures :** a boolean indicating whether to also set the level of water features such as ponds and pools.

- **includeWaterElements :** a boolean indicating whether to also set the level of all water elements.

- **includeWorldSea :** a boolean indicating whether to set the level of the sea water

- **includeOutsideWorldSea:** a boolean indicating whether to also set the level of sea water outside the world area, ie. outside -3000, 3000.

### Returns

Returns *true* if successful, *false* in case of failure.

## Alternate client-only syntax

Click to collapse [-]
Client only

```
bool setWaterLevel ( [float x, float y, float z,] float level )
```

### Required Arguments

- **level:** the new Z coordinate of the water surface

### Optional Arguments

The area of water containing that point or corresponding to that water element is changed.

- **x:** the X coordinate of the point indicating the water area to change.

- **y:** the Y coordinate of the point indicating the water area to change.

- **z:** the Z coordinate of the point indicating the water area to change. This parameter is reserved and is currently ignored, set it to 0.

### Returns

Returns *true* if successful, *false* in case of failure (there is no water at the specified coordinates).

## Example

Click to collapse [-]
Client

This example code will slowly drain away all rivers and seas.

```
local level = 0

function drainSomeWater()
    level = level - 0.01
    setWaterLevel ( level )
end
setTimer ( drainSomeWater, 100, 15000 )
```

Click to collapse [-]
Server

This example code will slowly drain away all rivers and seas.

```
local level = 0

function drainSomeWater()
    level = level - 0.01
    setWaterLevel ( level )
end
setTimer ( drainSomeWater, 100, 15000 )
```

This example code adds a command *water* which can be used to change the current water level.

```
addCommandHandler ( "water",
    function ( thePlayer, command, level )
        if level and tonumber ( level ) then -- if we have input something and if it is actually a number value
            setWaterLevel ( tonumber( level ) ) -- change the water level
            outputChatBox ( "Waterlevel is now: " .. level ) -- send a message to everyone to inform about the change
        end
    end
)
```

## See Also

- [getWaterLevel](mta://scripting/client/functions/getwaterlevel.md)

- [isWaterDrawnLast](mta://scripting/client/functions/iswaterdrawnlast.md)

- [setWaterDrawnLast](mta://scripting/client/functions/setwaterdrawnlast.md)
  

- **Shared**

- [createWater](mta://scripting/shared/functions/createwater.md)

- [getWaterColor](mta://scripting/shared/functions/getwatercolor.md)

- [getWaterVertexPosition](mta://scripting/shared/functions/getwatervertexposition.md)

- [getWaveHeight](mta://scripting/shared/functions/getwaveheight.md)

- [resetWaterColor](mta://scripting/shared/functions/resetwatercolor.md)

- [resetWaterLevel](mta://scripting/shared/functions/resetwaterlevel.md)

- [setWaterColor](mta://scripting/shared/functions/setwatercolor.md)

- setWaterLevel

- [setWaterVertexPosition](mta://scripting/shared/functions/setwatervertexposition.md)

- [setWaveHeight](mta://scripting/shared/functions/setwaveheight.md)

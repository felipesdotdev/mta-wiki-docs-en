---
doc_id: "mta-wiki:4346"
title: "SetWaterVertexPosition"
source_title: "SetWaterVertexPosition"
source_url: "https://wiki.multitheftauto.com/wiki/SetWaterVertexPosition"
revision_id: 50919
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# SetWaterVertexPosition

Sets the world position of a corner point of a water area.

| [[{{{image}}}\|link=\|]] | Note: X and Y positions will be changed to an even integer. i.e. -2, 0, 2, 4 etc. |
| --- | --- |
|  |  |

## Syntax

```
bool setWaterVertexPosition ( water theWater, int vertexIndex, int x, int y, float z )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[water](https://wiki.multitheftauto.com/index.php?search=water):setVertexPosition(...)*

**Counterpart**: *[getWaterVertexPosition](mta://scripting/shared/functions/getwatervertexposition.md)*

### Required Arguments

- **theWater:** the water element of which to change a vertex.

- **vertexIndex:** the index of the vertex to move. Values range from 1 to 4 for water quads, and 1 to 3 for triangles.

- **x:** the X coordinate to set for the vertex.

- **y:** the Y coordinate to set for the vertex.

- **z:** the Z coordinate to set for the vertex.

### Returns

Returns *true* if successful, *false* otherwise.

## Example

Click to collapse [-]
Server

This example creates a water whose vertices 2 and 4 go up and down when someone uses the '/water' command.

```
waterSquare = createWater (1418, -625, 91.8, 1436, -625, 91.8, 1418, -613, 91.8, 1436, -613, 91.8)
local waterVertices = false

function waterUp ()
    if waterVertices == false then
        setWaterVertexPosition (waterSquare, 2, 1436, -625, 94.8)
        setWaterVertexPosition (waterSquare, 4, 1436, -613, 94.8)
        waterVertices = true
    else
        setWaterVertexPosition (waterSquare, 2, 1436, -625, 91.8)
        setWaterVertexPosition (waterSquare, 4, 1436, -613, 91.8)
        waterVertices = false
    end
end
addCommandHandler("water", waterUp)
```

## See Also

- [createWater](mta://scripting/shared/functions/createwater.md)

- [getWaterColor](mta://scripting/shared/functions/getwatercolor.md)

- [getWaterVertexPosition](mta://scripting/shared/functions/getwatervertexposition.md)

- [getWaveHeight](mta://scripting/shared/functions/getwaveheight.md)

- [resetWaterColor](mta://scripting/shared/functions/resetwatercolor.md)

- [resetWaterLevel](mta://scripting/shared/functions/resetwaterlevel.md)

- [setWaterColor](mta://scripting/shared/functions/setwatercolor.md)

- [setWaterLevel](mta://scripting/shared/functions/setwaterlevel.md)

- setWaterVertexPosition

- [setWaveHeight](mta://scripting/shared/functions/setwaveheight.md)

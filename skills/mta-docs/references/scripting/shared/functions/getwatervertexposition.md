---
doc_id: "mta-wiki:4345"
title: "GetWaterVertexPosition"
source_title: "GetWaterVertexPosition"
source_url: "https://wiki.multitheftauto.com/wiki/GetWaterVertexPosition"
revision_id: 73248
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetWaterVertexPosition

Gets the world position of a vertex (i.e. corner) of a [water](https://wiki.multitheftauto.com/index.php?search=water) area. Each water area is either a triangle or quad (rectangle) so each has 3 or 4 corners.

## Syntax

```
int int float getWaterVertexPosition ( water theWater, int vertexIndex )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[water](https://wiki.multitheftauto.com/index.php?search=water):getVertexPosition(...)*

**Counterpart**: *[setWaterVertexPosition](mta://scripting/shared/functions/setwatervertexposition.md)*

### Required Arguments

- **theWater:** the water element to get the vertex of

- **vertexIndex:** the index of the vertex whose position to get. Values range from 1 to 4 for a water quad, or 1 to 3 for a triangle.

### Returns

Returns the x, y and z coordinates of the specified vertex if successful, *false* otherwise.

## Example

```
function water()
	local water = createWater(1866, -1444, 10, 1968, -1442, 10, 1866, -1372, 10, 1968, -1370, 10); -- create water element
	
	local x, y, z = getWaterVertexPosition(water, 1); -- get first vertex position of our water element
	
	outputChatBox("Water first vertex position X: "..x.." Y: "..y.." Z: "..z);
end
```

## See Also

- [createWater](mta://scripting/shared/functions/createwater.md)

- [getWaterColor](mta://scripting/shared/functions/getwatercolor.md)

- getWaterVertexPosition

- [getWaveHeight](mta://scripting/shared/functions/getwaveheight.md)

- [resetWaterColor](mta://scripting/shared/functions/resetwatercolor.md)

- [resetWaterLevel](mta://scripting/shared/functions/resetwaterlevel.md)

- [setWaterColor](mta://scripting/shared/functions/setwatercolor.md)

- [setWaterLevel](mta://scripting/shared/functions/setwaterlevel.md)

- [setWaterVertexPosition](mta://scripting/shared/functions/setwatervertexposition.md)

- [setWaveHeight](mta://scripting/shared/functions/setwaveheight.md)

---
doc_id: "mta-wiki:4562"
title: "ResetWaterColor"
source_title: "ResetWaterColour"
source_url: "https://wiki.multitheftauto.com/wiki/ResetWaterColour"
revision_id: 48760
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:16:34.280568+00:00"
---

# ResetWaterColor

This function reset the water color of the GTA world to default.

## Syntax

```
bool resetWaterColor ( )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Water](mta://reference/misc/water.md).resetColor(...)*

### Returns

Returns *true* if water color was reset correctly, *false* otherwise.

## Example

This example adds a command *resetwatercolor* with which a player can reset the water colour.

```
function changeWaterBackToNormal ()
    resetWaterColor ()
end
addCommandHandler ( "resetwatercolor", changeWaterBackToNormal )
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

- resetWaterColor

- [resetWaterLevel](mta://scripting/shared/functions/resetwaterlevel.md)

- [setWaterColor](mta://scripting/shared/functions/setwatercolor.md)

- [setWaterLevel](mta://scripting/shared/functions/setwaterlevel.md)

- [setWaterVertexPosition](mta://scripting/shared/functions/setwatervertexposition.md)

- [setWaveHeight](mta://scripting/shared/functions/setwaveheight.md)

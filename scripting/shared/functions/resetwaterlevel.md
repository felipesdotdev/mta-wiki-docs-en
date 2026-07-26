---
doc_id: "mta-wiki:6010"
title: "ResetWaterLevel"
source_title: "ResetWaterLevel"
source_url: "https://wiki.multitheftauto.com/wiki/ResetWaterLevel"
revision_id: 81047
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:16:34.292124+00:00"
---

# ResetWaterLevel

This function resets the water of the GTA world back to its default level. [Water elements](mta://reference/misc/water.md) are not affected.

## Syntax

```
bool resetWaterLevel ()
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Water](mta://reference/misc/water.md).resetLevel(...)*

### Returns

Returns *true* if water level was reset correctly, *false* otherwise.

## Example

This example adds a command *resetwaterlevel* with which a player can reset the water level.

```
function changeWaterLevelBackToNormal ()
    resetWaterLevel ()
end
addCommandHandler ( "resetwaterlevel", changeWaterLevelBackToNormal )
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

- resetWaterLevel

- [setWaterColor](mta://scripting/shared/functions/setwatercolor.md)

- [setWaterLevel](mta://scripting/shared/functions/setwaterlevel.md)

- [setWaterVertexPosition](mta://scripting/shared/functions/setwatervertexposition.md)

- [setWaveHeight](mta://scripting/shared/functions/setwaveheight.md)

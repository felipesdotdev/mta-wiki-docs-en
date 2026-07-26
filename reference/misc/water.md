---
doc_id: "mta-wiki:4388"
title: "Element/Water"
source_title: "Water"
source_url: "https://wiki.multitheftauto.com/wiki/Water"
revision_id: 70675
language: "en"
categories: ["Element_Types"]
generated_at: "2026-07-26T16:16:54.729739+00:00"
---

# Element/Water

In San Andreas, the water in the game world (rivers, lakes, seas) is defined through a large number of water polygons, which can be quadrilateral or triangular. A water element represents one such polygon. You can create water elements with [createWater](mta://scripting/shared/functions/createwater.md) or through a <water/> map element.

## XML syntax

```
<water posX1="" posY1="" posZ1="" posX2="" posY2="" posZ2="" posX3="" posY3="" posZ3="" [ posX4="" posY4="" posZ4="" ] />
```

### Required Attributes

- **posX1, posY1, posZ1:** the position of the lower left (south-west) corner of the water surface.

- **posX2, posY2, posZ2:** the position of the lower right (south-east) corner of the water surface.

- **posX3, posY3, posZ3:** the position of the upper left (north-west) corner of the water surface.

### Optional Attributes

- **posX4, posY4, posZ4:** the position of the upper right (north-east) corner of the water surface.

If only the first three corners are specified, a water triangle is created. If the fourth corner is also specified, a rectangle is created.

## Related scripting functions

### Server

- [createWater](mta://scripting/shared/functions/createwater.md)

- [getWaterColor](mta://scripting/shared/functions/getwatercolor.md)

- [getWaterVertexPosition](mta://scripting/shared/functions/getwatervertexposition.md)

- [getWaveHeight](mta://scripting/shared/functions/getwaveheight.md)

- [resetWaterColor](mta://scripting/shared/functions/resetwatercolor.md)

- [resetWaterLevel](mta://scripting/shared/functions/resetwaterlevel.md)

- [setWaterColor](mta://scripting/shared/functions/setwatercolor.md)

- [setWaterLevel](mta://scripting/shared/functions/setwaterlevel.md)

- [setWaterVertexPosition](mta://scripting/shared/functions/setwatervertexposition.md)

- [setWaveHeight](mta://scripting/shared/functions/setwaveheight.md)

### Client

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

- [setWaterLevel](mta://scripting/shared/functions/setwaterlevel.md)

- [setWaterVertexPosition](mta://scripting/shared/functions/setwatervertexposition.md)

- [setWaveHeight](mta://scripting/shared/functions/setwaveheight.md)

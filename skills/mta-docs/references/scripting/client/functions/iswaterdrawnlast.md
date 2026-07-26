---
doc_id: "mta-wiki:6784"
title: "IsWaterDrawnLast"
source_title: "IsWaterDrawnLast"
source_url: "https://wiki.multitheftauto.com/wiki/IsWaterDrawnLast"
revision_id: 81148
language: "en"
categories: ["Client_functions", "Changes_in_1.3.0"]
---

# IsWaterDrawnLast

This function determines whether [water](https://wiki.multitheftauto.com/index.php?search=water) is drawn last in the rendering order.

## Syntax

```
bool isWaterDrawnLast ( )
```

### Returns

Returns *true* if water is drawn last in the rendering order, *false* otherwise.

## Example

This example toggles water to be drawn last.

```
function toggleWaterDrawnLast ()
    local bWaterDrawnLast = not isWaterDrawnLast()
    outputChatBox (string.format('setWaterDrawnLast: %s', tostring(bWaterDrawnLast)))
    return setWaterDrawnLast (bWaterDrawnLast)
end
addCommandHandler ('togglewater', toggleWaterDrawnLast)
```

## See Also

- [getWaterLevel](mta://scripting/client/functions/getwaterlevel.md)

- isWaterDrawnLast

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

---
doc_id: "mta-wiki:6783"
title: "SetWaterDrawnLast"
source_title: "SetWaterDrawnLast"
source_url: "https://wiki.multitheftauto.com/wiki/SetWaterDrawnLast"
revision_id: 81147
language: "en"
categories: ["Client_functions", "Changes_in_1.3.0"]
generated_at: "2026-07-26T16:16:49.553861+00:00"
---

# SetWaterDrawnLast

This function changes the [water](mta://reference/misc/water.md) rendering order.

## Syntax

```
bool setWaterDrawnLast ( bool bEnabled )
```

### Required Arguments

- **bEnabled**: A boolean value determining whether water should be drawn last.

### Returns

Returns *true* if the rendering order was changed successfully, *false* otherwise.

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

- [isWaterDrawnLast](mta://scripting/client/functions/iswaterdrawnlast.md)

- setWaterDrawnLast
  

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

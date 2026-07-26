---
doc_id: "mta-wiki:2695"
title: "GetWaveHeight"
source_title: "GetWaveHeight"
source_url: "https://wiki.multitheftauto.com/wiki/GetWaveHeight"
revision_id: 48776
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:30.008391+00:00"
---

# GetWaveHeight

This function returns the current wave height.

## Syntax

```
float getWaveHeight()
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Water](mta://reference/misc/water.md).getWaveHeight(...)*

**Counterpart**: *[setWaveHeight](mta://scripting/shared/functions/setwaveheight.md)*

### Returns

Returns the height as a [float](mta://reference/misc/float.md), *false* otherwise.

## Example

Click to collapse [-]
Server

This example changes the wave height to the given amount.

```
function scriptWave ( thePlayer, command, height )
	local oldHeight = getWaveHeight()
	height = tonumber ( height )
	success = setWaveHeight ( height )
	if ( success ) then
		outputChatBox ( "The old wave height was: " .. oldHeight .. "; " .. getPlayerName ( thePlayer ) .. " set it to: " .. height )
	else
		outputChatBox ( "Invalid number." )
	end
end
addCommandHandler ( "setwave", scriptWave )
```

## See Also

- [createWater](mta://scripting/shared/functions/createwater.md)

- [getWaterColor](mta://scripting/shared/functions/getwatercolor.md)

- [getWaterVertexPosition](mta://scripting/shared/functions/getwatervertexposition.md)

- getWaveHeight

- [resetWaterColor](mta://scripting/shared/functions/resetwatercolor.md)

- [resetWaterLevel](mta://scripting/shared/functions/resetwaterlevel.md)

- [setWaterColor](mta://scripting/shared/functions/setwatercolor.md)

- [setWaterLevel](mta://scripting/shared/functions/setwaterlevel.md)

- [setWaterVertexPosition](mta://scripting/shared/functions/setwatervertexposition.md)

- [setWaveHeight](mta://scripting/shared/functions/setwaveheight.md)

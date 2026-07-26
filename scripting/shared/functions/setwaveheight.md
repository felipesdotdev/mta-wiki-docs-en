---
doc_id: "mta-wiki:2696"
title: "SetWaveHeight"
source_title: "SetWaveHeight"
source_url: "https://wiki.multitheftauto.com/wiki/SetWaveHeight"
revision_id: 48777
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:16:49.608193+00:00"
---

# SetWaveHeight

This function sets the wave height to the desired value, the default is 0.

## Syntax

```
bool setWaveHeight ( float height )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Water](mta://reference/misc/water.md).setWaveHeight(...)*

**Counterpart**: *[getWaveHeight](mta://scripting/shared/functions/getwaveheight.md)*

### Required Arguments

- **height:** A float between 0 and 100.

## Returns

Returns a boolean value *true* or *false* that tells you if it was successful or not.

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

- [getWaveHeight](mta://scripting/shared/functions/getwaveheight.md)

- [resetWaterColor](mta://scripting/shared/functions/resetwatercolor.md)

- [resetWaterLevel](mta://scripting/shared/functions/resetwaterlevel.md)

- [setWaterColor](mta://scripting/shared/functions/setwatercolor.md)

- [setWaterLevel](mta://scripting/shared/functions/setwaterlevel.md)

- [setWaterVertexPosition](mta://scripting/shared/functions/setwatervertexposition.md)

- setWaveHeight

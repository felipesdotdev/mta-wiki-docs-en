---
doc_id: "mta-wiki:2596"
title: "GetWaterLevel"
source_title: "GetWaterLevel"
source_url: "https://wiki.multitheftauto.com/wiki/GetWaterLevel"
revision_id: 73884
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:15:29.985400+00:00"
---

# GetWaterLevel

This function allows you to retrieve the water level from a certain location. The water level is 0 in most places though it can vary (e.g. it's higher near the dam).

| [[{{{image}}}\|link=\|]] | Note: Some small water areas within parts of the city do not count as water to be used with this function. For example, the shallow water area in Northwest San Fierro. |
| --- | --- |
|  |  |

## Syntax

```
float getWaterLevel ( float posX, float posY, float posZ [ , bool ignoreDistanceToWaterThreshold = false ] )
```

```
float getWaterLevel ( water theWater )
```

### Required Arguments

- **x:** The X axis position

- **y:** The Y axis position

- **z:** The Z axis position

*or:*

- **theWater:** the water element

### Optional Arguments

- **ignoreDistanceToWaterThreshold:** If set to false, this function returns false, if the difference between water level (without waves) and posZ is greater than 3.0

### Returns

Returns an *integer* of the water level if the [localPlayer](mta://scripting/client/functions/localplayer.md)/position is near the water (-3 to 20 on the Z coordinate) else *false* if there's no water near the [localPlayer](mta://scripting/client/functions/localplayer.md)/position.

## Example

This example will tell you what's the water level where the specified player is located.

```
function scriptGetLevel ( command, playername ) --when getlevel is called
  local thePlayer = getPlayerFromName ( playername ) --get the player from nickname
  if ( thePlayer ~= false ) then --if there is a player from the nickname
    local x, y, z = getElementPosition ( thePlayer ) -- get his position
    local level = getWaterLevel ( x, y, z )
	  if level then -- if it's not false
        level = z - level -- calculate how far away is he from the water
        outputChatBox( "You are " .. level .. " units away from the water!", source )
	  else outputChatBox ( "There's no sign of water" )
	  end
  else outputChatBox ( "Player does not exist" )
  end
end
addCommandHandler( "getlevel", scriptGetLevel ) -- add a command "getloc" which
```

## See Also

- getWaterLevel

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

---
doc_id: "mta-wiki:5474"
title: "GetWaterColor"
source_title: "GetWaterColor"
source_url: "https://wiki.multitheftauto.com/wiki/GetWaterColor"
revision_id: 48772
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:29.961110+00:00"
---

# GetWaterColor

This function returns the water color of the GTA world.

**Note:** The server can only return the water color, if it has actually been set by script.

## Syntax

```
int, int, int, int getWaterColor ( )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[water](mta://reference/misc/water.md):getColor(...)*

**Counterpart**: *[setWaterColor](mta://scripting/shared/functions/setwatercolor.md)*

### Returns

Returns 4 [ints](mta://reference/misc/int.md), indicating the color of the water. (RGBA)

## Example

These two examples adds the command *watercolor* which get water color(RGBA) and show in chat.

Click to collapse [-]
Client

```
function waterColor ()
    local r,g,b,a = getWaterColor ()
    if ( r and g and b and a ) then -- If color is true
          -- Output of the value of the water color to the chat
        outputChatBox ( "The color of water is: "..math.ceil(r)..", "..math.ceil(g)..", "..math.ceil(b)..", "..math.ceil(a).."", r, g, b )
    else
          -- Notify the player if the value of the colors is false
        outputChatBox ( "Failed to get the color of water!" )
    end
end
  -- Add command handler for the function
addCommandHandler("watercolor", waterColor )
```

Click to collapse [-]
Server

```
function waterColor ()
	local r,g,b,a = getWaterColor ()
	if ( r and g and b and a ) then -- If color is true
          -- Output of the value of the water color to the chat
		outputChatBox ( "The color of water is: "..math.ceil(r)..", "..math.ceil(g)..", "..math.ceil(b)..", "..math.ceil(a).."", getRootElement(), r, g, b )
    else
          -- Notify the player if the value of the colors is false
        outputChatBox ( "Failed to get the color of water!" )
    end
end
  -- Add command handler for the function
addCommandHandler("watercolor", waterColor )
```

## See Also

- [getWaterLevel](mta://scripting/client/functions/getwaterlevel.md)

- [isWaterDrawnLast](mta://scripting/client/functions/iswaterdrawnlast.md)

- [setWaterDrawnLast](mta://scripting/client/functions/setwaterdrawnlast.md)
  

- **Shared**

- [createWater](mta://scripting/shared/functions/createwater.md)

- getWaterColor

- [getWaterVertexPosition](mta://scripting/shared/functions/getwatervertexposition.md)

- [getWaveHeight](mta://scripting/shared/functions/getwaveheight.md)

- [resetWaterColor](mta://scripting/shared/functions/resetwatercolor.md)

- [resetWaterLevel](mta://scripting/shared/functions/resetwaterlevel.md)

- [setWaterColor](mta://scripting/shared/functions/setwatercolor.md)

- [setWaterLevel](mta://scripting/shared/functions/setwaterlevel.md)

- [setWaterVertexPosition](mta://scripting/shared/functions/setwatervertexposition.md)

- [setWaveHeight](mta://scripting/shared/functions/setwaveheight.md)

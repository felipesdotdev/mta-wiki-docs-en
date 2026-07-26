---
doc_id: "mta-wiki:4560"
title: "SetWaterColor"
source_title: "SetWaterColor"
source_url: "https://wiki.multitheftauto.com/wiki/SetWaterColor"
revision_id: 48773
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
---

# SetWaterColor

This function changes the water color of the GTA world.

## Syntax

```
bool setWaterColor ( int red, int green, int blue, [ int alpha = 200 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[water](https://wiki.multitheftauto.com/index.php?search=water):setColor(...)*

**Counterpart**: *[getWaterColor](mta://scripting/shared/functions/getwatercolor.md)*

### Required Arguments

- **red:** The *red* value of the water, from 0 to 255.

- **green:** The *green* value of the water, from 0 to 255.

- **blue:** The *blue* value of the water, from 0 to 255.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **alpha:** The *alpha* (visibility) value of the water, from 0 to 255. Defaults to 200 if not declared.

### Returns

Returns *true* if water color was set correctly, *false* if invalid values were passed.

## Example

This example adds a command *watercolor* with which a player can change the water colour.

```
function changeWaterColor ( commandName, red, green, blue, alpha )
    -- if alpha is input, then include it too
    alpha = tonumber ( alpha ) or 200
    red = tonumber ( red )
    green = tonumber ( green )
    blue = tonumber ( blue )
    -- check if the colour values for red, green and blue are valid
    if red and green and blue then
        setWaterColor ( red, green, blue, alpha )
    else
        outputChatBox ( "Failed to change the water colour!" )
    end
end
addCommandHandler ( "watercolor", changeWaterColor )
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

- [resetWaterLevel](mta://scripting/shared/functions/resetwaterlevel.md)

- setWaterColor

- [setWaterLevel](mta://scripting/shared/functions/setwaterlevel.md)

- [setWaterVertexPosition](mta://scripting/shared/functions/setwatervertexposition.md)

- [setWaveHeight](mta://scripting/shared/functions/setwaveheight.md)

---
doc_id: "mta-wiki:1477"
title: "SetBlipColor"
source_title: "SetBlipColor"
source_url: "https://wiki.multitheftauto.com/wiki/SetBlipColor"
revision_id: 63355
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# SetBlipColor

This function will let you change the color of a blip. This color is only applicable to the default blip icon (,  or ). All other icons will ignore this.

## Syntax

```
bool setBlipColor ( blip theBlip, int red, int green, int blue, int alpha )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[blip](https://wiki.multitheftauto.com/index.php?search=blip):setColor(...)*

**Counterpart**: *[getBlipColor](mta://scripting/shared/functions/getblipcolor.md)*

### Required Arguments

- **theBlip:** The blip who's color you wish to set.

- **red:** The amount of red in the blip's color (0 - 255).

- **green:** The amount of green in the blip's color (0 - 255).

- **blue:** The amount of blue in the blip's color (0 - 255).

- **alpha:** The amount of alpha in the blip's color (0 - 255).  Alpha decides transparancy where 255 is opaque and 0 is transparent.

### Returns

Returns *true* if the blip's color was set successfully. Returns *false* if the blip passed to the function is invalid, or any of the colors are out of the valid range.

## Example

This example will find all the blips that exist and set them all to white if they aren't white already.

```
-- Retrieve a table containing all the blips that exist
local blips = getElementsByType ( "blip" )
-- Loop through the list, storing the blip from the table in the variable blipValue
for blipKey, blipValue in ipairs ( blips ) do
	-- Retrieve the blip's colors into the variables red, green, blue and alpha
	local red, green, blue, alpha = getBlipColor ( blipValue )
	-- If the blip's icon isn't white already
	if ( red ~= 255 or green ~= 255 or blue ~= 255 or alpha ~= 255 ) then
		-- Set the blip's color to white
		setBlipColor ( blipValue, 255, 255, 255, 255 )
	end
end
```

## See Also

- [createBlip](mta://scripting/shared/functions/createblip.md)

- [createBlipAttachedTo](mta://scripting/shared/functions/createblipattachedto.md)

- [getBlipColor](mta://scripting/shared/functions/getblipcolor.md)

- [getBlipIcon](mta://scripting/shared/functions/getblipicon.md)

- [getBlipOrdering](mta://scripting/shared/functions/getblipordering.md)

- [getBlipSize](mta://scripting/shared/functions/getblipsize.md)

- [getBlipVisibleDistance](mta://scripting/shared/functions/getblipvisibledistance.md)

- setBlipColor

- [setBlipIcon](mta://scripting/shared/functions/setblipicon.md)

- [setBlipOrdering](mta://scripting/shared/functions/setblipordering.md)

- [setBlipSize](mta://scripting/shared/functions/setblipsize.md)

- [setBlipVisibleDistance](mta://scripting/shared/functions/setblipvisibledistance.md)

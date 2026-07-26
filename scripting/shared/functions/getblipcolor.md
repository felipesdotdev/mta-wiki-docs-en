---
doc_id: "mta-wiki:1476"
title: "GetBlipColor"
source_title: "GetBlipColor"
source_url: "https://wiki.multitheftauto.com/wiki/GetBlipColor"
revision_id: 63323
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:07.505084+00:00"
---

# GetBlipColor

This function will tell you what color a blip is. This color is only applicable to the default blip icon (,  or ). All other icons will ignore this.

## Syntax

```
int int int int getBlipColor ( blip theBlip )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[blip](mta://reference/misc/blip.md):getColor(...)*

**Counterpart**: *[setBlipColor](mta://scripting/shared/functions/setblipcolor.md)*

### Required Arguments

- **theBlip:** The blip whose color you wish to get.

### Returns

Returns four integers in RGBA format, with a maximum value of 255 for each. The values are, in order, *red*, *green*, *blue*, and *alpha*.  Alpha decides the transparancy where 255 is opaque and 0 is fully transparent. *false* is returned if the blip is invalid.

## Example

This example will find all the blips that exist and set them all to white if they aren't white already.

```
-- Retrieve a table containing all the blips that exist
blips = getElementsByType ( "blip" )
-- Loop through the list, storing the blip from the table in the variable blipValue
for blipKey, blipValue in ipairs(blips) do
	-- Retrieve the blip's colors into the variables red, green, blue and alpha
	red, green, blue, alpha = getBlipColor ( blipValue )
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

- getBlipColor

- [getBlipIcon](mta://scripting/shared/functions/getblipicon.md)

- [getBlipOrdering](mta://scripting/shared/functions/getblipordering.md)

- [getBlipSize](mta://scripting/shared/functions/getblipsize.md)

- [getBlipVisibleDistance](mta://scripting/shared/functions/getblipvisibledistance.md)

- [setBlipColor](mta://scripting/shared/functions/setblipcolor.md)

- [setBlipIcon](mta://scripting/shared/functions/setblipicon.md)

- [setBlipOrdering](mta://scripting/shared/functions/setblipordering.md)

- [setBlipSize](mta://scripting/shared/functions/setblipsize.md)

- [setBlipVisibleDistance](mta://scripting/shared/functions/setblipvisibledistance.md)

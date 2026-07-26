---
doc_id: "mta-wiki:1469"
title: "GetBlipIcon"
source_title: "GetBlipIcon"
source_url: "https://wiki.multitheftauto.com/wiki/GetBlipIcon"
revision_id: 63326
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:07.516798+00:00"
---

# GetBlipIcon

This function returns the icon a [blip](mta://reference/misc/blip.md) currently has.

## Syntax

```
int getBlipIcon ( blip theBlip )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[blip](mta://reference/misc/blip.md):getIcon(...)*

**Variable**: *.icon*

**Counterpart**: *[setBlipIcon](mta://scripting/shared/functions/setblipicon.md)*

### Required Arguments

- **theBlip**: the blip we're getting the icon number of.

### Returns

Returns an [int](mta://reference/misc/int.md) indicating which icon the blip has. Valid values are listed on the [Radar Blips](mta://reference/misc/radar-blips.md) page.

## Example

This example will find all the blips that exist and set them all to the default blip icon.

```
-- Retrieve a table containing all the blips that exist
blips = getElementsByType ( "blip" )
-- Loop through the list, storing the blip from the table in the variable blipValue
for blipKey, blipValue in ipairs(blips) do
	-- Retrieve the blip's icon into the variable 'blipIcon'
	blipIcon = getBlipIcon ( blipValue )
	-- If the blip's icon wasn't the default already
	if ( blipIcon ~= 0 ) then
		-- Set the blip's icon to the default
		setBlipIcon ( blipValue, 0 )
	end
end
```

## See Also

- [createBlip](mta://scripting/shared/functions/createblip.md)

- [createBlipAttachedTo](mta://scripting/shared/functions/createblipattachedto.md)

- [getBlipColor](mta://scripting/shared/functions/getblipcolor.md)

- getBlipIcon

- [getBlipOrdering](mta://scripting/shared/functions/getblipordering.md)

- [getBlipSize](mta://scripting/shared/functions/getblipsize.md)

- [getBlipVisibleDistance](mta://scripting/shared/functions/getblipvisibledistance.md)

- [setBlipColor](mta://scripting/shared/functions/setblipcolor.md)

- [setBlipIcon](mta://scripting/shared/functions/setblipicon.md)

- [setBlipOrdering](mta://scripting/shared/functions/setblipordering.md)

- [setBlipSize](mta://scripting/shared/functions/setblipsize.md)

- [setBlipVisibleDistance](mta://scripting/shared/functions/setblipvisibledistance.md)

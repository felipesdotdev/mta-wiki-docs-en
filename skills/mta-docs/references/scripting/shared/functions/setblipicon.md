---
doc_id: "mta-wiki:1470"
title: "SetBlipIcon"
source_title: "SetBlipIcon"
source_url: "https://wiki.multitheftauto.com/wiki/SetBlipIcon"
revision_id: 63357
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# SetBlipIcon

This function sets the icon for an existing blip element.

## Syntax

```
bool setBlipIcon ( blip theBlip, int icon )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[blip](https://wiki.multitheftauto.com/index.php?search=blip):setIcon(...)*

**Variable**: *.icon*

**Counterpart**: *[getBlipIcon](mta://scripting/shared/functions/getblipicon.md)*

### Required Arguments

- **theBlip** The blip you wish to set the icon of.

- **icon:** A number indicating the icon you wish to change it do. Valid values are listed on the [Radar Blips](mta://reference/misc/radar-blips.md) page.

### Returns

Returns *true* if the icon was successfully set, *false* if the element passed was not a valid blip or the icon value was not a valid icon number.

## Example

This example resets all blip icons to the default blip icon, 0.

```
-- Retrieve a table containing all the blips that exist
blips = getElementsByType ( "blip" )
-- Loop through the list, storing the blip from the table in the variable blipValue
for blipKey, blipValue in blips do
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

- [getBlipIcon](mta://scripting/shared/functions/getblipicon.md)

- [getBlipOrdering](mta://scripting/shared/functions/getblipordering.md)

- [getBlipSize](mta://scripting/shared/functions/getblipsize.md)

- [getBlipVisibleDistance](mta://scripting/shared/functions/getblipvisibledistance.md)

- [setBlipColor](mta://scripting/shared/functions/setblipcolor.md)

- setBlipIcon

- [setBlipOrdering](mta://scripting/shared/functions/setblipordering.md)

- [setBlipSize](mta://scripting/shared/functions/setblipsize.md)

- [setBlipVisibleDistance](mta://scripting/shared/functions/setblipvisibledistance.md)

---
doc_id: "mta-wiki:1472"
title: "SetBlipSize"
source_title: "SetBlipSize"
source_url: "https://wiki.multitheftauto.com/wiki/SetBlipSize"
revision_id: 63546
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# SetBlipSize

This function sets the size of a blip's icon.

## Syntax

```
bool setBlipSize ( blip theBlip, int iconSize )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[blip](https://wiki.multitheftauto.com/index.php?search=blip):setSize(...)*

**Variable**: *.size*

**Counterpart**: *[getBlipSize](mta://scripting/shared/functions/getblipsize.md)*

### Required Arguments

- **theBlip:** The blip you wish to get the size of.

- **iconSize:** The size you wish the icon to be. 2 is the default value. 25 is the maximum value. Value gets clamped between 0 and 25.

### Returns

Returns an *true* if the blip's size was set successfully. Returns *false* if the [element](mta://reference/misc/element.md) passed was not a [blip](https://wiki.multitheftauto.com/index.php?search=blip) or if the icon size passed was invalid.

## Example

This example will reset the size of all blips to the default.

```
-- Retrieve a table containing all the blips that exist
blips = getElementsByType ( "blip" )
-- Loop through the list
for blipKey, blipValue in ipairs(blips) do
	-- Retrieve the blip's size into the variable 'blipSize'
	blipSize = getBlipSize ( blipValue )
	-- If the blip's size wasn't 2 (the default size) already
	if ( blipSize ~= 2 ) then
		-- Set the size to the default
		setBlipSize ( blipValue, 2 )
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

- [setBlipIcon](mta://scripting/shared/functions/setblipicon.md)

- [setBlipOrdering](mta://scripting/shared/functions/setblipordering.md)

- setBlipSize

- [setBlipVisibleDistance](mta://scripting/shared/functions/setblipvisibledistance.md)

---
doc_id: "mta-wiki:1471"
title: "GetBlipSize"
source_title: "GetBlipSize"
source_url: "https://wiki.multitheftauto.com/wiki/GetBlipSize"
revision_id: 63330
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetBlipSize

This function gets the size of a blip..

## Syntax

```
int getBlipSize ( blip theBlip )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[blip](https://wiki.multitheftauto.com/index.php?search=blip):getSize(...)*

**Variable**: *.size*

**Counterpart**: *[setBlipSize](mta://scripting/shared/functions/setblipsize.md)*

### Required Arguments

- **theBlip:** The blip you wish to get the size of.

### Returns

Returns an [int](mta://reference/misc/int.md) indicating the size of the blip. The default value is 2. The maximum value is 25.

## Example

This example will reset the size of all blips to the default.

```
-- Retrieve a table containing all the blips that exist
blips = getElementsByType ( "blip" )
-- Loop through the list, storing the blip from the table in the variable blipValue
for blipKey, blipValue in ipairs(blips) do
	-- Retrieve the blip's size into the variable 'blipSize'
	blipSize = getBlipSize ( blipValue )
	-- If the blip's size wasn't 2 (the default size) already
	if ( blipSize ~= 2 ) then
		-- Set the blip's size to the default
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

- getBlipSize

- [getBlipVisibleDistance](mta://scripting/shared/functions/getblipvisibledistance.md)

- [setBlipColor](mta://scripting/shared/functions/setblipcolor.md)

- [setBlipIcon](mta://scripting/shared/functions/setblipicon.md)

- [setBlipOrdering](mta://scripting/shared/functions/setblipordering.md)

- [setBlipSize](mta://scripting/shared/functions/setblipsize.md)

- [setBlipVisibleDistance](mta://scripting/shared/functions/setblipvisibledistance.md)

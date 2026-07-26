---
doc_id: "mta-wiki:5657"
title: "SetBlipVisibleDistance"
source_title: "SetBlipVisibleDistance"
source_url: "https://wiki.multitheftauto.com/wiki/SetBlipVisibleDistance"
revision_id: 63548
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:16:38.298412+00:00"
---

# SetBlipVisibleDistance

This function will set the visible distance of a blip.

## Syntax

```
bool setBlipVisibleDistance ( blip theBlip, float theDistance )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[blip](mta://reference/misc/blip.md):setVisibleDistance(...)*

**Variable**: *.visibleDistance*

**Counterpart**: *[getBlipVisibleDistance](mta://scripting/shared/functions/getblipvisibledistance.md)*

### Required Arguments

- **theBlip:** The blip whose visible distance you wish to get.

- **theDistance:** The distance you want the blip to be visible for. Value gets clamped between 0 and 65535.

### Returns

Returns true if successful, false otherwise.

## Example

This example will demonstrate basic functionality of setBlipVisibleDistance

```
local blip = createBlip(0, 0, 0, 47, 0, 0, 0, 0, 0, 0, 1000)
outputDebugString("Blip visible distance: "..getBlipVisibleDistance(blip)) --1000
setBlipVisibleDistance(blip, 2000)
outputDebugString("Blip visible distance: "..getBlipVisibleDistance(blip)) --2000
```

This example will set the visible distance of all blips to half the original value.

```
-- Retrieve a table containing all the blips that exist
local blips = getElementsByType("blip")
-- Loop through the list, storing the blips visible distance with the rest.
for index, blip in ipairs(blips) do
	-- Retrieve the blip's visible distance and divide by 2
	setBlipVisibleDistance(blip, getBlipVisibleDistance(blip) / 2)
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

- [setBlipSize](mta://scripting/shared/functions/setblipsize.md)

- setBlipVisibleDistance

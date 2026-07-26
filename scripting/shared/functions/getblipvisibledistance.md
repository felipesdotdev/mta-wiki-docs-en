---
doc_id: "mta-wiki:5656"
title: "GetBlipVisibleDistance"
source_title: "GetBlipVisibleDistance"
source_url: "https://wiki.multitheftauto.com/wiki/GetBlipVisibleDistance"
revision_id: 63353
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:07.555349+00:00"
---

# GetBlipVisibleDistance

This function will tell you what visible distance a blip has.

## Syntax

```
float getBlipVisibleDistance ( blip theBlip )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[blip](mta://reference/misc/blip.md):getVisibleDistance(...)*

**Variable**: *.visibleDistance*

**Counterpart**: *[setBlipVisibleDistance](mta://scripting/shared/functions/setblipvisibledistance.md)*

### Required Arguments

- **theBlip:** The blip whose visible distance you wish to get.

### Returns

Returns one float with the blips visible distance, false if the blip is invalid.

## Example

This example will demonstrate basic functionality of getBlipVisibleDistance

```
local blip = createBlip(0, 0, 0, 47, 0, 0, 0, 0, 0, 0, 1000)
outputDebugString("Blip visible distance: "..getBlipVisibleDistance(blip))
```

This example will combine the total visible distances of all blips

```
-- Retrieve a table containing all the blips that exist
local blips = getElementsByType("blip")
local distance = 0
-- Loop through the list, storing the blips visible distance with the rest.
for index, blip in ipairs(blips) do
	-- Retrieve the blip's visible distance
	distance = distance + getBlipVisibleDistance(blip) or 0 -- "or 0" just incase its false ;)
end
outputDebugString("Combined total of all blips visible distances: "..distance)
```

## See Also

- [createBlip](mta://scripting/shared/functions/createblip.md)

- [createBlipAttachedTo](mta://scripting/shared/functions/createblipattachedto.md)

- [getBlipColor](mta://scripting/shared/functions/getblipcolor.md)

- [getBlipIcon](mta://scripting/shared/functions/getblipicon.md)

- [getBlipOrdering](mta://scripting/shared/functions/getblipordering.md)

- [getBlipSize](mta://scripting/shared/functions/getblipsize.md)

- getBlipVisibleDistance

- [setBlipColor](mta://scripting/shared/functions/setblipcolor.md)

- [setBlipIcon](mta://scripting/shared/functions/setblipicon.md)

- [setBlipOrdering](mta://scripting/shared/functions/setblipordering.md)

- [setBlipSize](mta://scripting/shared/functions/setblipsize.md)

- [setBlipVisibleDistance](mta://scripting/shared/functions/setblipvisibledistance.md)

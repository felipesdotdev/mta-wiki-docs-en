---
doc_id: "mta-wiki:1570"
title: "GetRadarAreaSize"
source_title: "GetRadarAreaSize"
source_url: "https://wiki.multitheftauto.com/wiki/GetRadarAreaSize"
revision_id: 43071
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:22.579751+00:00"
---

# GetRadarAreaSize

This function is used for getting the X and Y size of an existing [radar area](mta://reference/misc/radararea.md).

## Syntax

```
float, float getRadarAreaSize ( radararea theRadararea )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[radararea](mta://reference/misc/radararea.md):getSize(...)*

### Required Arguments

- **theRadararea:** The [radar area](mta://reference/misc/radararea.md) element whose size you wish to get.

### Returns

Returns two *floats* indicating the X and Y length of the radar area respectively, *false* if the radar area is invalid.

## Example

The following example looks for radar areas whose size is smaller than 100 by 100:

```
local radarareas = getElementsByType ( "radararea" ) -- get a table of radararea elements
for k, theArea in ipairs(radarareas) do -- use a generic for loop to step through each of the elements
   local sizeX, sizeY = getRadarAreaSize ( theArea ) -- get the size of the radar area
   if ( sizeX < 100 and sizeY < 100 ) then -- check if it's smaller than 100 by 100
      outputChatBox ( "A small radar area was found!" )
   end
end
```

## See Also

- [createRadarArea](mta://scripting/shared/functions/createradararea.md)

- [getRadarAreaColor](mta://scripting/shared/functions/getradarareacolor.md)

- getRadarAreaSize

- [isInsideRadarArea](mta://scripting/shared/functions/isinsideradararea.md)

- [isRadarAreaFlashing](mta://scripting/shared/functions/isradarareaflashing.md)

- [setRadarAreaColor](mta://scripting/shared/functions/setradarareacolor.md)

- [setRadarAreaFlashing](mta://scripting/shared/functions/setradarareaflashing.md)

- [setRadarAreaSize](mta://scripting/shared/functions/setradarareasize.md)

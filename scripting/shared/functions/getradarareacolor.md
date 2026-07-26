---
doc_id: "mta-wiki:1571"
title: "GetRadarAreaColor"
source_title: "GetRadarAreaColor"
source_url: "https://wiki.multitheftauto.com/wiki/GetRadarAreaColor"
revision_id: 43070
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:22.567007+00:00"
---

# GetRadarAreaColor

This function can be used to retrieve the current color of a [radar area](mta://reference/misc/radararea.md).

## Syntax

```
int, int, int, int getRadarAreaColor ( radararea theRadararea )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[radararea](mta://reference/misc/radararea.md):getColor(...)*

### Required Arguments

- **theRadararea:** The [radar area](mta://reference/misc/radararea.md) you wish to retrieve the colour of.

### Returns

Returns four integers in RGBA format (*red*, *green*, *blue*, *alpha*), with a maximum value of 255 for each.  Alpha decides transparency where 255 is opaque and 0 is transparent.  Returns *false* if the radararea is invalid.

## Example

This example checks the color of a radararea defined as 'area' and announces if it is Ballas or Grove Street territory.

```
local r,g,b,a = getRadarAreaColor ( area )           -- get the color of 'area' and store it in 'r', 'g', 'b' and 'a'
if r == 0 and g == 255 and b == 0 then               -- if the radar area is fully green
    outputChatBox ( "This is Grove Street turf!" )   -- announce it as grove street area
elseif r == 255 and g == 0 and b == 255 then         -- if it is purple however
    outputChatBox ( "This is Ballas turf!" )         -- announce it as ballas area
end
```

## See Also

- [createRadarArea](mta://scripting/shared/functions/createradararea.md)

- getRadarAreaColor

- [getRadarAreaSize](mta://scripting/shared/functions/getradarareasize.md)

- [isInsideRadarArea](mta://scripting/shared/functions/isinsideradararea.md)

- [isRadarAreaFlashing](mta://scripting/shared/functions/isradarareaflashing.md)

- [setRadarAreaColor](mta://scripting/shared/functions/setradarareacolor.md)

- [setRadarAreaFlashing](mta://scripting/shared/functions/setradarareaflashing.md)

- [setRadarAreaSize](mta://scripting/shared/functions/setradarareasize.md)

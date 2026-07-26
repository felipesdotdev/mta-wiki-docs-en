---
doc_id: "mta-wiki:1616"
title: "SetRadarAreaColor"
source_title: "SetRadarAreaColor"
source_url: "https://wiki.multitheftauto.com/wiki/SetRadarAreaColor"
revision_id: 49900
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:16:44.214374+00:00"
---

# SetRadarAreaColor

Sets the color of an existing radar area.

## Syntax

```
bool setRadarAreaColor ( radararea theRadarArea, int r, int g, int b, int a )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[radararea](mta://reference/misc/radararea.md):setColor(...)*

### Required Arguments

- **theRadarArea:** the radararea element whose color you wish to set.

- **r:** an integer representing the amount of red in the color (0 for no red, 255 for solid red)

- **g:** an integer representing the amount of green in the color (0 for no green, 255 for solid green)

- **b:** an integer representing the amount of blue in the color (0 for no blue, 255 for solid blue)

- **a:** an integer representing the color's alpha (0 for transparent, 255 for opaque)

### Returns

Returns *true* if the color was set successfully, *false* if the radar area doesn't exist or the color arguments are improper.

## Example

This example creates a radar area and changes its color right away:

```
someArea = createRadarArea ( 1024, 1024, 75, 100, 0, 0, 0, 255 ) -- create a black radar area
local flag = setRadarAreaColor ( someArea, 255, 85, 85, 170 )    -- change its color
if ( flag ) then                                                 -- if the function returned true...
   outputChatBox ( "Color set successfully!" )
else                                                             -- if the function returned false...
   outputChatBox ( "Failed to set color." )
end
```

## See Also

- [createRadarArea](mta://scripting/shared/functions/createradararea.md)

- [getRadarAreaColor](mta://scripting/shared/functions/getradarareacolor.md)

- [getRadarAreaSize](mta://scripting/shared/functions/getradarareasize.md)

- [isInsideRadarArea](mta://scripting/shared/functions/isinsideradararea.md)

- [isRadarAreaFlashing](mta://scripting/shared/functions/isradarareaflashing.md)

- setRadarAreaColor

- [setRadarAreaFlashing](mta://scripting/shared/functions/setradarareaflashing.md)

- [setRadarAreaSize](mta://scripting/shared/functions/setradarareasize.md)

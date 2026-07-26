---
doc_id: "mta-wiki:14380"
title: "SetMarkerTargetArrowProperties"
source_title: "SetMarkerTargetArrowProperties"
source_url: "https://wiki.multitheftauto.com/wiki/SetMarkerTargetArrowProperties"
revision_id: 79899
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.6.0"]
---

# SetMarkerTargetArrowProperties

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

This function changes the color and size of the checkpoint marker's target arrow. 

## Syntax

```
bool setMarkerTargetArrowProperties(element marker [, int r = 255, int g = 64, int b = 64, int a = 255, float size = markerSize * 0.625 ] )
```

### Required Arguments

- **theMarker:** The [marker](https://wiki.multitheftauto.com/index.php?search=marker) that you wish to set the color of.

- **r:** The amount of red in the final color (0 to 255).

- **g:** The amount of green in the final color (0 to 255).

- **b:** The amount of blue in the final color (0 to 255).

- **a:** The amount of alpha in the final color (0 to 255).

- **size:** Target arrow size.

## Example

```
local newMarker = createMarker ( 0, 0, 2, "checkpoint", 2, 255, 0, 0, 255 )  -- Create a red checkpoint marker
setMarkerTarget(newMarker, 0, 10, 5) -- set target arrow direction

setMarkerTargetArrowProperties(newMarker, 0, 255, 255, 255) -- Set target arrow color to light blue (aqua)
```

## See Also

- [createMarker](mta://scripting/shared/functions/createmarker.md)

- [getMarkerColor](mta://scripting/shared/functions/getmarkercolor.md)

- [getMarkerCount](mta://scripting/shared/functions/getmarkercount.md)

- [getMarkerIcon](mta://scripting/shared/functions/getmarkericon.md)

- [getMarkerSize](mta://scripting/shared/functions/getmarkersize.md)

- [getMarkerTarget](mta://scripting/shared/functions/getmarkertarget.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- [getMarkerTargetArrowProperties](mta://scripting/shared/functions/getmarkertargetarrowproperties.md)

- [getMarkerType](mta://scripting/shared/functions/getmarkertype.md)

- [setMarkerColor](mta://scripting/shared/functions/setmarkercolor.md)

- [setMarkerIcon](mta://scripting/shared/functions/setmarkericon.md)

- [setMarkerSize](mta://scripting/shared/functions/setmarkersize.md)

- [setMarkerTarget](mta://scripting/shared/functions/setmarkertarget.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- setMarkerTargetArrowProperties

- [setMarkerType](mta://scripting/shared/functions/setmarkertype.md)

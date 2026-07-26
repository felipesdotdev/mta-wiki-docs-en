---
doc_id: "mta-wiki:1401"
title: "SetMarkerColor"
source_title: "SetMarkerColor"
source_url: "https://wiki.multitheftauto.com/wiki/SetMarkerColor"
revision_id: 78149
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# SetMarkerColor

This function sets the color of the specified marker by modifying the values for red, green, blue and alpha.

## Syntax

```
bool setMarkerColor ( marker theMarker, int r, int g, int b, int a )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Marker](https://wiki.multitheftauto.com/index.php?search=Marker):setColor(...)*

**Counterpart**: *[getMarkerColor](mta://scripting/shared/functions/getmarkercolor.md)*

### Required Arguments

- **theMarker:** The [marker](https://wiki.multitheftauto.com/index.php?search=marker) that you wish to set the color of.

- **r:** The amount of red in the final color (0 to 255).

- **g:** The amount of green in the final color (0 to 255).

- **b:** The amount of blue in the final color (0 to 255).

- **a:** The amount of alpha in the final color (0 to 255).

## Example

```
local newMarker = createMarker ( 0, 0, 2, "cylinder", 1, 255, 0, 0, 255 )  -- Create a red marker
setMarkerColor ( newMarker, 0, 255, 0, 255 )                      -- Turn the red marker into a green one
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

- setMarkerColor

- [setMarkerIcon](mta://scripting/shared/functions/setmarkericon.md)

- [setMarkerSize](mta://scripting/shared/functions/setmarkersize.md)

- [setMarkerTarget](mta://scripting/shared/functions/setmarkertarget.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- [setMarkerTargetArrowProperties](mta://scripting/shared/functions/setmarkertargetarrowproperties.md)

- [setMarkerType](mta://scripting/shared/functions/setmarkertype.md)

---
doc_id: "mta-wiki:14381"
title: "GetMarkerTargetArrowProperties"
source_title: "GetMarkerTargetArrowProperties"
source_url: "https://wiki.multitheftauto.com/wiki/GetMarkerTargetArrowProperties"
revision_id: 82222
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.6.0"]
---

# GetMarkerTargetArrowProperties

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

function returns the color, transparency and size for a checkpoint marker's target arrow. 

## Syntax

```
int, int, int, int, int getMarkerTargetArrowProperties( marker theMarker )
```

### Required Arguments

- **theMarker**: The [marker](https://wiki.multitheftauto.com/index.php?search=marker) that you wish to retrieve the color and size of.

### Returns

Returns five [ints](mta://reference/misc/int.md) corresponding to the amount of *red*, *green*, *blue*, *alpha* and *size* of the marker's target arrow, *false* if invalid arguments were passed.

## Example

```
addEventHandler("onClientResourceStart", resourceRoot, function()

    local myMarker = createMarker(0, 0, 3, "checkpoint", 2.0, 255, 0, 0, 150)

    setMarkerTarget(myMarker, 10, 0, 3)

    local r, g, b, a, size = getMarkerTargetArrowProperties(myMarker)

    if r then
        outputChatBox("Marker Target Arrow Properties:")
        outputChatBox("Color: R=" .. r .. " G=" .. g .. " B=" .. b)
        outputChatBox("Alpha: " .. a)
        outputChatBox("Size: " .. size)
    else
        outputChatBox("Error: Could not retrieve marker target arrow properties.")
    end
end)
```

## See Also

- [createMarker](mta://scripting/shared/functions/createmarker.md)

- [getMarkerColor](mta://scripting/shared/functions/getmarkercolor.md)

- [getMarkerCount](mta://scripting/shared/functions/getmarkercount.md)

- [getMarkerIcon](mta://scripting/shared/functions/getmarkericon.md)

- [getMarkerSize](mta://scripting/shared/functions/getmarkersize.md)

- [getMarkerTarget](mta://scripting/shared/functions/getmarkertarget.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- getMarkerTargetArrowProperties

- [getMarkerType](mta://scripting/shared/functions/getmarkertype.md)

- [setMarkerColor](mta://scripting/shared/functions/setmarkercolor.md)

- [setMarkerIcon](mta://scripting/shared/functions/setmarkericon.md)

- [setMarkerSize](mta://scripting/shared/functions/setmarkersize.md)

- [setMarkerTarget](mta://scripting/shared/functions/setmarkertarget.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- [setMarkerTargetArrowProperties](mta://scripting/shared/functions/setmarkertargetarrowproperties.md)

- [setMarkerType](mta://scripting/shared/functions/setmarkertype.md)

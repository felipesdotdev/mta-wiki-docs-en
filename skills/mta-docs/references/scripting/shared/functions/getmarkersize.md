---
doc_id: "mta-wiki:1396"
title: "GetMarkerSize"
source_title: "GetMarkerSize"
source_url: "https://wiki.multitheftauto.com/wiki/GetMarkerSize"
revision_id: 78148
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetMarkerSize

This function returns a [float](mta://reference/misc/float.md) containing the size of the specified marker.

## Syntax

```
float getMarkerSize ( marker myMarker )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Marker](https://wiki.multitheftauto.com/index.php?search=Marker):getSize(...)*

**Variable**: *.size*

**Counterpart**: *[setMarkerSize](mta://scripting/shared/functions/setmarkersize.md)*

### Required Arguments

- **myMarker**: The [marker](https://wiki.multitheftauto.com/index.php?search=marker) that you wish to retrieve the size of.

### Returns

Returns a [float](mta://reference/misc/float.md) containing the size of the specified marker.

## Example

This example creates a marker and outputs the size to everyone.

```
-- Create a maker
local newMarker = createMarker ( 0, 0, 2, "cylinder", 2, 255, 0, 0, 255 )
-- If the marker was created successfully then...
if isElement ( newMarker ) then
    -- Tell everyone about it
    outputChatBox ( "Current marker size: " .. getMarkerSize ( newMarker ) )
end
```

## See Also

- [createMarker](mta://scripting/shared/functions/createmarker.md)

- [getMarkerColor](mta://scripting/shared/functions/getmarkercolor.md)

- [getMarkerCount](mta://scripting/shared/functions/getmarkercount.md)

- [getMarkerIcon](mta://scripting/shared/functions/getmarkericon.md)

- getMarkerSize

- [getMarkerTarget](mta://scripting/shared/functions/getmarkertarget.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- [getMarkerTargetArrowProperties](mta://scripting/shared/functions/getmarkertargetarrowproperties.md)

- [getMarkerType](mta://scripting/shared/functions/getmarkertype.md)

- [setMarkerColor](mta://scripting/shared/functions/setmarkercolor.md)

- [setMarkerIcon](mta://scripting/shared/functions/setmarkericon.md)

- [setMarkerSize](mta://scripting/shared/functions/setmarkersize.md)

- [setMarkerTarget](mta://scripting/shared/functions/setmarkertarget.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- [setMarkerTargetArrowProperties](mta://scripting/shared/functions/setmarkertargetarrowproperties.md)

- [setMarkerType](mta://scripting/shared/functions/setmarkertype.md)

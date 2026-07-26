---
doc_id: "mta-wiki:2190"
title: "GetMarkerIcon"
source_title: "GetMarkerIcon"
source_url: "https://wiki.multitheftauto.com/wiki/GetMarkerIcon"
revision_id: 43264
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:15.421488+00:00"
---

# GetMarkerIcon

This function returns the icon name for a marker.

## Syntax

```
string getMarkerIcon ( marker theMarker )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Marker](mta://reference/misc/marker.md):getIcon(...)*

**Variable**: *.icon*

**Counterpart**: *[setMarkerIcon](mta://scripting/shared/functions/setmarkericon.md)*

### Required Arguments

- **theMarker**: A [marker](mta://reference/misc/marker.md) element referencing the specified marker.

### Returns

Returns *false* if the marker passed is invalid or a string containing one of the following:

- **"none"**: No icon

- **"arrow"**: Arrow icon

- **"finish"**: Finish (end-race) icon

## Example

```
newmarker = createMarker ( 1000, 1000,1000, "checkpoint", 255, 0, 0 )
icon = getMarkerIcon ( newmarker )
outputChatBox ( "The default marker icon is " .. icon )
```

## See Also

- [createMarker](mta://scripting/shared/functions/createmarker.md)

- [getMarkerColor](mta://scripting/shared/functions/getmarkercolor.md)

- [getMarkerCount](mta://scripting/shared/functions/getmarkercount.md)

- getMarkerIcon

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

- [setMarkerTargetArrowProperties](mta://scripting/shared/functions/setmarkertargetarrowproperties.md)

- [setMarkerType](mta://scripting/shared/functions/setmarkertype.md)

---
doc_id: "mta-wiki:1400"
title: "SetMarkerSize"
source_title: "SetMarkerSize"
source_url: "https://wiki.multitheftauto.com/wiki/SetMarkerSize"
revision_id: 82129
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:16:41.330522+00:00"
---

# SetMarkerSize

This function sets the size of the specified marker.

Setting negative value will "flip" the marker, do nothing or make it invisible:

- **cylinder** or **arrow**: upside down

- **ring**: inside out

- **checkpoint**: disappear

- **corona**: bigger

## Syntax

```
bool setMarkerSize ( marker theMarker, float size )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Marker](mta://reference/misc/marker.md):setSize(...)*

**Variable**: *.size*

**Counterpart**: *[getMarkerSize](mta://scripting/shared/functions/getmarkersize.md)*

### Required Arguments

- **theMarker:** The [marker](mta://reference/misc/marker.md) that you wish to set the size of.

- **size:** A float representing new size of the marker.

### Returns

Returns *true* if successful, *false* if failed.

## Examples

This example creates a cylinder marker at the position 0, 0, 2 and sets its size to *2.5*.

```
local newMarker = createMarker ( 0, 0, 2, "cylinder", 1 )
setMarkerSize ( newMarker, 2.5 )
```

This example creates a cylinder marker at the position 0, 0, 2 and plus its size by *1* by using 'getMarkerSize'.

```
local newMarker = createMarker ( 0, 0, 2, "cylinder", 1 )
setMarkerSize ( newMarker, getMarkerSize( newMarker ) + 1 )
```

## See Also

### Client

- [isCoronaReflectionEnabled](mta://scripting/client/functions/iscoronareflectionenabled.md)

- [setCoronaReflectionEnabled](mta://scripting/client/functions/setcoronareflectionenabled.md)
  

- **Shared**

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

- setMarkerSize

- [setMarkerTarget](mta://scripting/shared/functions/setmarkertarget.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- [setMarkerTargetArrowProperties](mta://scripting/shared/functions/setmarkertargetarrowproperties.md)

- [setMarkerType](mta://scripting/shared/functions/setmarkertype.md)

### Server

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

- setMarkerSize

- [setMarkerTarget](mta://scripting/shared/functions/setmarkertarget.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- [setMarkerTargetArrowProperties](mta://scripting/shared/functions/setmarkertargetarrowproperties.md)

- [setMarkerType](mta://scripting/shared/functions/setmarkertype.md)

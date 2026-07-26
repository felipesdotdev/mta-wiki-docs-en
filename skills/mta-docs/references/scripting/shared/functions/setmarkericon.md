---
doc_id: "mta-wiki:2191"
title: "SetMarkerIcon"
source_title: "SetMarkerIcon"
source_url: "https://wiki.multitheftauto.com/wiki/SetMarkerIcon"
revision_id: 79763
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# SetMarkerIcon

This function allows changing the icon of a checkpoint marker.

## Syntax

```
bool setMarkerIcon ( marker theMarker, string icon )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Marker](https://wiki.multitheftauto.com/index.php?search=Marker):setIcon(...)*

**Variable**: *.icon*

**Counterpart**: *[getMarkerIcon](mta://scripting/shared/functions/getmarkericon.md)*

### Required Arguments

- **theMarker:** The [marker](https://wiki.multitheftauto.com/index.php?search=marker) to change the visual style of

- **icon:** A string referring to the type of icon, acceptable values are:

- **"none"**: No icon

- **"arrow"**: Arrow icon. Only 5 arrows can be visible at the same time.

- **"finish"**: Finish icon (at end of race)

## Example

This example creates a finish marker as you'd expect for the end of a race.

```
local newMarker = createMarker ( 0, 0, 2, "checkpoint", 1, 255, 0, 0) 
setMarkerIcon ( newMarker, "finish" )
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

- setMarkerIcon

- [setMarkerSize](mta://scripting/shared/functions/setmarkersize.md)

- [setMarkerTarget](mta://scripting/shared/functions/setmarkertarget.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- [setMarkerTargetArrowProperties](mta://scripting/shared/functions/setmarkertargetarrowproperties.md)

- [setMarkerType](mta://scripting/shared/functions/setmarkertype.md)

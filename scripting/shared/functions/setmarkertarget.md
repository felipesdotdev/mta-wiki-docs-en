---
doc_id: "mta-wiki:1551"
title: "SetMarkerTarget"
source_title: "SetMarkerTarget"
source_url: "https://wiki.multitheftauto.com/wiki/SetMarkerTarget"
revision_id: 79762
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:16:41.355283+00:00"
---

# SetMarkerTarget

This function sets the 'target' for a marker. Only the *checkpoint* and *ring* marker types can have a target.

For *checkpoint* markers, the target is shown as an arrow aiming at the point specified. Only 5 arrows can be visible at the same time.

For *ring* markers, the target is shown by rotating the whole ring so that it faces the point specified.

This function is most useful for setting up markers for races, where each marker points to the next one's position.
(This is mostly used in races!)

## Syntax

```
bool setMarkerTarget ( marker theMarker, float x, float y, float z )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Marker](mta://reference/misc/marker.md):setTarget(...)*

**Variable**: *.target*

**Counterpart**: *[getMarkerTarget](mta://scripting/shared/functions/getmarkertarget.md)*

### Required Arguments

- **theMarker:** The marker to set the target of

- **x:** The x axis of the coordinate to target the marker at

- **y:** The y axis of the coordinate to target the marker at

- **z:** The z axis of the coordinate to target the marker at

### Returns

Returns *true* if target was set, *false* otherwise.

## Example

Creates a marker in the center of the map and points it north.

```
local newMarker = createMarker(0, 0, 5, "ring", 2, 255, 0, 0, 255) --Creates a marker
setMarkerTarget(newMarker, 3000, 0, 0) --Face the marker north
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

- setMarkerTarget

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- [setMarkerTargetArrowProperties](mta://scripting/shared/functions/setmarkertargetarrowproperties.md)

- [setMarkerType](mta://scripting/shared/functions/setmarkertype.md)

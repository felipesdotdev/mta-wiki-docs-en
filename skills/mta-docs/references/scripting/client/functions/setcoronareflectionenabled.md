---
doc_id: "mta-wiki:13800"
title: "SetCoronaReflectionEnabled"
source_title: "SetCoronaReflectionEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/SetCoronaReflectionEnabled"
revision_id: 75594
language: "en"
categories: ["Client_functions", "Functions_and_events_with_issues"]
---

# SetCoronaReflectionEnabled

This function sets visibility of corona reflection.

## Syntax

```
bool setCoronaReflectionEnabled ( marker theMarker, bool enabled )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Marker](https://wiki.multitheftauto.com/index.php?search=Marker):setCoronaReflectionEnabled(...)*

**Counterpart**: *[isCoronaReflectionEnabled](mta://scripting/client/functions/iscoronareflectionenabled.md)*

### Required Arguments

- **theMarker:** the corona marker that you wish set visibility of corona reflection

- **enabled:** whenever corona reflection should be visible

### Returns

Returns *true* if [marker type](mta://scripting/shared/functions/setmarkertype.md) is *corona*, *false* otherwise.

## Issues

| Issue ID | Description |
| --- | --- |
| #2755 | Corona reflections do not render on custom placed objects |
| #2750 | Corona reflections do not render on all roads |

## See Also

- [isCoronaReflectionEnabled](mta://scripting/client/functions/iscoronareflectionenabled.md)

- setCoronaReflectionEnabled
  

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

- [setMarkerSize](mta://scripting/shared/functions/setmarkersize.md)

- [setMarkerTarget](mta://scripting/shared/functions/setmarkertarget.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- [setMarkerTargetArrowProperties](mta://scripting/shared/functions/setmarkertargetarrowproperties.md)

- [setMarkerType](mta://scripting/shared/functions/setmarkertype.md)

- [setCoronaReflectionsEnabled](mta://scripting/client/functions/setcoronareflectionsenabled.md)

- [getCoronaReflectionsEnabled](mta://scripting/client/functions/getcoronareflectionsenabled.md)

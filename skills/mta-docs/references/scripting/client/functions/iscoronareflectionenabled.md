---
doc_id: "mta-wiki:13801"
title: "IsCoronaReflectionEnabled"
source_title: "IsCoronaReflectionEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/IsCoronaReflectionEnabled"
revision_id: 75595
language: "en"
categories: ["Client_functions"]
---

# IsCoronaReflectionEnabled

This function gets visibility of corona reflection.

## Syntax

```
bool isCoronaReflectionEnabled ( marker theMarker )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Marker](https://wiki.multitheftauto.com/index.php?search=Marker):isCoronaReflectionEnabled(...)*

**Counterpart**: *[setCoronaReflectionEnabled](mta://scripting/client/functions/setcoronareflectionenabled.md)*

### Required Arguments

- **theMarker:** marker

### Returns

- Returns *false* is [marker type](mta://scripting/shared/functions/setmarkertype.md) is not *corona*.

- Returns *true* if corona reflection is enabled, *false* otherwise.

## See Also

- isCoronaReflectionEnabled

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

- [setMarkerSize](mta://scripting/shared/functions/setmarkersize.md)

- [setMarkerTarget](mta://scripting/shared/functions/setmarkertarget.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- [setMarkerTargetArrowProperties](mta://scripting/shared/functions/setmarkertargetarrowproperties.md)

- [setMarkerType](mta://scripting/shared/functions/setmarkertype.md)

- [setCoronaReflectionsEnabled](mta://scripting/client/functions/setcoronareflectionsenabled.md)

- [getCoronaReflectionsEnabled](mta://scripting/client/functions/getcoronareflectionsenabled.md)

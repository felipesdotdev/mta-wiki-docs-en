---
doc_id: "mta-wiki:4953"
title: "IsElementWithinMarker"
source_title: "IsElementWithinMarker"
source_url: "https://wiki.multitheftauto.com/wiki/IsElementWithinMarker"
revision_id: 58409
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:55.861400+00:00"
---

# IsElementWithinMarker

This function is used to determine if an [element](mta://reference/misc/element.md) is within a [marker](mta://reference/misc/marker.md).

## Syntax

```
bool isElementWithinMarker ( element theElement, marker theMarker )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[element](mta://reference/misc/element.md):isWithinMarker(...)*

### Required Arguments

- **theElement:** The [element](mta://reference/misc/element.md) you're checking.

- **theMarker:** The [marker](mta://reference/misc/marker.md) you're checking.

### Returns

Returns *true* if the element is within the marker, *false* otherwise

## Example

```
local dutymarker = createMarker(126.56, 254.98, 78.9, "cylinder", 2.0, 255, 0, 0, 150)

function duty(thePlayer)
    if isElementWithinMarker(thePlayer, dutymarker) then
        giveWeapon(thePlayer, 22, 100, 1)  
    else
        outputChatBox("You are not at the right place!", thePlayer, 255, 0, 0)
    end
end
addCommandHandler("duty", duty)
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

- [setMarkerTargetArrowProperties](mta://scripting/shared/functions/setmarkertargetarrowproperties.md)

- [setMarkerType](mta://scripting/shared/functions/setmarkertype.md)

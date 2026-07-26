---
doc_id: "mta-wiki:3958"
title: "GetMarkerCount"
source_title: "GetMarkerCount"
source_url: "https://wiki.multitheftauto.com/wiki/GetMarkerCount"
revision_id: 78157
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetMarkerCount

Returns the number of markers that currently exist in the world.

## Syntax

```
int getMarkerCount ( )
```

### Required Arguments

*None*

### Returns

Returns the number of markers that currently exist.

## Example

This example outputs the amount of markers to the player.

```
function howManyMarkers(thePlayer,command)
	local ammount = getMarkerCount()
	outputChatBox("There are "..ammount.." markers.",thePlayer,255,255,0)
end
addCommandHandler("markers",howManyMarkers)
```

## See Also

- [createMarker](mta://scripting/shared/functions/createmarker.md)

- [getMarkerColor](mta://scripting/shared/functions/getmarkercolor.md)

- getMarkerCount

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

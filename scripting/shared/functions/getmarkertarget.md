---
doc_id: "mta-wiki:1550"
title: "GetMarkerTarget"
source_title: "GetMarkerTarget"
source_url: "https://wiki.multitheftauto.com/wiki/GetMarkerTarget"
revision_id: 67677
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:15.454000+00:00"
---

# GetMarkerTarget

This function returns the position of the specified marker's target, the position it points to. This only works for checkpoint markers and ring markers. For checkpoints it returns the position the arrow is pointing to, for ring markers it returns the position the ring is facing. You can set this target with [setMarkerTarget](mta://scripting/shared/functions/setmarkertarget.md).

## Syntax

```
float float float getMarkerTarget ( marker theMarker )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Marker](mta://reference/misc/marker.md):getTarget(...)*

**Variable**: *.target*

**Counterpart**: *[setMarkerTarget](mta://scripting/shared/functions/setmarkertarget.md)*

### Required Arguments

- **theMarker:** The marker you wish to retrieve the target position of.

### Returns

Returns three *float*s if a target is set, or *false* in the first variable and *nil* in the two others if the marker is invalid or no target is set.

## Example

This example outputs the markers target (if available) when a player hits a marker.

Click to collapse [-]
Server

```
function nextCheck(thePlayer)
	local x,y,z = getMarkerTarget(source)    -- get the marker target
	if x ~= false then                       -- if a target is set for the marker, then...
		outputChatBox("Next checkpoint at: " .. x .. " " .. y .. " " .. z, thePlayer) -- output a message with the coordinates
	end
end
addEventHandler("onMarkerHit", root, nextCheck) -- add an event handler for the 'onMarkerHit' event
```

## See Also

- [createMarker](mta://scripting/shared/functions/createmarker.md)

- [getMarkerColor](mta://scripting/shared/functions/getmarkercolor.md)

- [getMarkerCount](mta://scripting/shared/functions/getmarkercount.md)

- [getMarkerIcon](mta://scripting/shared/functions/getmarkericon.md)

- [getMarkerSize](mta://scripting/shared/functions/getmarkersize.md)

- getMarkerTarget

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

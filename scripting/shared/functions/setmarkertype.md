---
doc_id: "mta-wiki:1398"
title: "SetMarkerType"
source_title: "SetMarkerType"
source_url: "https://wiki.multitheftauto.com/wiki/SetMarkerType"
revision_id: 44466
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:16:41.388567+00:00"
---

# SetMarkerType

This function changes a marker's type. The type controls how the marker is displayed in the game. It's important that you use marker types that users are used to from the single player game. For example, checkpoints are used in races, rings are used for aircraft races, arrows are used for entering buildings etc.

## Syntax

```
bool setMarkerType ( marker theMarker, string markerType )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Marker](mta://reference/misc/marker.md):setMarkerType(...)*

**Variable**: *.markerType*

**Counterpart**: *[getMarkerType](mta://scripting/shared/functions/getmarkertype.md)*

### Required Arguments

- **theMarker**: A [marker](mta://reference/misc/marker.md) element referencing the specified marker.

- **markerType**: A string denoting the marker type. Valid values are:

- **"checkpoint"**: A race checkpoint. These are very tall, but not infinite, light pillars. Checkpoints snap to ground and become invisible after going over a certain Z height.

- **"ring"**: Doughnut shaped ring, normally used for aircraft.

- **"cylinder"**: Small glowing ground ring. These are the glow markers you walk into to activate missions or events in single player.

- **"arrow"**: Arrow pointing down. These are the arrows on the doors you can enter in single player, except MTA's are not animated by default.

- **"corona"**: A glowing ball of light.

## Returns

Returns *true* if the marker type was changed, *false* if it wasn't or marker values were invalid.

## Example

This function changes all existing markers' type to the specified one.

```
function changeAllMarkersType ( newMarkerType )
	-- we store a table with all markers
	local allMarkers = getElementsByType( "marker" )
	-- for each marker in it,
	for index, aMarker in ipairs(allMarkers) do
		-- set its type to the one passed to this function
		setMarkerType( aMarker, newMarkerType )
	end
end
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

- setMarkerType

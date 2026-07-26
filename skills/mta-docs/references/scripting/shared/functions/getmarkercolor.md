---
doc_id: "mta-wiki:1397"
title: "GetMarkerColor"
source_title: "GetMarkerColor"
source_url: "https://wiki.multitheftauto.com/wiki/GetMarkerColor"
revision_id: 79902
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetMarkerColor

This function returns the color and transparency for a marker element.

## Syntax

```
int, int, int, int getMarkerColor ( marker theMarker )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Marker](https://wiki.multitheftauto.com/index.php?search=Marker):getColor(...)*

**Counterpart**: *[setMarkerColor](mta://scripting/shared/functions/setmarkercolor.md)*

### Required Arguments

- **theMarker**: The [marker](https://wiki.multitheftauto.com/index.php?search=marker) that you wish to retrieve the color of.

### Returns

Returns four [ints](mta://reference/misc/int.md) corresponding to the amount of *red*, *green*, *blue* and *alpha* (respectively) of the marker, *false* if invalid arguments were passed.

## Example

Click to collapse [-]
Serverside example

This example script fully heals players who hit a white marker, and kills players who hit a red one.

```
-- we define the function that will determine if the player is to be healed or killed
function healOrKill ( hitMarker, matchingDimension )
	-- if the marker was in a different dimension, stop here to ignore the event
	if not matchingDimension then
		return
	end
	-- get the marker's color
	local R, G, B, A = getMarkerColor( hitMarker )
	-- if its RGB color is 255,255,255 (white),
	if R == 255 and G == 255 and B == 255 then
		-- heal the player
		setElementHealth( source, 100 )
	-- if it isn't white, but 255,0,0 (red),
	elseif R == 255 and G == 0 and B == 0 then
		-- kill the player
		killPed( source )
	end
end
-- add our function as a handler to "onPlayerMarkerHit"
addEventHandler( "onPlayerMarkerHit", root, healOrKill )
```

## See Also

- [createMarker](mta://scripting/shared/functions/createmarker.md)

- getMarkerColor

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

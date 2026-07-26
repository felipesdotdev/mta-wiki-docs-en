---
doc_id: "mta-wiki:1394"
title: "GetMarkerType"
source_title: "GetMarkerType"
source_url: "https://wiki.multitheftauto.com/wiki/GetMarkerType"
revision_id: 78158
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:15.490988+00:00"
---

# GetMarkerType

This function returns a marker's type.

## Syntax

```
string getMarkerType ( marker theMarker )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Marker](mta://reference/misc/marker.md):getMarkerType(...)*

**Variable**: *.markerType*

**Counterpart**: *[setMarkerType](mta://scripting/shared/functions/setmarkertype.md)*

### Required Arguments

- **theMarker**: A [marker](mta://reference/misc/marker.md) element referencing the specified marker.

### Returns

- Returns one of the following strings:

- **"checkpoint"**: A race checkpoint. These are very tall, but not infinite, light pillars. Checkpoints snap to ground and become invisible after going over a certain Z height.

- **"ring"**: Doughnut shaped ring, normally used for aircraft.

- **"cylinder"**: Small glowing ground ring. These are the glow markers you walk into to activate missions or events in single player.

- **"arrow"**: Arrow pointing down. These are the arrows on the doors you can enter in single player, except MTA's are not animated by default.

- **"corona"**: A glowing ball of light.

If an invalid marker is specified, *false* is returned.

## Example

This function creates a default marker at a given position and outputs its type.

```
function createMarkerAndOutputType ( ... )
    -- we create the marker.
    local theMarker = createMarker ( ... )
    -- if the marker was created.
    if isElement ( theMarker ) then
        -- then get its type.
        local markerType = getMarkerType ( theMarker )
        -- and output it.
        return outputChatBox ( "It's a " .. markerType .. " marker!" )
    end
end

-- Create a marker and show its type in chat.
createMarkerAndOutputType(0, 0, 2, "cylinder", 2)
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

- getMarkerType

- [setMarkerColor](mta://scripting/shared/functions/setmarkercolor.md)

- [setMarkerIcon](mta://scripting/shared/functions/setmarkericon.md)

- [setMarkerSize](mta://scripting/shared/functions/setmarkersize.md)

- [setMarkerTarget](mta://scripting/shared/functions/setmarkertarget.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- [setMarkerTargetArrowProperties](mta://scripting/shared/functions/setmarkertargetarrowproperties.md)

- [setMarkerType](mta://scripting/shared/functions/setmarkertype.md)

---
doc_id: "mta-wiki:4118"
title: "OnClientMarkerLeave"
source_title: "OnClientMarkerLeave"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientMarkerLeave"
revision_id: 74755
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:19.007158+00:00"
---

# OnClientMarkerLeave

This event is triggered when a player leaves the area of a marker created using [createMarker](mta://scripting/shared/functions/createmarker.md).

## Parameters

```
player leftPlayer, bool matchingDimension
```

- **leftPlayer**: the [player](mta://reference/misc/player.md) that left the [marker's](mta://reference/misc/marker.md) area.

- **matchingDimension**: *true* if the [player](mta://reference/misc/player.md) is in the same [dimension](mta://reference/misc/dimension.md) as the [marker](mta://reference/misc/marker.md).

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [marker](mta://reference/misc/marker.md) that the player left.

## Example

This example shows a message in the chatbox whenever a player leaves any marker.

```
function markerLeave ( leavingPlayer, matchingDimension )
    outputChatBox ( getPlayerName(leavingPlayer) .. " left a marker" )
end

addEventHandler ( "onClientMarkerLeave", getRootElement(), markerLeave )
```

## See Also

### Client marker events

- [onClientMarkerHit](mta://scripting/client/events/onclientmarkerhit.md)

- onClientMarkerLeave

### Client marker functions

- [isCoronaReflectionEnabled](mta://scripting/client/functions/iscoronareflectionenabled.md)

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

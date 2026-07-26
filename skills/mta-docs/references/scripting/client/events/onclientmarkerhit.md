---
doc_id: "mta-wiki:4117"
title: "OnClientMarkerHit"
source_title: "OnClientMarkerHit"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientMarkerHit"
revision_id: 77647
language: "en"
categories: ["Client_events"]
---

# OnClientMarkerHit

This event is triggered when a player enters a marker created using [createMarker](mta://scripting/shared/functions/createmarker.md).

| [[{{{image}}}\|link=\|]] | Important Note: The event is not triggered when only the dimension changes of the player. So, if you use the `matchingDimension` when teleporting players into existing markers you should always first set their dimension/interior and only then the position |
| --- | --- |
|  |  |

## Parameters

```
player hitPlayer, bool matchingDimension
```

- **hitPlayer:** the [player](https://wiki.multitheftauto.com/index.php?search=player) that hit the [marker](https://wiki.multitheftauto.com/index.php?search=marker).

- **matchingDimension:** *true* if the [player](https://wiki.multitheftauto.com/index.php?search=player) is in the same [dimension](mta://reference/misc/dimension.md) as the hit [marker](https://wiki.multitheftauto.com/index.php?search=marker).

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [marker](https://wiki.multitheftauto.com/index.php?search=marker) that got hit by the player.

## Example

This code will output a message to the chatbox whenever any player walks into any marker.

```
function MarkerHit ( hitPlayer, matchingDimension )
	outputChatBox ( getPlayerName(hitPlayer) .. " entered a marker" )
end
addEventHandler ( "onClientMarkerHit", getRootElement(), MarkerHit )
```

## See Also

### Client marker events

- onClientMarkerHit

- [onClientMarkerLeave](mta://scripting/client/events/onclientmarkerleave.md)

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

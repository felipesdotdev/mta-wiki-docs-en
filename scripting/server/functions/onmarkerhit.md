---
doc_id: "mta-wiki:1819"
title: "OnMarkerHit"
source_title: "OnMarkerHit"
source_url: "https://wiki.multitheftauto.com/wiki/OnMarkerHit"
revision_id: 82853
language: "en"
categories: ["Server_Events", "Functions_and_events_with_issues"]
generated_at: "2026-07-26T16:16:24.208025+00:00"
---

# OnMarkerHit

This event is triggered when an element enters a marker created using [createMarker](mta://scripting/shared/functions/createmarker.md).

| [[{{{image}}}\|link=\|]] | Important Note: The event is not triggered when only the dimension changes of the player. So, if you use the `matchingDimension` when teleporting players into existing markers you should always first set their dimension/interior and only then the position |
| --- | --- |
|  |  |

## Parameters

```
element hitElement, bool matchingDimension
```

- **hitElement**: the [element](mta://reference/misc/element.md) that hit the [marker](mta://reference/misc/marker.md).

- **matchingDimension**: a [boolean](mta://reference/misc/boolean.md) representing whether the [element](mta://reference/misc/element.md) is in the same dimension as the [marker](mta://reference/misc/marker.md).

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [marker](mta://reference/misc/marker.md) that got hit by the element.

## Example

This example will output a message what type of element has entered a marker.

```
local playerMarker = createMarker(0, 0, 2, "cylinder", 5, 10, 244, 23, 200, root)

function handlePlayerMarker(hitElement)
	local elementType = getElementType(hitElement)

	outputChatBox("Element ("..elementType..") has entered marker.")
end
addEventHandler("onMarkerHit", playerMarker, handlePlayerMarker)
```

## Issues

| Issue ID | Description |
| --- | --- |
| #519 | onMarkerHit not always triggered in interiors |

## See Also

### Marker events

- onMarkerHit

- [onMarkerLeave](mta://scripting/server/events/onmarkerleave.md)

### Event functions

- [addEvent](mta://scripting/shared/functions/addevent.md)

- [addEventHandler](mta://scripting/shared/functions/addeventhandler.md)

- [cancelEvent](mta://scripting/shared/functions/cancelevent.md)

- [cancelLatentEvent](mta://scripting/shared/functions/cancellatentevent.md)

- [getEventHandlers](mta://scripting/shared/functions/geteventhandlers.md)

- [getLatentEventHandles](mta://scripting/shared/functions/getlatenteventhandles.md)

- [getLatentEventStatus](mta://scripting/shared/functions/getlatenteventstatus.md)

- [removeEventHandler](mta://scripting/shared/functions/removeeventhandler.md)

- [triggerEvent](mta://scripting/shared/functions/triggerevent.md)

- [wasEventCancelled](mta://scripting/shared/functions/waseventcancelled.md)

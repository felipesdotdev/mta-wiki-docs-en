---
doc_id: "mta-wiki:3308"
title: "OnMarkerLeave"
source_title: "OnMarkerLeave"
source_url: "https://wiki.multitheftauto.com/wiki/OnMarkerLeave"
revision_id: 69431
language: "en"
categories: ["Server_Events"]
---

# OnMarkerLeave

This event is triggered when an element leaves the area of a marker created using [createMarker](mta://scripting/shared/functions/createmarker.md).

## Parameters

```
element leftElement, bool matchingDimension
```

- **leftElement**: the [element](mta://reference/misc/element.md) that left the [marker's](https://wiki.multitheftauto.com/index.php?search=marker%27s) area.

- **matchingDimension**: a [boolean](mta://reference/misc/boolean.md) representing whether the [element](mta://reference/misc/element.md) is in the same dimension as the [marker](https://wiki.multitheftauto.com/index.php?search=marker).

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [marker](https://wiki.multitheftauto.com/index.php?search=marker) that the element left.

## Example

This example shows a message in the chat box when element (in this case a player) leaves a marker.

```
local myMarker = createMarker(-2596.6259765625, 579.3583984375, 15.626741409302, "cylinder", 2.0, 255, 0, 0, 150)

function markerLeave(leaveElement, matchingDimension)
	local elementType = getElementType(leaveElement)

	if elementType == "player" then
		outputChatBox("Player has left a marker.", root, 255, 255, 0)
	end
end
addEventHandler("onMarkerLeave", myMarker, markerLeave)
```

## See Also

### Marker events

- [onMarkerHit](mta://scripting/server/functions/onmarkerhit.md)

- onMarkerLeave

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

---
doc_id: "mta-wiki:5277"
title: "OnElementStopSync"
source_title: "OnElementStopSync"
source_url: "https://wiki.multitheftauto.com/wiki/OnElementStopSync"
revision_id: 75958
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:24.133472+00:00"
---

# OnElementStopSync

This event is triggered when an element is no longer synced by a player.

## Parameters

```
player oldSyncer
```

- **oldSyncer**: a [player](mta://reference/misc/player.md) element representing the last player who was syncing the [element](mta://reference/misc/element.md).

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [element](mta://reference/misc/element.md) which is no longer synced by a player.

## Example

This script creates a vehicle in the center of the map and outputs a message to its old syncer if he is not syncing the vehicle anymore.

```
function onResourceStart()
	local vehicleElement = createVehicle(434, 0, 0, 3) -- Create vehicle

	addEventHandler("onElementStopSync", vehicleElement, onElementStopSync) -- Bind handler specifically to it
end
addEventHandler("onResourceStart", resourceRoot, onResourceStart)

function onElementStopSync(oldSyncer)
	outputChatBox("The vehicle is not being synced by you anymore.", oldSyncer) -- Tell player (oldSyncer) that he's not syncing vehicle
end
```

## See Also

### Element events

- [onElementClicked](mta://scripting/server/events/onelementclicked.md)

- [onElementColShapeHit](mta://scripting/server/events/onelementcolshapehit.md)

- [onElementColShapeLeave](mta://scripting/server/events/onelementcolshapeleave.md)

- [onElementDataChange](mta://scripting/server/events/onelementdatachange.md)

- [onElementDestroy](mta://scripting/server/events/onelementdestroy.md)

- [onElementDimensionChange](mta://scripting/server/events/onelementdimensionchange.md)

- [onElementInteriorChange](mta://scripting/server/events/onelementinteriorchange.md)

- [onElementModelChange](mta://scripting/server/events/onelementmodelchange.md)

- [onElementStartSync](mta://scripting/server/events/onelementstartsync.md)

- onElementStopSync

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

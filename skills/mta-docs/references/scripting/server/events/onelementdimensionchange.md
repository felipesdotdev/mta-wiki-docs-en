---
doc_id: "mta-wiki:12641"
title: "OnElementDimensionChange"
source_title: "OnElementDimensionChange"
source_url: "https://wiki.multitheftauto.com/wiki/OnElementDimensionChange"
revision_id: 81279
language: "en"
categories: ["Server_Events"]
---

# OnElementDimensionChange

This event is triggered when the dimension of an [element](mta://reference/misc/element.md) is changed using [setElementDimension](mta://scripting/shared/functions/setelementdimension.md).

## Parameters

```
int oldDimension, int newDimension
```

- **oldDimension**: An [int](mta://reference/misc/int.md) representing the dimension the [element](mta://reference/misc/element.md) was in before.

- **newDimension**: An [int](mta://reference/misc/int.md) representing the dimension the [element](mta://reference/misc/element.md) is in now.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [element](mta://reference/misc/element.md) that changed its dimension.

## Example

This example prints the old and the new dimension of a vehicle

```
local vehicle = createVehicle (411, 0, 0, 3) -- create a vehicle
setTimer (setElementDimension, 1000, 1, vehicle, 10) -- set a new dimension to the vehicle after 1 second

-- add an event handler to onElementDimensionChange attached to the vehicle
addEventHandler ("onElementDimensionChange", vehicle,
	function (oldDimension, newDimension)
		 -- print the old and the new vehicle's dimension
		outputChatBox (inspect (source) .. "'s dimension changed from " .. oldDimension .. " to " .. newDimension)
	end
)
```

## See Also

### Element events

- [onElementClicked](mta://scripting/server/events/onelementclicked.md)

- [onElementColShapeHit](mta://scripting/server/events/onelementcolshapehit.md)

- [onElementColShapeLeave](mta://scripting/server/events/onelementcolshapeleave.md)

- [onElementDataChange](mta://scripting/server/events/onelementdatachange.md)

- [onElementDestroy](mta://scripting/server/events/onelementdestroy.md)

- onElementDimensionChange

- [onElementInteriorChange](mta://scripting/server/events/onelementinteriorchange.md)

- [onElementModelChange](mta://scripting/server/events/onelementmodelchange.md)

- [onElementStartSync](mta://scripting/server/events/onelementstartsync.md)

- [onElementStopSync](mta://scripting/server/events/onelementstopsync.md)

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

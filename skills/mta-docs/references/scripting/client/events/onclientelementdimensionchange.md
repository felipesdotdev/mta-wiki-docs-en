---
doc_id: "mta-wiki:12640"
title: "OnClientElementDimensionChange"
source_title: "OnClientElementDimensionChange"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientElementDimensionChange"
revision_id: 81278
language: "en"
categories: ["Client_events"]
---

# OnClientElementDimensionChange

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

```
local vehicle = createVehicle (411, 0, 0, 3)
setTimer (setElementDimension, 1000, 1, vehicle, 10)

addEventHandler ("onClientElementDimensionChange", vehicle,
	function (oldDimension, newDimension)
		outputChatBox (inspect (source) .. "'s dimension changed from " .. oldDimension .. " to " .. newDimension)
	end
)
```

## See Also

### Client element events

- [onClientElementColShapeHit](mta://scripting/client/events/onclientelementcolshapehit.md)

- [onClientElementColShapeLeave](mta://scripting/client/events/onclientelementcolshapeleave.md)

- [onClientElementDataChange](mta://scripting/client/events/onclientelementdatachange.md)

- [onClientElementDestroy](mta://scripting/client/events/onclientelementdestroy.md)

- onClientElementDimensionChange

- [onClientElementInteriorChange](mta://scripting/client/events/onclientelementinteriorchange.md)

- [onClientElementModelChange](mta://scripting/client/events/onclientelementmodelchange.md)

- [onClientElementStreamIn](mta://scripting/client/events/onclientelementstreamin.md)

- [onClientElementStreamOut](mta://scripting/client/events/onclientelementstreamout.md)

### Client event functions

- [triggerLatentServerEvent](mta://scripting/client/functions/triggerlatentserverevent.md)

- [triggerServerEvent](mta://scripting/client/functions/triggerserverevent.md)
  

- **Shared**

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

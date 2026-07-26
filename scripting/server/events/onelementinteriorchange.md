---
doc_id: "mta-wiki:12858"
title: "OnElementInteriorChange"
source_title: "OnElementInteriorChange"
source_url: "https://wiki.multitheftauto.com/wiki/OnElementInteriorChange"
revision_id: 81300
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:24.072614+00:00"
---

# OnElementInteriorChange

This event is triggered when the interior of an [element](mta://reference/misc/element.md) is changed using [setElementInterior](mta://scripting/shared/functions/setelementinterior.md).

## Parameters

```
int oldInterior, int newInterior
```

- **oldInterior**: an [int](mta://reference/misc/int.md) representing the interior the [element](mta://reference/misc/element.md) was in before.

- **newInterior**: an [int](mta://reference/misc/int.md) representing the interior the [element](mta://reference/misc/element.md) is in now.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [element](mta://reference/misc/element.md) that changed its interior.

## Example

```
local vehicle = createVehicle(411, 0, 0, 3)
setTimer(setElementInterior, 1000, 1, vehicle, 10)

addEventHandler("onElementInteriorChange", vehicle, function(oldInterior, newInterior)
    outputChatBox(inspect(source).."'s interior changed from "..oldInterior.." to "..newInterior)
end)
```

## See Also

### Element events

- [onElementClicked](mta://scripting/server/events/onelementclicked.md)

- [onElementColShapeHit](mta://scripting/server/events/onelementcolshapehit.md)

- [onElementColShapeLeave](mta://scripting/server/events/onelementcolshapeleave.md)

- [onElementDataChange](mta://scripting/server/events/onelementdatachange.md)

- [onElementDestroy](mta://scripting/server/events/onelementdestroy.md)

- [onElementDimensionChange](mta://scripting/server/events/onelementdimensionchange.md)

- onElementInteriorChange

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

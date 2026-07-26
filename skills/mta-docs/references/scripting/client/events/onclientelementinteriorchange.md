---
doc_id: "mta-wiki:12857"
title: "OnClientElementInteriorChange"
source_title: "OnClientElementInteriorChange"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientElementInteriorChange"
revision_id: 81299
language: "en"
categories: ["Client_events"]
---

# OnClientElementInteriorChange

This event is triggered when the interior of an [element](mta://reference/misc/element.md) is changed using [setElementInterior](mta://scripting/shared/functions/setelementinterior.md).

## Parameters

```
int oldInterior, int newInterior
```

- **oldInterior**: An [int](mta://reference/misc/int.md) representing the interior the [element](mta://reference/misc/element.md) was in before.

- **newInterior**: An [int](mta://reference/misc/int.md) representing the interior the [element](mta://reference/misc/element.md) is in now.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [element](mta://reference/misc/element.md) that changed its interior.

## Example

```
local vehicle = createVehicle (411, 0, 0, 3)
setTimer (setElementInterior, 1000, 1, vehicle, 10)

addEventHandler ("onClientElementInteriorChange", vehicle, function (oldInterior, newInterior)
    outputChatBox (inspect (source).."'s interior changed from "..oldInterior.." to "..newInterior)
end)
```

## See Also

### Client element events

- [onClientElementColShapeHit](mta://scripting/client/events/onclientelementcolshapehit.md)

- [onClientElementColShapeLeave](mta://scripting/client/events/onclientelementcolshapeleave.md)

- [onClientElementDataChange](mta://scripting/client/events/onclientelementdatachange.md)

- [onClientElementDestroy](mta://scripting/client/events/onclientelementdestroy.md)

- [onClientElementDimensionChange](mta://scripting/client/events/onclientelementdimensionchange.md)

- onClientElementInteriorChange

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

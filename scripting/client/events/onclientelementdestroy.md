---
doc_id: "mta-wiki:4227"
title: "OnClientElementDestroy"
source_title: "OnClientElementDestroy"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientElementDestroy"
revision_id: 79547
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:18.352561+00:00"
---

# OnClientElementDestroy

This event is triggered when an element gets destroyed by [destroyElement](mta://scripting/shared/functions/destroyelement.md) or when the creator resource is stopping. It is also triggered when a children element of this element is destroyed. It is not triggered on a player when they quit.

## Parameters

No parameters.

## Source

The source of this event is the element that is being destroyed.

## Example

This example prints a message in the chat box when the vehicle that you are in gets destroyed.

```
addEventHandler("onClientElementDestroy", root, function()
	if getElementType(source) == "vehicle" and getPedOccupiedVehicle(localPlayer) == source then
		outputChatBox("The vehicle that you were in has been destroyed by the script")
	end
end)
```

## See Also

### Client element events

- [onClientElementColShapeHit](mta://scripting/client/events/onclientelementcolshapehit.md)

- [onClientElementColShapeLeave](mta://scripting/client/events/onclientelementcolshapeleave.md)

- [onClientElementDataChange](mta://scripting/client/events/onclientelementdatachange.md)

- onClientElementDestroy

- [onClientElementDimensionChange](mta://scripting/client/events/onclientelementdimensionchange.md)

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

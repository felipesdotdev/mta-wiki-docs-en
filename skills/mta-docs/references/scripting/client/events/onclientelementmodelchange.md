---
doc_id: "mta-wiki:11373"
title: "OnClientElementModelChange"
source_title: "OnClientElementModelChange"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientElementModelChange"
revision_id: 71398
language: "en"
categories: ["Client_events", "Changes_in_1.5.6"]
---

# OnClientElementModelChange

This event is triggered when the model of an [element](mta://reference/misc/element.md) is changed using [setElementModel](mta://scripting/shared/functions/setelementmodel.md).

## Parameters

```
int oldModel, int newModel
```

- **oldModel:** an [int](mta://reference/misc/int.md) representing the model of the [element](mta://reference/misc/element.md) before the change occurred.

- **newModel:** an [int](mta://reference/misc/int.md) representing the new model of the [element](mta://reference/misc/element.md).

## Source

The source of this event is the element that changed its model.

## Cancel effect

This event doesn't support [cancellation](mta://reference/misc/event-system.md). Use [setElementModel](mta://scripting/shared/functions/setelementmodel.md) with the old value to reverse.

## Example

This example sends a message to players when their model changes telling them what the model ID is and was.

```
function informPlayerOnModelChange(oldModel, newModel)
    if ( getElementType(source) == "player" ) then -- Make sure the element is a player
        outputChatBox("Model ID changing from: "..oldModel.." to: ".. newModel, 0, 255, 0) -- Message for player
    end
end
addEventHandler("onClientElementModelChange", root, informPlayerOnModelChange) -- Bind the event to every element
```

## See Also

### Client element events

- [onClientElementColShapeHit](mta://scripting/client/events/onclientelementcolshapehit.md)

- [onClientElementColShapeLeave](mta://scripting/client/events/onclientelementcolshapeleave.md)

- [onClientElementDataChange](mta://scripting/client/events/onclientelementdatachange.md)

- [onClientElementDestroy](mta://scripting/client/events/onclientelementdestroy.md)

- [onClientElementDimensionChange](mta://scripting/client/events/onclientelementdimensionchange.md)

- [onClientElementInteriorChange](mta://scripting/client/events/onclientelementinteriorchange.md)

- onClientElementModelChange

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

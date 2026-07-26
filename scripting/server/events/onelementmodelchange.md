---
doc_id: "mta-wiki:6032"
title: "OnElementModelChange"
source_title: "OnElementModelChange"
source_url: "https://wiki.multitheftauto.com/wiki/OnElementModelChange"
revision_id: 64618
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:24.088335+00:00"
---

# OnElementModelChange

This event is triggered when the model of an [element](mta://reference/misc/element.md) is changed using [setElementModel](mta://scripting/shared/functions/setelementmodel.md).

## Parameters

```
int oldModel, int newModel
```

- **oldModel:** an [int](mta://reference/misc/int.md) representing the model of the [element](mta://reference/misc/element.md) before the change occurred.

- **newModel:** an [int](mta://reference/misc/int.md) representing the new model of the [element](mta://reference/misc/element.md).

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [element](mta://reference/misc/element.md) that changed its model

## Cancel effect

This event does NOT support [cancellation](mta://reference/misc/event-system.md). Use [setElementModel](mta://scripting/shared/functions/setelementmodel.md) with the old value to reverse.

## Example

This example sends a message to players when their model changes telling them what the model ID is and was.

```
function informPlayerOnModelChange(oldModel, newModel)
    if ( getElementType(source) == "player" ) then -- Make sure the element is a player
        outputChatBox("Model ID changing from: "..oldModel.." to: ".. newModel, source, 0, 255, 0) -- Message for player
    end
end
addEventHandler("onElementModelChange", root, informPlayerOnModelChange) -- Bind the event to every element
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

- onElementModelChange

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

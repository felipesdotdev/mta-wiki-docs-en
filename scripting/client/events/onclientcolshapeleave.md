---
doc_id: "mta-wiki:2581"
title: "OnClientColShapeLeave"
source_title: "OnClientColShapeLeave"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientColShapeLeave"
revision_id: 54478
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:17.207409+00:00"
---

# OnClientColShapeLeave

This event is triggered when a physical [element](mta://reference/misc/element.md) leaves a [colshape](mta://reference/misc/colshape.md).

## Parameters

```
element theElement, bool matchingDimension
```

- **theElement:** the [element](mta://reference/misc/element.md) that left the [colshape](mta://reference/misc/colshape.md).

- **matchingDimension:** a [boolean](mta://reference/misc/boolean.md) referring to whether the collision shape was in the same [dimension](mta://reference/misc/dimension.md) as the element.

## Source

The source of this event is the colshape that the element left.

## Example

This example outputs "Out." to the chatbox whenever the local user leaves a collision shape.

```
function onClientColShapeLeave( theElement, matchingDimension )
    if ( theElement == localPlayer ) then  -- Checks whether the leaving element is the local player
        outputChatBox( "Out." )  --Outputs.
    end
end
addEventHandler("onClientColShapeLeave", root, onClientColShapeLeave)
```

## See Also

### Client colshape events

- [onClientColShapeHit](mta://scripting/client/events/onclientcolshapehit.md)

- onClientColShapeLeave

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

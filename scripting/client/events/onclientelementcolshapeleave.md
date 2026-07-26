---
doc_id: "mta-wiki:2583"
title: "OnClientElementColShapeLeave"
source_title: "OnClientElementColShapeLeave"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientElementColShapeLeave"
revision_id: 48447
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:18.319608+00:00"
---

# OnClientElementColShapeLeave

This event is triggered when an element (like a player or vehicle) leaves a collision shape.

## Parameters

```
colshape theShape, bool matchingDimension
```

- **theShape:** the colshape that the element left.

- **matchingDimension:** *true* if the element is in the same dimension as the colshape, *false* otherwise.

## Source

The source of this event is the element that left the colshape.

## Example

This example tells player when he/she left any collision shapes that were created.

```
addEventHandler( "onClientElementColShapeLeave", getRootElement( ),
    function ( )
        if ( getElementType( source ) == "player" ) and ( source == getLocalPlayer( ) ) then
            outputChatBox( "You left colshape" );
        end
    end
);
```

## See Also

### Client element events

- [onClientElementColShapeHit](mta://scripting/client/events/onclientelementcolshapehit.md)

- onClientElementColShapeLeave

- [onClientElementDataChange](mta://scripting/client/events/onclientelementdatachange.md)

- [onClientElementDestroy](mta://scripting/client/events/onclientelementdestroy.md)

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

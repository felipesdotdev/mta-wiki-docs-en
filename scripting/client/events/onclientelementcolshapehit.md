---
doc_id: "mta-wiki:2582"
title: "OnClientElementColShapeHit"
source_title: "OnClientElementColShapeHit"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientElementColShapeHit"
revision_id: 48445
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:18.301592+00:00"
---

# OnClientElementColShapeHit

This event is triggered when an element (like a player or vehicle) enters a collision shape.

## Parameters

```
colshape theShape, bool matchingDimension
```

- **theShape:** the colshape that the element entered.

- **matchingDimension:** *true* if the element is in the same dimension as the colshape, *false* otherwise.

## Source

The source of this event is the element that entered the colshape.

## Example

This example tells player when he/she entered any collision shapes that were created.

```
addEventHandler( "onClientElementColShapeHit", getRootElement( ),
    function ( )
        if ( getElementType( source ) == "player" ) and ( source == getLocalPlayer( ) ) then
            outputChatBox( "You entered colshape" );
        end
    end
);
```

## See Also

### Client element events

- onClientElementColShapeHit

- [onClientElementColShapeLeave](mta://scripting/client/events/onclientelementcolshapeleave.md)

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

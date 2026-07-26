---
doc_id: "mta-wiki:2317"
title: "OnElementColShapeHit"
source_title: "OnElementColShapeHit"
source_url: "https://wiki.multitheftauto.com/wiki/OnElementColShapeHit"
revision_id: 75904
language: "en"
categories: ["Server_Events"]
---

# OnElementColShapeHit

This event is triggered when an player or vehicle element collides with a colshape.

## Parameters

```
colshape theColShape, bool matchingDimension
```

- **theColShape**: the [colshape](https://wiki.multitheftauto.com/index.php?search=colshape) that this [element](mta://reference/misc/element.md) collided with.

- **matchingDimension**: a [boolean](mta://reference/misc/boolean.md) representing if the [element](mta://reference/misc/element.md) and the [colshape](https://wiki.multitheftauto.com/index.php?search=colshape) are in the same [dimension](mta://reference/misc/dimension.md).

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [player](https://wiki.multitheftauto.com/index.php?search=player) or [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle) that collided with the colshape.

## Example

This example prints type of the element which entered the created colshape to chatbox.

```
colArea = createColCircle( 1400.0, -700.0, 5.0 ) -- create the colshape

function elementColShapeHit( colShapeHit )
    if colShapeHit == colArea then -- if element entered the created colshape
        outputChatBox( getElementType( source ) .. " entered the colCircle!" ) -- print the type of the element to chatbox
    end
end
addEventHandler( "onElementColShapeHit", root, elementColShapeHit ) -- add a handler function for the event
```

## See Also

### Element events

- [onElementClicked](mta://scripting/server/events/onelementclicked.md)

- onElementColShapeHit

- [onElementColShapeLeave](mta://scripting/server/events/onelementcolshapeleave.md)

- [onElementDataChange](mta://scripting/server/events/onelementdatachange.md)

- [onElementDestroy](mta://scripting/server/events/onelementdestroy.md)

- [onElementDimensionChange](mta://scripting/server/events/onelementdimensionchange.md)

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

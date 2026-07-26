---
doc_id: "mta-wiki:2318"
title: "OnElementColShapeLeave"
source_title: "OnElementColShapeLeave"
source_url: "https://wiki.multitheftauto.com/wiki/OnElementColShapeLeave"
revision_id: 59465
language: "en"
categories: ["Server_Events"]
---

# OnElementColShapeLeave

This event is triggered when an player or vehicle element leaves the area of a [colshape](https://wiki.multitheftauto.com/index.php?search=colshape).

## Parameters

```
colshape theColShape, bool matchingDimension
```

- **theColShape**: the [colshape](https://wiki.multitheftauto.com/index.php?search=colshape) that this [element](mta://reference/misc/element.md) left the area of.

- **matchingDimension**: a [boolean](mta://reference/misc/boolean.md) representing if the [element](mta://reference/misc/element.md) and the [colshape](https://wiki.multitheftauto.com/index.php?search=colshape) are in the same [dimension](mta://reference/misc/dimension.md).

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [player](https://wiki.multitheftauto.com/index.php?search=player) or [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle) that left colshape.

## Example

This example prints type of the element which left the created colshape to chatbox.

```
colArea = createColCircle( 1400.0, -700.0, 5.0 ) -- create the colshape

function elementColShapeLeave( colShapeLeft )
    if colShapeLeft == colArea then -- if element left the created colshape
        outputChatBox( getElementType( source ) .. " left the colCircle!" ) -- print the type of the element to chatbox
    end
end
addEventHandler( "onElementColShapeLeave", getRootElement(), elementColShapeLeave ) -- add a handler function for the event
```

## See Also

### Element events

- [onElementClicked](mta://scripting/server/events/onelementclicked.md)

- [onElementColShapeHit](mta://scripting/server/events/onelementcolshapehit.md)

- onElementColShapeLeave

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

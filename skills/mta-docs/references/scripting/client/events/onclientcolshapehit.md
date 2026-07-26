---
doc_id: "mta-wiki:2580"
title: "OnClientColShapeHit"
source_title: "OnClientColShapeHit"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientColShapeHit"
revision_id: 63077
language: "en"
categories: ["Client_events"]
---

# OnClientColShapeHit

This event is triggered when a physical [element](mta://reference/misc/element.md) hits a [colshape](https://wiki.multitheftauto.com/index.php?search=colshape).

| [[{{{image}}}\|link=\|]] | Note: The hit won't be detected if the element that entered the colshape is a colshape or projectile. |
| --- | --- |
|  |  |

## Parameters

```
element theElement, bool matchingDimension
```

- **theElement:** the [element](mta://reference/misc/element.md) that entered the [colshape](https://wiki.multitheftauto.com/index.php?search=colshape).

- **matchingDimension:** a [boolean](mta://reference/misc/boolean.md) referring to whether the hit collision shape was in the same [dimension](mta://reference/misc/dimension.md) as the element.

## Source

The source of this event is the colshape that was hit.

## Example

This example outputs "In." to the chatbox whenever the local user enters a collision shape.

```
function onClientColShapeHit( theElement, matchingDimension )
    if ( theElement == localPlayer ) then  -- Checks whether the entering element is the local player
        outputChatBox( "In." )  --Outputs.
    end
end
addEventHandler("onClientColShapeHit", root, onClientColShapeHit)
```

This example outputs to the chatbox if the local user is in the same dimension as the collision shape or not.

```
myZone = createColSphere (2490, -1668, 12.5, 25) -- Creates a collision sphere.

function dimensionChecker (theElement, matchingDimension)
    if matchingDimension then -- Checks whether the entering element is in the same dimension as the collision shape.
        outputChatBox ("The element is in the same dimension.")
    else
        outputChatBox ("The element is not in the same dimension.")
    end
end
addEventHandler ("onClientColShapeHit", myZone, dimensionChecker)
```

## See Also

### Client colshape events

- onClientColShapeHit

- [onClientColShapeLeave](mta://scripting/client/events/onclientcolshapeleave.md)

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

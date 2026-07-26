---
doc_id: "mta-wiki:1853"
title: "OnColShapeLeave"
source_title: "OnColShapeLeave"
source_url: "https://wiki.multitheftauto.com/wiki/OnColShapeLeave"
revision_id: 59462
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:20.782759+00:00"
---

# OnColShapeLeave

This event is triggered when a player or a vehicle leaves a collision shape.

## Parameters

```
element leaveElement, bool matchingDimension
```

- **leaveElement**: The [element](mta://reference/misc/element.md) that who exited the col shape. This can be a player or a vehicle.

- **matchingDimension**: a [boolean](mta://reference/misc/boolean.md) referring to whether the collision shape was in the same [dimension](mta://reference/misc/dimension.md) as the element.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [colshape](mta://reference/misc/colshape.md) that the element no longer is in contact with.

## Example

This example kills the player whenever they leave a certain collision shape:

```
local jailZone = createColCircle ( 1024, 1024, 15 ) -- create a collision shape

-- call 'jailZoneLeave' whenever a player leaves the collision shape:
function jailZoneLeave ( thePlayer )
   if getElementType ( thePlayer ) == "player" then -- if the element that left was player
      killPlayer ( thePlayer ) -- kill the player
      outputChatBox ( "You are not allowed to leave the jail!", thePlayer )
   end
end
addEventHandler ( "onColShapeLeave", jailZone, jailZoneLeave )
```

## See Also

### Colshape events

- [onColShapeHit](mta://scripting/server/events/oncolshapehit.md)

- onColShapeLeave

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

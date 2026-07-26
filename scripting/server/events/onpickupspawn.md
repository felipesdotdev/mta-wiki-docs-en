---
doc_id: "mta-wiki:1833"
title: "OnPickupSpawn"
source_title: "OnPickupSpawn"
source_url: "https://wiki.multitheftauto.com/wiki/OnPickupSpawn"
revision_id: 59475
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:24.359860+00:00"
---

# OnPickupSpawn

This event is triggered when a [pickup](mta://reference/misc/pickup.md) is spawned or respawned.

## Parameters

No parameters.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [pickup](mta://reference/misc/pickup.md) that just spawned or respawned.

## Example

This example gets the area and city name when a pickup spawns and outputs it to all the players.

```
function outputSpawn( )
    local area = getElementZoneName( source ) -- Get the area name where the pickup spawned
    local city = getElementZoneName( source, true ) -- Get the city name where the pickup spawned
    outputChatBox( "A pickup has spawned in " .. area .. " ( " .. city .. " )", root, 255, 0, 0 ) -- Output a message to the chatbox
end
addEventHandler( "onPickupSpawn", root, outputSpawn ) -- Trigger the function when a pickup spawns
```

## See Also

### Pickup events

- [onPickupHit](mta://scripting/server/events/onpickuphit.md)

- [onPickupLeave](mta://scripting/server/events/onpickupleave.md)

- onPickupSpawn

- [onPickupUse](mta://scripting/server/events/onpickupuse.md)

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

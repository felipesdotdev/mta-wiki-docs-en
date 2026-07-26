---
doc_id: "mta-wiki:10228"
title: "OnPickupLeave"
source_title: "OnPickupLeave"
source_url: "https://wiki.multitheftauto.com/wiki/OnPickupLeave"
revision_id: 74686
language: "en"
categories: ["Server_Events", "Changes_in_1.5.5"]
generated_at: "2026-07-26T16:16:24.347885+00:00"
---

# OnPickupLeave

This event is triggered when a [player](mta://reference/misc/player.md) leaves a [pickup](mta://reference/misc/pickup.md).

## Parameters

```
player thePlayer
```

- **thePlayer**: a [player](mta://reference/misc/player.md) element referring to the player who left the [pickup](mta://reference/misc/pickup.md).

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [pickup](mta://reference/misc/pickup.md) that was left by the player.

## Example

This example creates a pickup and outputs a message to the chat box when a player leaves it.

```
local thePickup = createPickup( 10, 10, 10, 2, 31, 3000, 50 ) -- Create a M4 weapon pickup when the script starts

function leftWeaponPickup( player )
    outputChatBox( "You have left the M4 weapon pickup.", player ) -- Output a message to the chatbox
end
addEventHandler( "onPickupLeave", thePickup, leftWeaponPickup)
```

## See Also

### Pickup events

- [onPickupHit](mta://scripting/server/events/onpickuphit.md)

- onPickupLeave

- [onPickupSpawn](mta://scripting/server/events/onpickupspawn.md)

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

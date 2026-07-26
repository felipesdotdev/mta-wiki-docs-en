---
doc_id: "mta-wiki:1834"
title: "OnPickupHit"
source_title: "OnPickupHit"
source_url: "https://wiki.multitheftauto.com/wiki/OnPickupHit"
revision_id: 59473
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:24.334940+00:00"
---

# OnPickupHit

This event is triggered when a [player](mta://reference/misc/player.md) hits a [pickup](mta://reference/misc/pickup.md).

## Parameters

```
player thePlayer
```

- **thePlayer**: a [player](mta://reference/misc/player.md) element referring to the player who moved over the [pickup](mta://reference/misc/pickup.md).

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [pickup](mta://reference/misc/pickup.md) that was hit by the player.

## Cancel effect

If this event is [canceled](mta://reference/misc/event-system.md), the pickup does not disappear and the player does not receive its bonus.

## Example

This example creates a pickup and outputs a message to the chat box when a player walks over it.

```
local thePickup = createPickup( 10, 10, 10, 2, 31, 3000, 50 ) -- Create a M4 weapon pickup when the script starts

function pickedUpWeaponCheck( player )
    outputChatBox( "You have picked up a M4.", player ) -- Output a message to the chatbox
end
addEventHandler( "onPickupHit", thePickup, pickedUpWeaponCheck )
```

## See Also

### Pickup events

- onPickupHit

- [onPickupLeave](mta://scripting/server/events/onpickupleave.md)

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

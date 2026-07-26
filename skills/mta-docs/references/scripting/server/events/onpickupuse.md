---
doc_id: "mta-wiki:1835"
title: "OnPickupUse"
source_title: "OnPickupUse"
source_url: "https://wiki.multitheftauto.com/wiki/OnPickupUse"
revision_id: 75039
language: "en"
categories: ["Server_Events"]
---

# OnPickupUse

This event is triggered when a [player](https://wiki.multitheftauto.com/index.php?search=player) stands on a [pickup](https://wiki.multitheftauto.com/index.php?search=pickup) while not in a [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle).

| [[{{{image}}}\|link=\|]] | Tip: Pickups use colshapes , you can get the colshape of the pickup with getElementColShape and use colshape events to it. |
| --- | --- |
|  |  |

## Parameters

```
player playerWhoUsed
```

- **playerWhoUsed**: a [player](https://wiki.multitheftauto.com/index.php?search=player) element referring to the player who used the [pickup](https://wiki.multitheftauto.com/index.php?search=pickup).

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [pickup](https://wiki.multitheftauto.com/index.php?search=pickup) that is getting used by the player.

### Canceling

If this event is [canceled](mta://reference/misc/event-system.md), the player will not be given the item they picked up.

## Example

This example outputs a message to the chatbox when a player uses a pickup.

```
function pickupUse( thePlayer )
    outputChatBox( getPlayerName( thePlayer ) .. " used a pickup!" )
end
addEventHandler( "onPickupUse", root, pickupUse )
```

## See Also

### Pickup events

- [onPickupHit](mta://scripting/server/events/onpickuphit.md)

- [onPickupLeave](mta://scripting/server/events/onpickupleave.md)

- [onPickupSpawn](mta://scripting/server/events/onpickupspawn.md)

- onPickupUse

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

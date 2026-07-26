---
doc_id: "mta-wiki:6960"
title: "OnClientObjectDamage"
source_title: "OnClientObjectDamage"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientObjectDamage"
revision_id: 81155
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:19.237637+00:00"
---

# OnClientObjectDamage

This event is fired before an object gets damaged.

| [[{{{image}}}\|link=\|]] | Note: This event is only triggered for objects that are streamed in. |
| --- | --- |
|  |  |

## Parameters

```
float loss, element attacker
```

- **loss:** the health loss caused by the damage. This parameter contains the theoretical loss, which could be less than 0, if you substract it of the current health. If you want to get the real loss, you have to substract the new health of the old health (use a timer for this).

- **attacker:** the vehicle/ped/player who is damaging the object.

## Source

The source of this event is the object which was damaged.

## Cancel effect

If this event is [canceled](mta://reference/misc/event-system.md), the object will not be damaged.

## Example

This example outputs the theoretical and real loss:

```
function outputLoss(loss)
    local oldHealth = getElementHealth(source)
    setTimer(function(source)
        local newHealth = getElementHealth(source)
        outputChatBox("Real loss: "..(newHealth-oldHealth))
        outputChatBox("Theoretical loss: "..loss)
    end,100,1,source)
end
addEventHandler("onClientObjectDamage", root, outputLoss)
```

## See Also

### Client object events

- [onClientObjectBreak](mta://scripting/client/events/onclientobjectbreak.md)

- onClientObjectDamage

- [onClientObjectMoveStart](mta://scripting/client/events/onclientobjectmovestart.md)

- [onClientObjectMoveStop](mta://scripting/client/events/onclientobjectmovestop.md)

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

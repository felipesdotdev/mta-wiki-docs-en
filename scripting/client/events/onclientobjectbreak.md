---
doc_id: "mta-wiki:7038"
title: "OnClientObjectBreak"
source_title: "OnClientObjectBreak"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientObjectBreak"
revision_id: 81176
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:19.220149+00:00"
---

# OnClientObjectBreak

This event is fired before an object breaks.

| [[{{{image}}}\|link=\|]] | Note: This event is only triggered for objects that are streamed in |
| --- | --- |
|  |  |

## Parameters

```
element attacker
```

- **attacker:** the vehicle/ped/player who is breaking the object

## Source

The source of this event is the object which will break.

## Cancel effect

If this event is [canceled](mta://reference/misc/event-system.md), the object will not break.

## Example

Click to collapse [-]
Client

This example prevents objects from beeing broken in interiors.

```
addEventHandler("onClientObjectBreak", root,
    function()
        if getElementInterior(source) ~= 0 then
            cancelEvent()
        end
    end
)
```

## See Also

### Client object events

- onClientObjectBreak

- [onClientObjectDamage](mta://scripting/client/events/onclientobjectdamage.md)

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

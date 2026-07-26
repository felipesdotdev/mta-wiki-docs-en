---
doc_id: "mta-wiki:12686"
title: "OnClientObjectMoveStart"
source_title: "OnClientObjectMoveStart"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientObjectMoveStart"
revision_id: 81295
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:19.250125+00:00"
---

# OnClientObjectMoveStart

This event is triggered when an [object](mta://reference/misc/object.md) starts moving.

## Parameters

None.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [object](mta://reference/misc/object.md) which was moved.

## Example

```
local obj = createObject (5239, -2417.22339, -606.70374, 132.56250)
moveObject (obj, 3000, -2417.22339, -606.70374, 137.56250)

addEventHandler ("onClientObjectMoveStart", obj,
    function ()
        outputChatBox ("Object started moving!")
    end
)
```

## See Also

### Client object events

- [onClientObjectBreak](mta://scripting/client/events/onclientobjectbreak.md)

- [onClientObjectDamage](mta://scripting/client/events/onclientobjectdamage.md)

- onClientObjectMoveStart

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

---
doc_id: "mta-wiki:12687"
title: "OnClientObjectMoveStop"
source_title: "OnClientObjectMoveStop"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientObjectMoveStop"
revision_id: 81296
language: "en"
categories: ["Client_events"]
---

# OnClientObjectMoveStop

This event is triggered when an [object](https://wiki.multitheftauto.com/index.php?search=object)'s movements stop.

## Parameters

None.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [object](https://wiki.multitheftauto.com/index.php?search=object) which was moved.

## Example

```
local obj = createObject (5239, -2417.22339, -606.70374, 132.56250)
moveObject (obj, 3000, -2417.22339, -606.70374, 137.56250)

addEventHandler ("onClientObjectMoveStop", obj,
    function ()
        outputChatBox ("Object stopped moving!")
    end
)
```

## See Also

### Client object events

- [onClientObjectBreak](mta://scripting/client/events/onclientobjectbreak.md)

- [onClientObjectDamage](mta://scripting/client/events/onclientobjectdamage.md)

- [onClientObjectMoveStart](mta://scripting/client/events/onclientobjectmovestart.md)

- onClientObjectMoveStop

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

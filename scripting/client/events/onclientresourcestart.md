---
doc_id: "mta-wiki:2552"
title: "OnClientResourceStart"
source_title: "OnClientResourceStart"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientResourceStart"
revision_id: 22433
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:20.297827+00:00"
---

# OnClientResourceStart

This event is triggered when a [resource](mta://reference/misc/resource.md) is started.  Please note that this is **not** triggered the same time as the serverside event [onResourceStart](mta://scripting/server/events/onresourcestart.md) is.  The event is triggered when any *clientside resources* are started.  This means it is triggered when a clientside script is initiated after a download, which includes downloading after join. So:

- If a resource is running **before** a player joins, the onClientResourceStart event will be triggered after they join and have downloaded that resource.

- If a resource is started **after** a player has joined, the player will be made to download the required files, and then the onClientResourceStart event will be triggered.

## Parameters

```
resource startedResource
```

- **startedResource**: the [resource](mta://reference/misc/resource.md) that was started.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the started resource's [root element](mta://reference/misc/root-element.md).

## Example

This example outputs name of resource that was started.

```
addEventHandler( "onClientResourceStart", getRootElement( ),
    function ( startedRes )
        outputChatBox( "Resource started: " .. getResourceName( startedRes ) );
    end
);
```

## See Also

### Client resource events

- [onClientResourceFileDownload](mta://scripting/client/events/onclientresourcefiledownload.md)

- onClientResourceStart

- [onClientResourceStop](mta://scripting/client/events/onclientresourcestop.md)

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

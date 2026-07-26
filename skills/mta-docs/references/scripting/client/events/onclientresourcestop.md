---
doc_id: "mta-wiki:2553"
title: "OnClientResourceStop"
source_title: "OnClientResourceStop"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientResourceStop"
revision_id: 64214
language: "en"
categories: ["Client_events"]
---

# OnClientResourceStop

This event is triggered when a [resource](mta://reference/misc/resource.md) is being stopped.

## Parameters

```
resource stoppedResource
```

- **stoppedResource**: the [resource](mta://reference/misc/resource.md) that is about to get stopped.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the stopped resource [root element](https://wiki.multitheftauto.com/index.php?search=root%20element).

## Example

This example outputs name of resource that was stopped.

```
addEventHandler( "onClientResourceStop", getRootElement( ),
    function ( stoppedRes )
        outputChatBox( "Resource stopped: " .. getResourceName( stoppedRes ) );
    end
);
```

## See Also

### Client resource events

- [onClientResourceFileDownload](mta://scripting/client/events/onclientresourcefiledownload.md)

- [onClientResourceStart](mta://scripting/client/events/onclientresourcestart.md)

- onClientResourceStop

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

---
doc_id: "mta-wiki:2449"
title: "OnResourceStop"
source_title: "OnResourceStop"
source_url: "https://wiki.multitheftauto.com/wiki/OnResourceStop"
revision_id: 64503
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:26.316000+00:00"
---

# OnResourceStop

This event is triggered when the resource is stopped. This can occur for a number of reasons:

- The *stop* console command was used

- The *restart* console command was used

- The resource was modified (the resource will automatically restart)

- Another resource stopped it using [stopResource](mta://scripting/server/functions/stopresource.md).

**Note:** If you wish to just detect a single resource being stopped, you should attach handlers for this event to the resource's root element. You can access this using [getResourceRootElement](mta://scripting/shared/functions/getresourcerootelement.md).

## Parameters

```
resource stoppedResource, boolean wasDeleted
```

- **stoppedResource**: the [resource](mta://reference/misc/resource.md) that is being stopped.

- **wasDeleted**: a [boolean](mta://reference/misc/boolean.md) representing whether the resource folder was deleted, moved or renamed.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the root [element](mta://reference/misc/element.md) of the resource that is being stopped.

## Example

This example displays a message in the chatbox when a resource is stopped.

```
addEventHandler( "onResourceStop", root,
    function( resource )
        outputChatBox( "The resource " .. getResourceName( resource ) .. " was stopped!", root )
    end
)
```

This example only outputs message if the stopped resource is the same resource where the eventHandler is.

```
addEventHandler( "onResourceStop", resourceRoot,
    function( resource )
        outputChatBox( "This resource has stopped!", root )
   end
)
```

## Changelog

| Version | Description |
| --- | --- |

| 1.5.5-9.11854 | Added wasDeleted parameter |
| --- | --- |

## See Also

### Resource events

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22430](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22430))

- [onResourceStateChange](mta://scripting/server/events/onresourcestatechange.md)

- [onPlayerResourceStart](mta://scripting/server/events/onplayerresourcestart.md)

- [onResourceLoadStateChange](mta://scripting/server/events/onresourceloadstatechange.md)

- [onResourcePreStart](mta://scripting/server/events/onresourceprestart.md)

- [onResourceStart](mta://scripting/server/events/onresourcestart.md)

- onResourceStop

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

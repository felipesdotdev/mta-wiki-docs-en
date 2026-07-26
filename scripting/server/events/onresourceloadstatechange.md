---
doc_id: "mta-wiki:12685"
title: "OnResourceLoadStateChange"
source_title: "OnResourceLoadStateChange"
source_url: "https://wiki.multitheftauto.com/wiki/OnResourceLoadStateChange"
revision_id: 81294
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:26.234525+00:00"
---

# OnResourceLoadStateChange

This event is triggered when a [resource](mta://reference/misc/resource.md) load state is changed.

## Parameters

```
resource changedResource, string oldState, string newState
```

- **changedResource**: The [resource](mta://reference/misc/resource.md) that was either loaded, reloaded or is unloading.

- **oldState**: The state the [resource](mta://reference/misc/resource.md) was in before it changed.

- **newState**: The state the [resource](mta://reference/misc/resource.md) has changed to.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the root [element](mta://reference/misc/element.md).

## Example

This code will output the state of resource when it's state will be changed:

```
function onResourceLoadStateChange (resource, oldState, newState)
    print ("Resource "..getResourceName (resource).." has changed it's state from "..tostring (oldState).." to "..tostring (newState))
end

addEventHandler ("onResourceLoadStateChange", root, onResourceLoadStateChange)
```

## See Also

### Resource events

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22430](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22430))

- [onResourceStateChange](mta://scripting/server/events/onresourcestatechange.md)

- [onPlayerResourceStart](mta://scripting/server/events/onplayerresourcestart.md)

- onResourceLoadStateChange

- [onResourcePreStart](mta://scripting/server/events/onresourceprestart.md)

- [onResourceStart](mta://scripting/server/events/onresourcestart.md)

- [onResourceStop](mta://scripting/server/events/onresourcestop.md)

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

---
doc_id: "mta-wiki:14296"
title: "OnResourceStateChange"
source_title: "OnResourceStateChange"
source_url: "https://wiki.multitheftauto.com/wiki/OnResourceStateChange"
revision_id: 82080
language: "en"
categories: ["Server_Events"]
---

# OnResourceStateChange

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22430](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22430))

This event is triggered when a [resource](mta://reference/misc/resource.md)'s state is changed.
This event is an extended version of [onResourceLoadStateChange](mta://scripting/server/events/onresourceloadstatechange.md)

| [[{{{image}}}\|link=\|]] | Note: Possible states: loaded - when resource is loaded but not running running - when resource is loaded and running starting - when resource is starting stopping - when resource is stopping unloaded - when resource is not loaded |
| --- | --- |
|  |  |

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
addEventHandler('onResourceStateChange', root, function(res, oldState, newState)
    iprint('Resource '..getResourceName(res)..' has changed its state from '..oldState..' to '..newState)
end)
```

## See Also

### Resource events

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22430](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22430))

- onResourceStateChange

- [onPlayerResourceStart](mta://scripting/server/events/onplayerresourcestart.md)

- [onResourceLoadStateChange](mta://scripting/server/events/onresourceloadstatechange.md)

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

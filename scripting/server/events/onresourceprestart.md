---
doc_id: "mta-wiki:4544"
title: "OnResourcePreStart"
source_title: "OnResourcePreStart"
source_url: "https://wiki.multitheftauto.com/wiki/OnResourcePreStart"
revision_id: 72071
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:26.252137+00:00"
---

# OnResourcePreStart

Analogous to [onResourceStart](mta://scripting/server/events/onresourcestart.md), but triggered before script files are initialised.

| [[{{{image}}}\|link=\|]] | Note: This event isn't triggered within the resource starting. |
| --- | --- |
|  |  |

## Parameters

```
resource startingResource
```

- **startingResource**: the [resource](mta://reference/misc/resource.md) that is starting.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the root [element](mta://reference/misc/element.md).

## Cancel effect

If this event is cancelled, the resource won't begin starting.

## Example

This code will output the name of any resource that is starting.

```
function displayStartingRes(res)
	outputChatBox("Resource "..getResourceName(res).." is going to start.", root, 255, 255, 255)
end
addEventHandler("onResourcePreStart", root, displayStartingRes)
```

## See Also

### Resource events

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22430](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22430))

- [onResourceStateChange](mta://scripting/server/events/onresourcestatechange.md)

- [onPlayerResourceStart](mta://scripting/server/events/onplayerresourcestart.md)

- [onResourceLoadStateChange](mta://scripting/server/events/onresourceloadstatechange.md)

- onResourcePreStart

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

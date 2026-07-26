---
doc_id: "mta-wiki:2446"
title: "OnResourceStart"
source_title: "OnResourceLoad"
source_url: "https://wiki.multitheftauto.com/wiki/OnResourceLoad"
revision_id: 71142
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:26.214936+00:00"
---

# OnResourceStart

This event is triggered when a resource is started.

**Important:** If you attach this event to the root element it will called when *any* resource starts, not just the resource your script is running inside. As such, most of the time you will want to check that the resource passed to this event matches your resource (compare with the value returned by [getThisResource](mta://scripting/shared/functions/getthisresource.md) before doing anything. Alternatively you can attach the event to resourceRoot.

## Parameters

```
resource startedResource
```

- **startedResource**: the [resource](mta://reference/misc/resource.md) that was started.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the root [element](mta://reference/misc/element.md) in the resource that started.

## Cancel effect

If this event is [canceled](mta://reference/misc/event-system.md), the resource starting is aborted and is stopped again.

## Example

Click to collapse [-]
Example 1

This code will output the name of any resource that is started.

```
function displayLoadedRes ( res )
	outputChatBox ( "Resource " .. getResourceName(res) .. " loaded", root, 255, 255, 255 )
end
addEventHandler ( "onResourceStart", root, displayLoadedRes )
```

## See Also

### Resource events

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22430](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22430))

- [onResourceStateChange](mta://scripting/server/events/onresourcestatechange.md)

- [onPlayerResourceStart](mta://scripting/server/events/onplayerresourcestart.md)

- [onResourceLoadStateChange](mta://scripting/server/events/onresourceloadstatechange.md)

- [onResourcePreStart](mta://scripting/server/events/onresourceprestart.md)

- onResourceStart

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

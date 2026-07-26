---
doc_id: "mta-wiki:13360"
title: "OnPlayerResourceStart"
source_title: "OnPlayerResourceStart"
source_url: "https://wiki.multitheftauto.com/wiki/OnPlayerResourceStart"
revision_id: 81315
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:25.367575+00:00"
---

# OnPlayerResourceStart

This event is triggered when a [resource](mta://reference/misc/resource.md) has loaded client-side for a [player](mta://reference/misc/player.md).

## Parameters

```
resource loadedResource
```

- **loadedResource**: The [resource](mta://reference/misc/resource.md) that was loaded on the client.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [player](mta://reference/misc/player.md) who loaded the resource.

## Example

This example shows how you can trigger a custom event client-side defined in the same resource as soon as the player is ready (resource loaded on client):

```
function onPlayerResourceStart(startedResource)
	local resourceName = getResourceName(startedResource)
	local playerName = getPlayerName(source)
	local matchingResource = (startedResource == resource) -- 'resource' is predefined variable, see: https://wiki.multitheftauto.com/wiki/Predefined_variables_list#MTA_Predefined_variables
	local chatMessage = (resourceName.." has started for "..playerName)

	outputChatBox(chatMessage) -- display message when any resource starts for player

	if (not matchingResource) then -- check if startedResource matches current, if it doesn't do not trigger custom event
		return false
	end

	triggerClientEvent(source, "onClientCustomEvent", resourceRoot) -- send a custom clientside event defined in this resource, for specific player (source) only
end
addEventHandler("onPlayerResourceStart", root, onPlayerResourceStart)
```

## See Also

### Resource events

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22430](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22430))

- [onResourceStateChange](mta://scripting/server/events/onresourcestatechange.md)

- onPlayerResourceStart

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

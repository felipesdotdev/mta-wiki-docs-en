---
doc_id: "mta-wiki:3854"
title: "OnClientElementStreamIn"
source_title: "OnClientElementStreamIn"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientElementStreamIn"
revision_id: 81799
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:18.427400+00:00"
---

# OnClientElementStreamIn

This event is triggered whenever a physical element is streamed in. This is triggered for all elements that are streamable, such as players, peds, vehicles, objects and markers. When this event is triggered, that element is guaranteed to be physically created as a GTA object.

Be aware that this event triggers for local player (as itself being the element that got streamed in) when said local player spawns, as this is the creation of entity local ped.

| [[{{{image}}}\|link=\|]] | Note: This event also triggers for a remote player that dies in front of local player, even if they respawn far away.. the moment they do so, this event will be triggered, and if you'd measure distance between local and said remote player (that spawned far away) during this event, it would output the distance at which they died in front of local player, e.g 2 metres. This is bug-prone behavior and likely incorrect, to be fixed in the future, but for now be aware. The 'low distance' aspect of this (which could worsen your results) is caused by the split second that their ped elements may 'flash' past its wasted location during the respawning process. For now you can work around these side effect (both, or the distance aspect.. results may vary based on randomness) by adding an isPedDead check inside the event, checking source (said remote player), as this delays the onClientElementIn until after full respawn has taken place. The below script example incorporates this workaround |
| --- | --- |
|  |  |

## Parameters

No parameters.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [element](mta://reference/misc/element.md) that streamed in.

## Example

This example shows you how to tell player that another player was streamed in and the distance between them and said player

```
function onClientElementStreamIn()
	local validElement = isElement(source)

	if (not validElement) then
		return false
	end

	local elementType = getElementType(source)
	local playerType = (elementType == "player")

	if (not playerType) then
		return false
	end

	local pedDead = isPedDead(source)

	if (pedDead) then
		return false
	end

	local localX, localY, localZ = getElementPosition(localPlayer)
	local playerX, playerY, playerZ = getElementPosition(source)
	local distanceBetweenPlayers = getDistanceBetweenPoints3D(localX, localY, localZ, playerX, playerY, playerZ)

	outputChatBox("A player has just streamed in. Distance to the player: "..distanceBetweenPlayers)
end
addEventHandler("onClientElementStreamIn", root, onClientElementStreamIn)
```

## See Also

### Client element events

- [onClientElementColShapeHit](mta://scripting/client/events/onclientelementcolshapehit.md)

- [onClientElementColShapeLeave](mta://scripting/client/events/onclientelementcolshapeleave.md)

- [onClientElementDataChange](mta://scripting/client/events/onclientelementdatachange.md)

- [onClientElementDestroy](mta://scripting/client/events/onclientelementdestroy.md)

- [onClientElementDimensionChange](mta://scripting/client/events/onclientelementdimensionchange.md)

- [onClientElementInteriorChange](mta://scripting/client/events/onclientelementinteriorchange.md)

- [onClientElementModelChange](mta://scripting/client/events/onclientelementmodelchange.md)

- onClientElementStreamIn

- [onClientElementStreamOut](mta://scripting/client/events/onclientelementstreamout.md)

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

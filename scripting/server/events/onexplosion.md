---
doc_id: "mta-wiki:14089"
title: "OnExplosion"
source_title: "OnExplosion"
source_url: "https://wiki.multitheftauto.com/wiki/OnExplosion"
revision_id: 82642
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:24.150749+00:00"
---

# OnExplosion

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r21914](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21914))

This event is triggered every time an explosion is created either by server-side [createExplosion](mta://scripting/shared/functions/createexplosion.md), or when reported by [player](mta://reference/misc/player.md).

## Parameters

```
float x, float y, float z, int theType
```

- **x:** X coordinate of where the explosion was created

- **y:** Y coordinate of where the explosion was created

- **z:** Z coordinate of where the explosion was created

- **theType:** the type of explosion created, see: [Explosion types](mta://reference/misc/explosion-types.md)

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [player](mta://reference/misc/player.md) who notified server about explosion, or [root](mta://reference/misc/root.md) if explosion was created server-side along without specifying creator in [createExplosion](mta://scripting/shared/functions/createexplosion.md).

### Canceling

If this event is [canceled](mta://reference/misc/event-system.md), the explosion will not occur.
If an explosion is notified by a player, that explosion will still be visible to this player.

## Example

This example outputs information about occuring explosion.

```
local debugMsgLevel = 4
local debugMsgR = 255
local debugMsgG = 127
local debugMsgB = 0
local explosionTypes = {
	[0] = "Grenade",
	[1] = "Molotov",
	[2] = "Rocket",
	[3] = "Rocket Weak",
	[4] = "Car",
	[5] = "Car Quick",
	[6] = "Boat",
	[7] = "Aircraft",
	[8] = "Mine",
	[9] = "Object",
	[10] = "Tank Grenade",
	[11] = "Small",
	[12] = "Tiny",
}

function onExplosion(explosionX, explosionY, explosionZ, explosionType)
	local explosionPos = explosionX..", "..explosionY..", "..explosionZ
	local explosionTypeName = explosionTypes[explosionType]
	local explosionSource = inspect(source)
	local debugMsg = explosionTypeName.." explosion has occured at "..explosionPos.." (source: "..explosionSource..")"

	outputDebugString(debugMsg, debugMsgLevel, debugMsgR, debugMsgG, debugMsgB)
end
addEventHandler("onExplosion", root, onExplosion)
```

## See Also

### Server events

- [onBan](mta://scripting/server/events/onban.md)

- [onChatMessage](mta://scripting/server/events/onchatmessage.md)

- [onDebugMessage](mta://scripting/server/events/ondebugmessage.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r21914](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21914))

- onExplosion

- [onSettingChange](mta://scripting/server/events/onsettingchange.md)

- [onUnban](mta://scripting/server/events/onunban.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22837](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22837):

- [onShutdown](mta://scripting/server/events/onshutdown.md)

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

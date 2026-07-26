---
doc_id: "mta-wiki:3462"
title: "OnUnban"
source_title: "OnUnban"
source_url: "https://wiki.multitheftauto.com/wiki/OnUnban"
revision_id: 59521
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:26.440828+00:00"
---

# OnUnban

This event is triggered when a ban is removed from the server.

if the ban was removed using function [removeBan](mta://scripting/server/functions/removeban.md), and the responsibleElement was not specifying, the event will return nil.

## Parameters

```
ban theBan, player responsibleElement
```

- **theBan**: the [ban](mta://reference/misc/ban.md) that will be removed.

- **responsibleElement**: the [player](mta://reference/misc/player.md) who removed the ban, otherwise returns *nil*.

## Source

The source is always the global root element.

## Cancel effect

If this event is [canceled](mta://reference/misc/event-system.md), the requested unban is not performed.

## Example

This example does...

```
root = getRootElement()

function announceUnban( theBan, responsibleElement )
	if getElementType( responsibleElement ) then --Check if a player unbanned the IP/Serial
		outputChatBox( getPlayerName( responsibleElement ) .. " unbanned " .. ( getBanSerial(theBan) or getBanIP(theBan) ) ) --Output to the chatbox saying the player has unbanned the IP/Serial
	end
end

addEventHandler( "onUnban", root, announceUnban ) --Adds the event handler for 'onUnban'
```

## Changelog

| Version | Description |
| --- | --- |

| 1.3.0-9.03908 | Fixed/added responsible element parameter |
| --- | --- |

## See Also

### Server events

- [onBan](mta://scripting/server/events/onban.md)

- [onChatMessage](mta://scripting/server/events/onchatmessage.md)

- [onDebugMessage](mta://scripting/server/events/ondebugmessage.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r21914](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21914))

- [onExplosion](mta://scripting/server/events/onexplosion.md)

- [onSettingChange](mta://scripting/server/events/onsettingchange.md)

- onUnban

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

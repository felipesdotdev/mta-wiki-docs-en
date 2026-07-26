---
doc_id: "mta-wiki:3461"
title: "OnBan"
source_title: "OnBan"
source_url: "https://wiki.multitheftauto.com/wiki/OnBan"
revision_id: 67290
language: "en"
categories: ["Server_Events"]
---

# OnBan

This event is triggered when an IP address or serial is banned from the server.

## Parameters

```
ban theBan
```

- **theBan**: the [ban](mta://reference/misc/ban.md) which was added.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [element](mta://reference/misc/element.md) that was responsible for the banning. If no responsible was specified, the source is the global root element.

## Cancel effect

This event cannot be canceled.

## Example

This example outputs a simple message to all players when a player added a ban.

```
function announceBan( theBan )
   if ( isElement( source ) ) and ( getElementType( source ) == "player" ) then -- Check if the element responsible for the ban is a player element
	outputChatBox( getPlayerName( source ) .. " banned " .. ( getBanSerial( theBan ) or getBanIP( theBan ) ) ) -- Output to the chatbox saying the player has banned the IP/Serial
   end
end
addEventHandler( "onBan", root, announceBan ) -- Adds the event handler for "onBan" and must be bound to root
```

## See Also

### Server events

- onBan

- [onChatMessage](mta://scripting/server/events/onchatmessage.md)

- [onDebugMessage](mta://scripting/server/events/ondebugmessage.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r21914](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21914))

- [onExplosion](mta://scripting/server/events/onexplosion.md)

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

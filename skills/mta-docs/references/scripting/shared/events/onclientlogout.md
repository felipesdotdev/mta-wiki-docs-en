---
doc_id: "mta-wiki:1878"
title: "OnClientLogout"
source_title: "OnClientLogout"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientLogout"
revision_id: 44575
language: "en"
categories: ["Server_Events", "Deprecated"]
---

# OnClientLogout

|  | This event is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use onPlayerLogout instead. |  |

This event is triggered when a user logs out of their account in-game.

## Parameters

```
account thePreviousAccount, account theCurrentAccount
```

- **thePreviousAccount**: The account the client was logged in as

- **theCurrentAccount**: The account the client is a part of now (usually a guest account)

## Source

The [source](mta://reference/misc/event-system.md) of this event is the client [element](mta://reference/misc/element.md) that logged out. For example a player.

## Example

This example displays a message if the client logs out.

```
function loggedOut()
	outputChatBox( "You have successfully logged out!", source )
end
addEventHandler("onClientLogout",getRootElement(),loggedOut)
```

## See Also

### Client events

- [onConsole](mta://scripting/server/events/onconsole.md)

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

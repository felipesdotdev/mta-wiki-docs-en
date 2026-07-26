---
doc_id: "mta-wiki:3804"
title: "OnClientChangeNick"
source_title: "OnClientChangeNick"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientChangeNick"
revision_id: 44014
language: "en"
categories: ["Server_Events", "Deprecated"]
---

# OnClientChangeNick

|  | This event is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use onPlayerChangeNick instead. |  |

This event is triggered when a player changes his nickname.

## Parameters

```
string oldNick, string newNick
```

- **oldNick:** the nickname the player had before.

- **newNick:** the new nickname of the player.

## Source

The source of this event is the player that changed his nick

## Example

```
function nickChangeHandler(oldNick, newNick)
outputChatBox(oldNick.." is now known as "..newNick, getRootElement(), 255, 100, 100) -- display the message
end
addEventHandler("onClientChangeNick", getRootElement(), nickChangeHandler) -- add an event handler
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

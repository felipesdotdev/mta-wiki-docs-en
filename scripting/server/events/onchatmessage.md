---
doc_id: "mta-wiki:5864"
title: "OnChatMessage"
source_title: "OnChatMessage"
source_url: "https://wiki.multitheftauto.com/wiki/OnChatMessage"
revision_id: 82030
language: "en"
categories: ["Server_Events", "Changes_in_1.2"]
generated_at: "2026-07-26T16:16:16.965049+00:00"
---

# OnChatMessage

This event is triggered when any message is output to chat using [outputChatBox](mta://scripting/shared/functions/outputchatbox.md) server-side (also when a player uses *say*, *teamsay* or *me* successfully).

| [[{{{image}}}\|link=\|]] | Note: It can be used to get the element responsible for a specific outputChatBox call via the second parameter. |
| --- | --- |
|  |  |

## Parameters

```
string theMessage, element theElement
```

- **theMessage:** A [string](mta://reference/misc/string.md) representing the text that was output to the chatbox.

- **theElement:** A [resource](mta://reference/misc/resource.md) if it was done via [outputChatBox](mta://scripting/shared/functions/outputchatbox.md) or a [player](mta://reference/misc/player.md) element if it was done via *say*, *teamsay* or *me*.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the root element.

## Example

This example outputs all chat messages to debug view.

```
function onChatMessageHandler(theMessage, thePlayer)
	outputDebugString(theMessage)
end
addEventHandler("onChatMessage", root, onChatMessageHandler)
```

## See Also

### Server events

- [onBan](mta://scripting/server/events/onban.md)

- onChatMessage

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

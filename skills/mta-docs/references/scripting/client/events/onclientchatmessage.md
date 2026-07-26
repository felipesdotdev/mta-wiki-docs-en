---
doc_id: "mta-wiki:4552"
title: "OnClientChatMessage"
source_title: "OnClientChatMessage"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientChatMessage"
revision_id: 72868
language: "en"
categories: ["Client_events"]
---

# OnClientChatMessage

This event is triggered when any text is output to chatbox, including MTA's internal messages.

## Parameters

```
string text, int r, int g, int b, int messageType
```

- **text:** The text that was output to chatbox.

- **r:** The amount of red in the color of the text.

- **g:** The amount of green in the color of the text.

- **b:** The amount of blue in the color of the text.

- **messageType:** The type of message as a number.

- **0:** normal message

- **1:** action message (/me)

- **2:** team message

- **3:** private message

- **4:** internal message

## Source

The [source](mta://reference/misc/event-system.md) of this event is either a [player](https://wiki.multitheftauto.com/index.php?search=player) element or the [root](https://wiki.multitheftauto.com/index.php?search=root) element.

## Cancel effect

If this event is [canceled](mta://reference/misc/event-system.md), the game's chat system won't deliver the posts. You may use [outputChatBox](mta://scripting/shared/functions/outputchatbox.md) to send the messages then.

## Example

This example doesn't output anything to chatbox if it consists only of numbers

```
function onClientChatMessageHandler(text)
	if string.match(text,"%d+") --[[string.match searches for pattern "%d+", means decimals]] == text then -- if string.match and text itself are the same
		cancelEvent() -- don't output it
	end
end
addEventHandler("onClientChatMessage", root, onClientChatMessageHandler)
```

## See Also

### Client other events

- onClientChatMessage

- [onClientConsole](mta://scripting/client/events/onclientconsole.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22649](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22649):

- [onClientCoreCommand](mta://scripting/client/events/onclientcorecommand.md)

- [onClientDebugMessage](mta://scripting/client/events/onclientdebugmessage.md)

- [onClientExplosion](mta://scripting/client/events/onclientexplosion.md)

- [onClientFileDownloadComplete](mta://scripting/client/events/onclientfiledownloadcomplete.md)

- [onClientHUDRender](mta://scripting/client/events/onclienthudrender.md)

- [onClientMinimize](mta://scripting/client/events/onclientminimize.md)

- [onClientMTAFocusChange](mta://scripting/client/events/onclientmtafocuschange.md)

- [onClientPedsProcessed](mta://scripting/client/events/onclientpedsprocessed.md)

- [onClientPlayerNetworkStatus](mta://scripting/client/events/onclientplayernetworkstatus.md)

- [onClientPreRender](mta://scripting/client/events/onclientprerender.md)

- [onClientRender](mta://scripting/client/events/onclientrender.md)

- [onClientRestore](mta://scripting/client/events/onclientrestore.md)

- [onClientTransferBoxProgressChange](mta://scripting/client/events/onclienttransferboxprogresschange.md)

- [onClientTransferBoxVisibilityChange](mta://scripting/client/events/onclienttransferboxvisibilitychange.md)

- [onClientWorldSound](mta://scripting/client/events/onclientworldsound.md)

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

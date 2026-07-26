---
doc_id: "mta-wiki:5471"
title: "OnClientDebugMessage"
source_title: "OnClientDebugMessage"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientDebugMessage"
revision_id: 69810
language: "en"
categories: ["Client_events", "Changes_in_1.5.7"]
generated_at: "2026-07-26T16:16:17.287346+00:00"
---

# OnClientDebugMessage

This event is triggered when client-side debug messages (for instance errors or warnings) would appear in the debug window. This event doesn't require the debug window to be enabled to trigger, however.

**Note:** To prevent infinite loops, debug messages that occur inside the function that handles this event won't trigger this event, so you won't be able to rely on debug info to fix faulty code that is inside this function. Since build [r14683](https://buildinfo.mtasa.com/index.php?Revision=14683) debug messages from [outputDebugString](mta://scripting/shared/functions/outputdebugstring.md) and [iprint](mta://scripting/shared/functions/iprint.md) will show up.

## Parameters

```
string message, int level, string file, int line, int r, int g, int b
```

- **message**: The message which was outputted in the server console, without details like file, line etc

- **level**: The type of debug message which was outputted

- **0:** "Custom" message

- **1:** Error message

- **2:** Warning message

- **3:** Information message

- **file**: The file from which the debug message was outputted

- **Note:** May return [nil](mta://reference/misc/nil.md) when the source could not be found

- **line**: The line in file **file** where the debug message was outputted

- **Note:** May return [nil](mta://reference/misc/nil.md) when the source could not be found

- **r**: Amount of red color (0-255)

- **g**: Amount of green color (0-255)

- **b**: Amount of blue color (0-255)

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [root element](mta://reference/misc/root-element.md).

## Examples

This example outputs the debug message in the console.

```
function onClientDebugMessage(message, level, file, line)
	outputConsole(message)
end
addEventHandler("onClientDebugMessage", root, onClientDebugMessage)
```

This example tells players that they missed a debug message, if they don't have debugscript enabled.

```
function newDebug()
	if not isDebugViewActive() then -- If their debug view is not active
		outputChatBox("* You just missed a debug message. Use the \'/debugscript\' command to view it.", 255, 0, 0) -- Output to them that they missed a debug message
	end
end
addEventHandler("onClientDebugMessage", root, newDebug) -- When we get a new client debug message, call the newDebug function
```

## See Also

### Other client events

- [onClientChatMessage](mta://scripting/client/events/onclientchatmessage.md)

- [onClientConsole](mta://scripting/client/events/onclientconsole.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22649](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22649):

- [onClientCoreCommand](mta://scripting/client/events/onclientcorecommand.md)

- onClientDebugMessage

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

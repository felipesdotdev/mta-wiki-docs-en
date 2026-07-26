---
doc_id: "mta-wiki:5470"
title: "OnDebugMessage"
source_title: "OnDebugMessage"
source_url: "https://wiki.multitheftauto.com/wiki/OnDebugMessage"
revision_id: 79532
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:20.819888+00:00"
---

# OnDebugMessage

This event is triggered when debug messages (for instance errors or warnings) appear in the server console.

**Note:** To prevent infinite loops, debug messages that occur inside the function that handles this event won't trigger this event, so you won't be able to rely on debug info to fix faulty code that is inside this function. Since build [r14683](https://buildinfo.mtasa.com/index.php?Revision=14683) debug messages from [outputDebugString](mta://scripting/shared/functions/outputdebugstring.md) and [iprint](mta://scripting/shared/functions/iprint.md) will show up.

## Parameters

```
string message, int level, string file, int line, int r, int g, int b
```

- **message**: the message which was outputted in the server console, without details like file, line etc.

- **level**: the type of debug message which was outputted.

- **0:** *"Custom"* message.

- **1:** *Error* message.

- **2:** *Warning* message.

- **3:** *Information* message.

- **file**: the file from which the debug message was outputted.

- **Note:** may return [nil](mta://reference/misc/nil.md) when the source could not be found.

- **line**: the line in file **file** where the debug message was outputted.

- **Note:** may return [nil](mta://reference/misc/nil.md) when the source could not be found.

- **r**: an [int](mta://reference/misc/int.md) representing the amount of red color (0-255).

- **g**: an [int](mta://reference/misc/int.md) representing the amount of green color (0-255).

- **b**: an [int](mta://reference/misc/int.md) representing the amount of blue color (0-255).

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [root element](mta://reference/misc/root-element.md).

## Canceling

If this event is [canceled](mta://reference/misc/event-system.md), the debug message won't appear.

## Example

This example outputs error debug messages to chat.

```
function onDebugMessage(debugMessage, debugLevel, debugFile, debugLine, debugRed, debugGreen, debugBlue)
	local debugError = (debugLevel == 1)

	if (not debugError) then
		return false
	end

	local debugAtFile = (debugFile and debugFile or "NO_FILE")
	local debugAtLine = (debugLine and debugLine or "NO_LINE")
	local debugChatMessage = "ERROR: "..debugAtFile..":"..debugAtLine..": "..debugMessage

	outputChatBox(debugChatMessage, root, debugRed, debugGreen, debugBlue)
end
addEventHandler("onDebugMessage", root, onDebugMessage)
```

## See Also

### Server events

- [onBan](mta://scripting/server/events/onban.md)

- [onChatMessage](mta://scripting/server/events/onchatmessage.md)

- onDebugMessage

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

---
doc_id: "mta-wiki:1825"
title: "OnConsole"
source_title: "OnConsole"
source_url: "https://wiki.multitheftauto.com/wiki/OnConsole"
revision_id: 59460
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:20.796913+00:00"
---

# OnConsole

This event is triggered when a player types a message into his console. It is also triggered when entering '/' commands via the chatbox.

| [[{{{image}}}\|link=\|]] | Note: The event will not be triggered if the message can be processed by an existing command handler |
| --- | --- |
|  |  |

## Parameters

```
string theMessage
```

- **theMessage**: a [string](mta://reference/misc/string.md) representing the message entered into the console.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [player](mta://reference/misc/player.md) that entered the message in the console. This can be a player or the server console.

## Example

This example adds the *yo* command into the script. For example, if a player called Bob types "yo likes pie" in console, it will display "* Bob likes pie" in the chatbox.

**NOTE:** this script is for example purposes only. This can be done in a more efficient way with [addCommandHandler](mta://scripting/shared/functions/addcommandhandler.md).

```
function input_Console ( text ) --when a player types in the console
	-- if it's an ingame player,
	if ( getElementType ( source ) == "player" ) then
		--split the command by spaces (ASCII 32) and get the first piece of text
		local command = gettok ( text, 1, 32 )
		--if the first piece of text was "yo",
		if ( command == "yo" ) then
			--get the player's name
			local playerName = getPlayerName ( source )
			-- get the action text by substracting the first three characters ("yo ")
			local actionText = string.sub ( text, 3 )
			-- announce the yo command into the chatbox
			outputChatBox ( "* " .. playerName .. " " .. actionText, getRootElement(), 255, 255, 0 )
		end
	end
end
addEventHandler ( "onConsole", getRootElement(), input_Console ) -- add an event handler for onConsole
```

## See Also

### Client events

- onConsole

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

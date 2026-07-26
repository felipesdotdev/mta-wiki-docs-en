---
doc_id: "mta-wiki:6076"
title: "CancelLatentEvent"
source_title: "CancelLatentEvent"
source_url: "https://wiki.multitheftauto.com/wiki/CancelLatentEvent"
revision_id: 81068
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:11:35.146345+00:00"
---

# CancelLatentEvent

Stops a latent event from completing

## Syntax

Click to collapse [-]
Server

```
bool cancelLatentEvent( player thePlayer, int handle )
```

### Required Arguments

- **thePlayer:** The player who is receiving the event.

- **handle:** A handle previous got from [getLatentEventHandles](mta://scripting/shared/functions/getlatenteventhandles.md).

Click to collapse [-]
Client

```
bool cancelLatentEvent( int handle )
```

### Required Arguments

- **handle:** A handle previous got from [getLatentEventHandles](mta://scripting/shared/functions/getlatenteventhandles.md).

### Returns

Returns a true if the latent event was successfully cancelled, or false if it was not

## Example

Click to collapse [-]
Example 1 - 1/2

```
-- Cancel triggerLatentServerEvent directly after execution.
addCommandHandler("cancelLatentEvent",
function ()
	triggerLatentServerEvent("exampleEvent",3000,false,localPlayer)

	-- Get all your active handles, when you executed the command: /cancelLatentEvent
	local handles = getLatentEventHandles() -- Returns a table.

	local handle = handles[#handles] -- Get the latest handle.

	if cancelLatentEvent(handle) then -- Cancel it!
		outputChatBox("Successfully cancelled!",0,200,0)
	end
end)
```

Click to collapse [-]
Example 1 - 2/2

```
addEvent("exampleEvent",true)
addEventHandler("exampleEvent",root,
function ()
	outputChatBox("Warning! The triggerLatentServerEvent wasn't cancelled!",client,255,0,0) -- warn the user.
end)
```

Click to collapse [-]
Example 2

```
-- Cancel all my triggerLatentClientEvent's.
addCommandHandler("cancelLatentEvents",
function (player)

	-- Get all active handles from the player that executed the command: /cancelLatentEvents
	local handles = getLatentEventHandles (player) -- Returns a table. 
	
	for index=1,#handles do -- Loop through the table.
		local handle = handles[index]
		cancelLatentEvent(player,handle) -- Cancel it!
	end
end)
```

Click to collapse [-]
Example 3

```
-- Cancel all my triggerLatentServerEvent's.
addCommandHandler("cancelLatentEvents",
function ()

	-- Get all your active handles, when you executed the command: /cancelLatentEvents
	local handles = getLatentEventHandles () -- Returns a table. 
	
	for index=1,#handles do -- Loop through the table.
		local handle = handles[index] 
		cancelLatentEvent(handle) -- Cancel it!
	end
end)
```

## See Also

- [addEvent](mta://scripting/shared/functions/addevent.md)

- [addEventHandler](mta://scripting/shared/functions/addeventhandler.md)

- [cancelEvent](mta://scripting/shared/functions/cancelevent.md)

- cancelLatentEvent

- [getEventHandlers](mta://scripting/shared/functions/geteventhandlers.md)

- [getLatentEventHandles](mta://scripting/shared/functions/getlatenteventhandles.md)

- [getLatentEventStatus](mta://scripting/shared/functions/getlatenteventstatus.md)

- [removeEventHandler](mta://scripting/shared/functions/removeeventhandler.md)

- [triggerEvent](mta://scripting/shared/functions/triggerevent.md)

- [wasEventCancelled](mta://scripting/shared/functions/waseventcancelled.md)

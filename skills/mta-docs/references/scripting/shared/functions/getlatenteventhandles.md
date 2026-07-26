---
doc_id: "mta-wiki:6074"
title: "GetLatentEventHandles"
source_title: "GetLatentEventHandles"
source_url: "https://wiki.multitheftauto.com/wiki/GetLatentEventHandles"
revision_id: 81066
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetLatentEventHandles

Gets the currently queued latent events. The last one in the table is always the latest event queued. Each returned handle can be used with [getLatentEventStatus](mta://scripting/shared/functions/getlatenteventstatus.md) or [cancelLatentEvent](mta://scripting/shared/functions/cancellatentevent.md)

## Syntax

Click to collapse [-]
Server

```
table getLatentEventHandles ( player thePlayer )
```

### Required Arguments

- **thePlayer:** The player who is receiving the events.

Click to collapse [-]
Client

```
table getLatentEventHandles ( )
```

### Returns

Returns a table of handles or false if invalid arguments were passed.

## Example

This command is triggering an latent-event to server, and if you write the command again and the trigger still didn't end then you have to wait.

```
-- CLIENT SIDE:

local lastTriggerd = false 

addCommandHandler("trigger",function()
	local triggers = getLatentEventHandles() -- get all latent events
	if triggers[lastTriggerd] then -- you can use (getLatentEventStatus) too!
		outputChatBox("Wait until the trigger ("..lastTriggerd..") ends!",255,0,0)
		return 
	end 
	triggerLatentServerEvent("LatentEventsCheck",20000,resourceRoot,localPlayer)
	lastTriggerd = #getLatentEventHandles() -- set the lastTriggerd with the id for last event triggerd
end)

-- SERVER SIDE:

addEvent("LatentEventsCheck",true)
addEventHandler("LatentEventsCheck",root,function (thePlayer)
	outputChatBox("Latent trigger done from: " .. getPlayerName(thePlayer), root,math.random(255),0,0) 
end)
```

## See Also

- [addEvent](mta://scripting/shared/functions/addevent.md)

- [addEventHandler](mta://scripting/shared/functions/addeventhandler.md)

- [cancelEvent](mta://scripting/shared/functions/cancelevent.md)

- [cancelLatentEvent](mta://scripting/shared/functions/cancellatentevent.md)

- [getEventHandlers](mta://scripting/shared/functions/geteventhandlers.md)

- getLatentEventHandles

- [getLatentEventStatus](mta://scripting/shared/functions/getlatenteventstatus.md)

- [removeEventHandler](mta://scripting/shared/functions/removeeventhandler.md)

- [triggerEvent](mta://scripting/shared/functions/triggerevent.md)

- [wasEventCancelled](mta://scripting/shared/functions/waseventcancelled.md)

---
doc_id: "mta-wiki:2605"
title: "TriggerServerEvent"
source_title: "TriggerServerEvent"
source_url: "https://wiki.multitheftauto.com/wiki/TriggerServerEvent"
revision_id: 79199
language: "en"
categories: ["Client_functions"]
---

# TriggerServerEvent

This function triggers an event previously registered on the server. This is the primary means of passing information between the client and the server. Servers have a similar [triggerClientEvent](mta://scripting/server/functions/triggerclientevent.md) function that can do the reverse. You can treat this function as if it was an asynchronous function call, using [triggerClientEvent](mta://scripting/server/functions/triggerclientevent.md) to pass back any returned information if necessary.

Almost any data types can be passed as expected, including [elements](mta://reference/misc/element.md) and complex nested [tables](mta://reference/misc/table.md). Non-element MTA data types like xmlNodes or resource pointers will not be able to be passed as they do not necessarily have a valid representation on the client. **Elements of the Vector or Matrix classes cannot be passed!**

Events are sent reliably, so the server will receive them, but there may be (but shouldn't be) a significant delay before they are received. You should take this into account when using them.

Keep in mind the bandwidth issues when using events - don't pass a large list of arguments unless you really need to. **It is marginally more efficient to pass one large event than two smaller ones**.

| [[{{{image}}}\|link=\|]] | Important Note: You should use the global variable client server-side instead of passing the localPlayer by parameter or source. Otherwise event faking (passing another player instead of the localPlayer ) would be possible. For more information see: Script security article. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: It is marginally more efficient to pass one large event than two smaller ones. |
| --- | --- |
|  |  |

## Syntax

```
bool triggerServerEvent ( string event, element theElement, [arguments...] )
```

### Required Arguments

- **event:** The name of the event to trigger server-side. You should register this event with [addEvent](mta://scripting/shared/functions/addevent.md) and add at least one event handler using [addEventHandler](mta://scripting/shared/functions/addeventhandler.md).

- **theElement:** The element that is the [source](mta://reference/misc/event-system.md) of the event.

| [[{{{image}}}\|link=\|]] | Important Note: To save server CPU, you should avoid setting theElement to the root element where possible - it should be used as a last resort (rather questionable thing to do, limited to very specific tasks, if any). Using localPlayer is preferred and highly advisable. resourceRoot can also be used as alternative choice, if addEventHandler is bound to root element, or to resourceRoot when there is need to restrict event to single certain resource (although cheater could still trigger it from different resource, by using getResourceRootElement and passing respective resource root element) |
| --- | --- |
|  |  |

### Optional Arguments

- **arguments...:** A list of arguments to trigger with the event. You can pass any lua data type (except functions). You can also pass [elements](mta://reference/misc/element.md).

### Returns

Returns *true* if the event trigger has been sent, *false* if invalid arguments were specified or a client side element was a parameter.

## Example

This example shows how you can send text from client to server.

Click to collapse [-]
Client

```
function sendMessageToServer()
	local messageToSend = "Hello, world!" -- this string would be passed to server

	triggerServerEvent("onServerSendMessage", localPlayer, messageToSend) -- refer to the note on wiki page (under theElement), for understanding which element you should use as 2nd argument
end
addCommandHandler("message", sendMessageToServer)
```

Click to collapse [-]
Server

```
function onServerSendMessage(sentMessage)
	if (not client) then -- 'client' points to the player who triggered the event, and should be used as security measure (in order to prevent player faking)
		return false -- if this variable doesn't exists at the moment (for unknown reason, or it was the server who triggered this event), stop code execution
	end

	local matchingSource = (source == client) -- check whether source element (2nd argument in triggerServerEvent) passed from client was the exact same player

	if (not matchingSource) then -- apparently it wasn't
		return false -- so do not process this event
	end

	local dataType = type(sentMessage) -- check type of data coming from client
	local dataString = (dataType == "string") -- check whether it's string

	if (not dataString) then -- if it isn't string
		return false -- stop our code here
	end

	local minStringLength = 1 -- min allowed length of string
	local maxStringLength = 64 -- max allowed length of string
	local stringLength = utf8.len(sentMessage) -- get string length
	local allowedStringLength = (stringLength >= minStringLength and stringLength <= maxStringLength) -- verify whether length is allowed

	if (not allowedStringLength) then -- if string length was exceeded
		return false -- tell server to stop here
	end

	local playerName = getPlayerName(client) -- get name of player who sent message
	local chatMessage = playerName.." sent message from client: "..sentMessage

	outputChatBox(chatMessage, root, 255, 255, 255, false) -- output text sent from client-side for everyone on server

	-- useful utility for checking event data: https://wiki.multitheftauto.com/wiki/Script_security
end
addEvent("onServerSendMessage", true) -- 2nd argument should be set to true, in order to be triggered from counter side (in this case client-side)
addEventHandler("onServerSendMessage", root, onServerSendMessage)
```

When the command **message** is executed (by typing it in the player's console or in chat: **/message**), **sendMessageToServer** function is called. This triggers the server-side event *onServerSendMessage* and passes [string](mta://reference/misc/string.md) **"Hello, world!"**. This event is then handled by function on server-side, which process security measures, and if everything is alright - outputs text to chat.

This example shows how you can send table with numbers from client to server.

Click to collapse [-]
Client

```
function sendTableToServer()
	local tableToSent = {1, 2, 3} -- this table would be passed to server

	triggerServerEvent("onServerSendTable", resourceRoot, tableToSent) -- refer to the note on wiki page (under theElement), for understanding which element you should use as 2nd argument
end
addCommandHandler("table", sendTableToServer)
```

Click to collapse [-]
Server

```
function onServerSendTable(sentTable)
	if (not client) then -- 'client' points to the player who triggered the event, and should be used as security measure (in order to prevent player faking)
		return false -- if this variable doesn't exists at the moment (for unknown reason, or it was the server who triggered this event), stop code execution
	end

	local matchingSource = (source == resourceRoot) -- check whether source element (2nd argument in triggerServerEvent) passed from client was resourceRoot

	if (not matchingSource) then -- apparently it wasn't
		return false -- so do not process this event
	end

	local dataType = type(sentTable) -- check type of data coming from client
	local dataTable = (dataType == "table") -- check whether it's table

	if (not dataTable) then -- if it isn't table
		return false -- stop our code here
	end

	local minTableLength = 1 -- min allowed length of table
	local maxTableLength = 3 -- max allowed length of table
	local tableLength = (#sentTable) -- get table length
	local matchingTableLength = (tableLength >= minTableLength and tableLength <= maxTableLength) -- verify whether length is allowed

	if (not matchingTableLength) then -- if table length was exceeded
		return false -- tell server to stop here
	end

	local numbersOnly = true -- variable which will hold whether numbers only were in the table

	for _, numberValue in pairs(sentTable) do -- iterate through table 
		local valueType = type(numberValue) -- check type of each data
		local numberType = (valueType == "number") -- check whether it's a number

		if (not numberType) then -- it isn't a number
			numbersOnly = false -- since at least one of data inside isn't number, set it to false
			break -- break the loop, no need to check further
		end
	end

	if (not numbersOnly) then -- it isn't numbers only table
		return false -- stop code execution
	end

	local playerName = getPlayerName(client) -- get name of player who sent message
	local sentNumbers = table.concat(sentTable, ", ") -- convert our table into list of numbers separated by comma
	local chatMessage = playerName.." sent table with numbers from client: "..sentNumbers

	outputChatBox(chatMessage, root, 255, 255, 255, false) -- output numbers sent from client-side for everyone on server

	-- useful utility for checking event data: https://wiki.multitheftauto.com/wiki/Script_security
end
addEvent("onServerSendTable", true) -- 2nd argument should be set to true, in order to be triggered from counter side (in this case client-side)
addEventHandler("onServerSendTable", resourceRoot, onServerSendTable)
```

When the command **table** is executed (by typing it in the player's console or in chat: **/table**), **sendTableToServer** function is called. This triggers the server-side event *onServerSendTable* and passes [table](mta://reference/misc/table.md) **{1, 2, 3}**. This event is then handled by function on server-side, which process security measures, and if everything is alright - outputs numbers to chat.

## See Also

- [triggerLatentServerEvent](mta://scripting/client/functions/triggerlatentserverevent.md)

- triggerServerEvent
  

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

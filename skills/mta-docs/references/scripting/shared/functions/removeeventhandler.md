---
doc_id: "mta-wiki:1887"
title: "RemoveEventHandler"
source_title: "RemoveEventHandler"
source_url: "https://wiki.multitheftauto.com/wiki/RemoveEventHandler"
revision_id: 23983
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# RemoveEventHandler

This functions removes a handler function from an [event](https://wiki.multitheftauto.com/index.php?search=event), so that the function is not called anymore when the event is triggered. See [event system](mta://reference/misc/event-system.md) for more information on how the event system works.

## Syntax

```
bool removeEventHandler ( string eventName, element attachedTo, function functionVar )
```

### Required Arguments

- **eventName:** The name of the [event](https://wiki.multitheftauto.com/index.php?search=event) you want to detach the handler function from.

- **attachedTo:** The [element](mta://reference/misc/element.md) the handler was attached to.

- **functionVar:** The handler function that was attached.

### Returns

Returns *true* if the event handler was removed successfully. Returns *false* if the specified event handler could not be found or invalid parameters were passed.

## Example

Click to collapse [-]
Client

This example shows how to toggle a message on/off a screen with a command.

```
function drawText() -- A function to draw the text we want
	dxDrawText(text, 10,100) -- creates a dx text 10 pixels from left, 100 from top of the screen
end
function doText(command, ...)
	if command == "starttext" then -- if player wrote /starttext
		text = table.concat({...}," ") -- then we retrieve the text
		addEventHandler("onClientRender", getRootElement(), drawText) 		-- and since addEventHandler and removeEventHandler's syntax is the same, we just define the function we use later
	elseif command == "stoptext" then
		removeEventHandler("onClientRender", getRootElement(), drawText) 	-- this time we use removeEventHandler
	end
end
addCommandHandler("starttext", doText) -- add two command handlers to doText function
addCommandHandler("stoptext", doText)
```

## See Also

- [addEvent](mta://scripting/shared/functions/addevent.md)

- [addEventHandler](mta://scripting/shared/functions/addeventhandler.md)

- [cancelEvent](mta://scripting/shared/functions/cancelevent.md)

- [cancelLatentEvent](mta://scripting/shared/functions/cancellatentevent.md)

- [getEventHandlers](mta://scripting/shared/functions/geteventhandlers.md)

- [getLatentEventHandles](mta://scripting/shared/functions/getlatenteventhandles.md)

- [getLatentEventStatus](mta://scripting/shared/functions/getlatenteventstatus.md)

- removeEventHandler

- [triggerEvent](mta://scripting/shared/functions/triggerevent.md)

- [wasEventCancelled](mta://scripting/shared/functions/waseventcancelled.md)

---
doc_id: "mta-wiki:6072"
title: "TriggerLatentServerEvent"
source_title: "TriggerLatentServerEvent"
source_url: "https://wiki.multitheftauto.com/wiki/TriggerLatentServerEvent"
revision_id: 82673
language: "en"
categories: ["Client_functions"]
---

# TriggerLatentServerEvent

This function is the same as [triggerServerEvent](mta://scripting/client/functions/triggerserverevent.md) except the transmission rate of the data contained in the arguments can be limited and other network traffic is not blocked while the data is being transferred.

## Syntax

```
bool triggerLatentServerEvent ( string event, [int bandwidth=5000, bool persist=false,] element theElement, [arguments...] )
```

### Required Arguments

- **event:** The name of the event to trigger server-side. You should register this event with [addEvent](mta://scripting/shared/functions/addevent.md) and add at least one event handler using [addEventHandler](mta://scripting/shared/functions/addeventhandler.md).

- **theElement:** The element that is the [source](mta://reference/misc/event-system.md) of the event. This could be another player, or if this isn't relevant, use the root element.

### Optional Arguments

- **bandwidth:** The bytes per second rate to send the data contained in the arguments.

- **persist:** A bool indicating whether the transmission should be allowed to continue even after the resource that triggered it has since stopped.

- **arguments...:** A list of arguments to trigger with the event. You can pass any Lua data type (except functions). You can also pass [elements](mta://reference/misc/element.md). The total amount of data should not exceed 100MB.

### Returns

Returns *true* if the event trigger has been sent, *false* if invalid arguments were specified.

## Example

Click to collapse [-]
Client

```
if fileExists("text.txt") then
	file = fileOpen("test.txt")						--Open a file (you can create it yourself).
	local data = fileRead(file,100*1024*1024)				--Max 100 MB
	fileClose(file)								--Close File
	triggerLatentServerEvent("onReadFile",5000,false,root,data)	--trigger
end
```

Click to collapse [-]
Server

```
addEvent("onReadFile",true)
addEventHandler("onReadFile",root,function(data)
	local file = fileCreate("text.txt")					--Save "data" into "text.txt"
	fileWrite(file,data)
	fileClose(file)
end)
```

## See Also

- triggerLatentServerEvent

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

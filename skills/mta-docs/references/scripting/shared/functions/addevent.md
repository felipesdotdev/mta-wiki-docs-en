---
doc_id: "mta-wiki:1543"
title: "AddEvent"
source_title: "AddEvent"
source_url: "https://wiki.multitheftauto.com/wiki/AddEvent"
revision_id: 67675
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# AddEvent

This function allows you to register a custom [event](https://wiki.multitheftauto.com/index.php?search=event). Custom events function exactly like the built-in events. See [event system](mta://reference/misc/event-system.md) for more information on the event system.

## Syntax

```
bool addEvent ( string eventName [, bool allowRemoteTrigger = false ] )
```

### Required Arguments

- **eventName:** The name of the event you wish to create.

### Optional Arguments

- **allowRemoteTrigger:** A boolean specifying whether this event can be called remotely using [triggerClientEvent](mta://scripting/server/functions/triggerclientevent.md) / [triggerServerEvent](mta://scripting/client/functions/triggerserverevent.md) or not.

### Returns

Returns *true* if the event was added successfully, *false* if the event was already added.

## Example

This example will define a new event called *onSpecialEvent*.

```
-- Add a new event called onSpecialEvent
addEvent ( "onSpecialEvent", true )

-- Define our handler function, that takes a "text" parameter and outputs it to the chatbox
function specialEventHandler ( text )
	outputChatBox ( text )
end

-- Add it as a handler for our event
addEventHandler ( "onSpecialEvent", root, specialEventHandler )
```

You can then trigger this event later on using:

```
triggerEvent ( "onSpecialEvent", root, "test" )
```

This will cause the handler to be triggered, so "test" will be output to the chatbox.

## See Also

- addEvent

- [addEventHandler](mta://scripting/shared/functions/addeventhandler.md)

- [cancelEvent](mta://scripting/shared/functions/cancelevent.md)

- [cancelLatentEvent](mta://scripting/shared/functions/cancellatentevent.md)

- [getEventHandlers](mta://scripting/shared/functions/geteventhandlers.md)

- [getLatentEventHandles](mta://scripting/shared/functions/getlatenteventhandles.md)

- [getLatentEventStatus](mta://scripting/shared/functions/getlatenteventstatus.md)

- [removeEventHandler](mta://scripting/shared/functions/removeeventhandler.md)

- [triggerEvent](mta://scripting/shared/functions/triggerevent.md)

- [wasEventCancelled](mta://scripting/shared/functions/waseventcancelled.md)

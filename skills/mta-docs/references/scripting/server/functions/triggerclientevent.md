---
doc_id: "mta-wiki:2398"
title: "TriggerClientEvent"
source_title: "TriggerClientEvent"
source_url: "https://wiki.multitheftauto.com/wiki/TriggerClientEvent"
revision_id: 82147
language: "en"
categories: ["Server_functions", "Utility_templates"]
---

# TriggerClientEvent

This function triggers an event previously registered on a client. This is the primary means of passing information between the server and the client. Clients have a similar [triggerServerEvent](mta://scripting/client/functions/triggerserverevent.md) function that can do the reverse. You can treat this function as if it was an asynchronous function call, using [triggerServerEvent](mta://scripting/client/functions/triggerserverevent.md) to pass back any returned information if necessary.

Almost any data types can be passed as expected, including [elements](mta://reference/misc/element.md) and complex nested [tables](mta://reference/misc/table.md). Non-element MTA data types like xmlNodes or resource pointers will not be able to be passed as they do not necessarily have a valid representation on the client.

Events are sent reliably, so clients will receive them, but there may be (but shouldn't be) a significant delay before they are received. You should take this into account when using them.

Keep in mind the bandwidth issues when using events - don't pass a large list of arguments unless you really need to. **It is marginally more efficient to pass one large event than two smaller ones**.

| [[{{{image}}}\|link=\|]] | Important Note: Non-element MTA data types like xmlNodes or resource pointers will not be able to be passed as they do not necessarily have a valid representation on the client. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: It is marginally more efficient to pass one large event than two smaller ones. |
| --- | --- |
|  |  |

## Syntax

```
bool triggerClientEvent ( [ table/element sendTo = getRootElement(), ] string name, element sourceElement [, arguments... ] )
```

### Required Arguments

- **name:** The name of the event to trigger client side. You should register this event with [addEvent](mta://scripting/shared/functions/addevent.md) and add at least one event handler using [addEventHandler](mta://scripting/shared/functions/addeventhandler.md).

- **sourceElement:** The element that is the [source](mta://reference/misc/event-system.md) of the event.

| [[{{{image}}}\|link=\|]] | Important Note: To save client CPU, you should avoid setting theElement to the root element where possible - it should be used as a last resort (rather questionable thing to do, limited to very specific tasks, if any). Using target element ( player who should receive event, if expected to be delivered to particular one) is preferred and highly advisable. resourceRoot can also be used as alternative choice, if addEventHandler is bound to root element, or to resourceRoot when there is need to restrict event to single certain resource. |
| --- | --- |
|  |  |

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **sendTo:** The event will be sent to all [players](https://wiki.multitheftauto.com/index.php?search=players) that are children of the specified element. By default this is the root element, and hence the event is sent to all players. If you specify a single player it will just be sent to that player. This argument can also be a table of player elements.

- **arguments...:** A list of arguments to trigger with the event. You can pass any lua data type (except functions). You can also pass [elements](mta://reference/misc/element.md).

### Returns

Returns *true* if the event trigger has been sent, *false* if invalid arguments were specified.

## Examples

This example shows how you can pass a simple "Hello World" message from the server to the all the clients using an event.

Click to collapse [-]
Client

```
function greetingHandler ( message )
    outputChatBox ( "The server says: " .. message )
end
addEvent( "onGreeting", true )
addEventHandler( "onGreeting", localPlayer, greetingHandler )
```

When the command "greet" is executed (by typing it in the server console or the player's console), the server's *greetingCommand* function is called. This triggers the client side event *onGreeting* with the string *"Hello World!"*. This event is then handled by the *greetingHandler* function client side which then displays the message.

Click to collapse [-]
Server

```
function greetingCommand ( playerSource, commandName )
    triggerClientEvent ( playerSource, "onGreeting", playerSource, "Hello World!" )
end
addCommandHandler ( "greet", greetingCommand )
```

This example shows how you can pass a simple "Hello World" message from the server to **a single** client using an event.

Click to collapse [-]
Client

```
function greetingHandler ( message )
    outputChatBox ( "The server says: " .. message )
end
addEvent( "onGreeting", true )
addEventHandler( "onGreeting", localPlayer, greetingHandler )
```

This works like the first example except an extra *thePlayer* argument is specified for triggerClientEvent.

Click to collapse [-]
Server

```
function greetingCommandOne ( playerSource, commandName, playerName )
    if playerName then
        local thePlayer = getPlayerFromName ( playerName )
        if thePlayer then
            triggerClientEvent ( thePlayer, "onGreeting", thePlayer, "Hello World!" )
        else
            -- invalid player name specified
        end
    else
        -- No player name specified
    end 
end
addCommandHandler ( "greet_one", greetingCommandOne )
```

This example uses resourceRoot to avoid being called by resources other than the same one that was created. (it can still be circumvented with [getResourceRootElement](mta://scripting/shared/functions/getresourcerootelement.md) but it makes it more difficult for cheating players).

Click to collapse [-]
Client

```
function nameFunction(message)
    if source == resourceRoot then
        outputChatBox(message)
    end
end
addEvent("toClientSide", true )
addEventHandler("toClientSide", resourceRoot, nameFunction)
```

Click to collapse [-]
Server

```
function commandFunction(source)
    triggerClientEvent(source, "toClientSide", resourceRoot, "Hello World!")
end
addCommandHandler("cool", commandFunction)
```

## Changelog

| Version | Description |
| --- | --- |

| 1.3.0-9.04570 | Added option to use a list of player elements for the 'sendTo' argument |
| --- | --- |

## See Also

- [getCancelReason](mta://scripting/server/functions/getcancelreason.md)

- triggerClientEvent

- [triggerLatentClientEvent](mta://scripting/server/functions/triggerlatentclientevent.md)
  

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

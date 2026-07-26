---
doc_id: "mta-wiki:6075"
title: "GetLatentEventStatus"
source_title: "GetLatentEventStatus"
source_url: "https://wiki.multitheftauto.com/wiki/GetLatentEventStatus"
revision_id: 81067
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetLatentEventStatus

Gets the status of one queued latent event.

## Syntax

Click to collapse [-]
Server

```
table getLatentEventStatus( player thePlayer, int handle )
```

### Required Arguments

- **thePlayer:** The player who is receiving the event.

- **handle:** A handle previous got from [getLatentEventHandles](mta://scripting/shared/functions/getlatenteventhandles.md).

Click to collapse [-]
Client

```
table getLatentEventStatus( int handle )
```

### Required Arguments

- **handle:** A handle previous got from [getLatentEventHandles](mta://scripting/shared/functions/getlatenteventhandles.md).

### Returns

Returns a table with the following info or false if invalid arguments were passed:

- **tickStart:** A number estimating how many ticks until the data transfer starts (Negative means the transfer has already started)

- **tickEnd:** A number estimating how many ticks until the data transfer completes

- **totalSize:** A number representing how many bytes in total this transfer will transfer

- **percentComplete:** A number between 0-100 saying how much is done

## Example

Click to collapse [-]
Client

The example starts a latent event and outputs the status of the transfer to the client console

```
function beginTransfer()
    triggerLatentServerEvent("blah", resourceRoot, myVeryLongString)    -- Start latent event
    myHandle = getLatentEventHandles()[#getLatentEventHandles()]        -- Get last latent event handle
    myTimer = setTimer( updateStatus, 1000, 0 )                         -- Output status once a second
end

function updateStatus()
    local status = getLatentEventStatus(myHandle)   -- Get latent event status
    if not status then
        killTimer(myTimer)                          -- getLatentEventStatus returns false when the handle is no longer valid
    else
        outputConsole( "Transfer status:"
            .. " tickStart:" .. tostring(status.tickStart)
            .. " tickEnd:" .. tostring(status.tickEnd)
            .. " totalSize:" .. tostring(status.totalSize)
            .. " percentComplete:" .. tostring(status.percentComplete)
            )
    end
end
```

## See Also

- [addEvent](mta://scripting/shared/functions/addevent.md)

- [addEventHandler](mta://scripting/shared/functions/addeventhandler.md)

- [cancelEvent](mta://scripting/shared/functions/cancelevent.md)

- [cancelLatentEvent](mta://scripting/shared/functions/cancellatentevent.md)

- [getEventHandlers](mta://scripting/shared/functions/geteventhandlers.md)

- [getLatentEventHandles](mta://scripting/shared/functions/getlatenteventhandles.md)

- getLatentEventStatus

- [removeEventHandler](mta://scripting/shared/functions/removeeventhandler.md)

- [triggerEvent](mta://scripting/shared/functions/triggerevent.md)

- [wasEventCancelled](mta://scripting/shared/functions/waseventcancelled.md)

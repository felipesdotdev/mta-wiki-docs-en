---
doc_id: "mta-wiki:4336"
title: "GetCancelReason"
source_title: "GetCancelReason"
source_url: "https://wiki.multitheftauto.com/wiki/GetCancelReason"
revision_id: 80366
language: "en"
categories: ["Server_functions"]
---

# GetCancelReason

Gets the reason for cancelling an event.

## Syntax

```
string getCancelReason ( )
```

### Required Arguments

*None*

### Returns

Returns the reason that was given with [cancelEvent](mta://scripting/shared/functions/cancelevent.md)

## Example

This example cancels when a hunterPlayer tries to enter a vehicle and outputs to the world what the player tried to do.

```
-- call 'stopVehicleEntry' whenever hunterPlayer is about to enter a vehicle:
function stopVehicleEntry ( theplayer, seat, jacked )
   cancelEvent (true, "You can't enter a vehicle during war.") -- stop the event from occuring and tell the player the reason.
   outputConsole("We told "..getPlayerName(theplayer).." : "..getCancelReason()) --Now tell everyone what the player tried to do
end
addEventHandler ( "onVehicleStartEnter", huntedPlayer, stopVehicleEntry )
```

## See Also

- getCancelReason

- [triggerClientEvent](mta://scripting/server/functions/triggerclientevent.md)

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

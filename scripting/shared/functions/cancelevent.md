---
doc_id: "mta-wiki:1849"
title: "CancelEvent"
source_title: "CancelEvent"
source_url: "https://wiki.multitheftauto.com/wiki/CancelEvent"
revision_id: 75035
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
generated_at: "2026-07-26T16:10:28.696683+00:00"
---

# CancelEvent

This function is used to stop the automatic internal handling of events, for example this can be used to prevent an item being given to a player when they walk over a pickup, by canceling the [onPickupUse](mta://scripting/server/events/onpickupuse.md) event.

cancelEvent does not have an effect on all events, see the individual event's pages for information on what happens when the event is canceled. cancelEvent does not stop further event handlers from being called, as the order of event handlers being called is undefined in many cases. Instead, you can see if the currently active event has been cancelled using [wasEventCancelled](mta://scripting/shared/functions/waseventcancelled.md).

The use of cancelEvent outside of an event handler has no effect.

If you implement your own custom events and want to handle them being cancelled, you should call [wasEventCancelled](mta://scripting/shared/functions/waseventcancelled.md) to check after your call to [triggerEvent](mta://scripting/shared/functions/triggerevent.md).

## Syntax

Click to collapse [-]
Server

```
bool cancelEvent ( [ bool cancel = true, string reason = "" ] )
```

Click to collapse [-]
Client

```
bool cancelEvent ()
```

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **cancel:** True to cancel, false to uncancel.

- **reason:** The reason for cancelling the event.

### Returns

Always returns *true*.

## Example

Click to collapse [-]
Example 1 - Server

This example stops the player from entering a vehicle.

```
function onVehicleStartEnter()
   cancelEvent()
end
addEventHandler("onVehicleStartEnter", root, onVehicleStartEnter)
```

Click to collapse [-]
Example 2 - Client

This example prevents any damage to a player clientside by making cancelEvent an event handler for the [onClientPlayerDamage](mta://scripting/client/events/onclientplayerdamage.md) event.

```
function onClientPlayerDamage()
	cancelEvent()
end
addEventHandler("onClientPlayerDamage", root, onClientPlayerDamage)
```

## See Also

- [addEvent](mta://scripting/shared/functions/addevent.md)

- [addEventHandler](mta://scripting/shared/functions/addeventhandler.md)

- cancelEvent

- [cancelLatentEvent](mta://scripting/shared/functions/cancellatentevent.md)

- [getEventHandlers](mta://scripting/shared/functions/geteventhandlers.md)

- [getLatentEventHandles](mta://scripting/shared/functions/getlatenteventhandles.md)

- [getLatentEventStatus](mta://scripting/shared/functions/getlatenteventstatus.md)

- [removeEventHandler](mta://scripting/shared/functions/removeeventhandler.md)

- [triggerEvent](mta://scripting/shared/functions/triggerevent.md)

- [wasEventCancelled](mta://scripting/shared/functions/waseventcancelled.md)

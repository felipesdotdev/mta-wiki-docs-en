---
doc_id: "mta-wiki:12579"
title: "OnPedVehicleEnter"
source_title: "OnPedVehicleEnter"
source_url: "https://wiki.multitheftauto.com/wiki/OnPedVehicleEnter"
revision_id: 81266
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:24.253438+00:00"
---

# OnPedVehicleEnter

This event is triggered when a [ped](mta://reference/misc/ped.md) enters a [vehicle](mta://reference/misc/vehicle.md).

## Parameters

```
vehicle theVehicle, int seat, ped jacked
```

- **theVehicle**: A [vehicle](mta://reference/misc/vehicle.md) element representing the [vehicle](mta://reference/misc/vehicle.md) that was entered.

- **seat**: An [int](mta://reference/misc/int.md) representing the seat in which the [ped](mta://reference/misc/ped.md) is entering.

- **jacked**: A [player](mta://reference/misc/player.md) or [ped](mta://reference/misc/ped.md) element representing who has been jacked.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [ped](mta://reference/misc/ped.md) that entered the [vehicle](mta://reference/misc/vehicle.md).

## Example

Sending a message to every [player](mta://reference/misc/player.md) when [ped](mta://reference/misc/ped.md) has entered to a [vehicle](mta://reference/misc/vehicle.md):

```
function sendMessage (theVehicle, seat)
   local vehicleName = getVehicleName (theVehicle) -- Get name of the vehicle
   if seat == 0 then -- if the ped is a driver
      outputChatBox ("Ped is now a driver of "..vehicleName, root)
   else -- if not
      outputChatBox ("Ped has entered to "..vehicleName, root)
   end
end

addEventHandler ("onPedVehicleEnter", root, sendMessage)
```

## See Also

### Ped events

- [onPedDamage](mta://scripting/server/events/onpeddamage.md)

- onPedVehicleEnter

- [onPedVehicleExit](mta://scripting/server/events/onpedvehicleexit.md)

- [onPedWasted](mta://scripting/server/events/onpedwasted.md)

- [onPedWeaponSwitch](mta://scripting/server/events/onpedweaponswitch.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22909](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22909))

- [onPedWeaponReload](mta://scripting/server/events/onpedweaponreload.md)

### Event functions

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

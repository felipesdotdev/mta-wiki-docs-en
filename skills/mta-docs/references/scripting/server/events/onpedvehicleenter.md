---
doc_id: "mta-wiki:12579"
title: "OnPedVehicleEnter"
source_title: "OnPedVehicleEnter"
source_url: "https://wiki.multitheftauto.com/wiki/OnPedVehicleEnter"
revision_id: 81266
language: "en"
categories: ["Server_Events"]
---

# OnPedVehicleEnter

This event is triggered when a [ped](https://wiki.multitheftauto.com/index.php?search=ped) enters a [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle).

## Parameters

```
vehicle theVehicle, int seat, ped jacked
```

- **theVehicle**: A [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle) element representing the [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle) that was entered.

- **seat**: An [int](mta://reference/misc/int.md) representing the seat in which the [ped](https://wiki.multitheftauto.com/index.php?search=ped) is entering.

- **jacked**: A [player](https://wiki.multitheftauto.com/index.php?search=player) or [ped](https://wiki.multitheftauto.com/index.php?search=ped) element representing who has been jacked.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [ped](https://wiki.multitheftauto.com/index.php?search=ped) that entered the [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle).

## Example

Sending a message to every [player](https://wiki.multitheftauto.com/index.php?search=player) when [ped](https://wiki.multitheftauto.com/index.php?search=ped) has entered to a [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle):

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

---
doc_id: "mta-wiki:12580"
title: "OnPedVehicleExit"
source_title: "OnPedVehicleExit"
source_url: "https://wiki.multitheftauto.com/wiki/OnPedVehicleExit"
revision_id: 81267
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:24.269471+00:00"
---

# OnPedVehicleExit

This event is triggered when a [ped](mta://reference/misc/ped.md) leaves a [vehicle](mta://reference/misc/vehicle.md).

## Parameters

```
vehicle theVehicle, int seat, ped jacker, bool forcedByScript
```

- **theVehicle**: A [vehicle](mta://reference/misc/vehicle.md) element representing the [vehicle](mta://reference/misc/vehicle.md) in which the [ped](mta://reference/misc/ped.md) exited from.

- **seat**: An [int](mta://reference/misc/int.md) representing the seat in which the [ped](mta://reference/misc/ped.md) was before exiting.

- **jacker**: A [player](mta://reference/misc/player.md) or [ped](mta://reference/misc/ped.md) element representing who jacked the driver.

- **forcedByScript:** A [boolean](mta://reference/misc/boolean.md) representing whether the exit was forced using [removePedFromVehicle](mta://scripting/shared/functions/removepedfromvehicle.md) or by the [ped](mta://reference/misc/ped.md).

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [ped](mta://reference/misc/ped.md) that left the [vehicle](mta://reference/misc/vehicle.md).

## Example

Destroy the [vehicle](mta://reference/misc/vehicle.md) when [ped](mta://reference/misc/ped.md) has been jacked and kick the jacker if exists:

```
function destroyVehicle (theVehicle, seat, jacker, forcedByScript)
   if seat == 0 then -- If ped was a driver
      if forcedByScript then
         destroyElement (theVehicle) -- If the exit was forced using removePedFromVehicle then destroy the vehicle
      elseif jacker then
         kickPlayer (jacker)
         destroyElement (theVehicle)
      end
   end
end

addEventHandler ("onPedVehicleExit", root, destroyVehicle)
```

## See Also

### Ped events

- [onPedDamage](mta://scripting/server/events/onpeddamage.md)

- [onPedVehicleEnter](mta://scripting/server/events/onpedvehicleenter.md)

- onPedVehicleExit

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

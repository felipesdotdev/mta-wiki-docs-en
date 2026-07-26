---
doc_id: "mta-wiki:2263"
title: "OnVehicleExit"
source_title: "OnVehicleExit"
source_url: "https://wiki.multitheftauto.com/wiki/OnVehicleExit"
revision_id: 82077
language: "en"
categories: ["Server_Events", "Changes_in_1.5.3"]
generated_at: "2026-07-26T16:16:26.508835+00:00"
---

# OnVehicleExit

This event is triggered when a player or ped leaves a vehicle.

## Parameters

```
ped thePed, int seat, ped jacker, bool forcedByScript
```

- **thePed**: a [player](mta://reference/misc/player.md) or [ped](mta://reference/misc/ped.md) element who exited the [vehicle](mta://reference/misc/vehicle.md).

- **seat**: an [int](mta://reference/misc/int.md) representing the seat in which the ped exited from.

- **jacker**: a [player](mta://reference/misc/player.md) or [ped](mta://reference/misc/ped.md) element who jacked the driver.

- **forcedByScript:** a [boolean](mta://reference/misc/boolean.md) representing whether the exit was forced using [removePedFromVehicle](mta://scripting/shared/functions/removepedfromvehicle.md) or by the ped/player.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [vehicle](mta://reference/misc/vehicle.md) that was exited.

## Examples

This example adds a 'moto' helmet to a player when he gets on a nrg bike, and removes it when he gets off.

```
function addHelmetOnEnter ( thePlayer, seat, jacked )
    if ( getElementModel ( source ) == 522 ) then -- if its a nrg
        addPedClothes ( thePlayer, "moto", "moto", 16 ) -- add the helmet
    end
end
addEventHandler ( "onVehicleEnter", getRootElement(), addHelmetOnEnter )

function removeHelmetOnExit ( thePlayer, seat, jacked )
    if ( getElementModel ( source ) == 522 ) then -- if its a nrg
        removePedClothes ( thePlayer, 16 ) -- remove the helmet
    end
end
addEventHandler ( "onVehicleExit", getRootElement(), removeHelmetOnExit )
```

This example will turn off a vehicle's engine when the driver gets out of the car.

```
addEventHandler ( "onVehicleExit", getRootElement(), function(theVehicle, leftSeat, jackerPlayer)
    if leftSeat == 0 and not jackerPlayer then
       setVehicleEngineState( theVehicle, false)
    end
end)
```

## Changelog

| Version | Description |
| --- | --- |

| 1.5.3-9.11247 | Added forcedByScript argument |
| --- | --- |

## See Also

### Vehicle events

- [onTrailerAttach](mta://scripting/server/events/ontrailerattach.md)

- [onTrailerDetach](mta://scripting/server/events/ontrailerdetach.md)

- [onVehicleDamage](mta://scripting/server/events/onvehicledamage.md)

- [onVehicleEnter](mta://scripting/server/events/onvehicleenter.md)

- onVehicleExit

- [onVehicleExplode](mta://scripting/server/events/onvehicleexplode.md)

- [onVehicleRespawn](mta://scripting/server/events/onvehiclerespawn.md)

- [onVehicleStartEnter](mta://scripting/server/events/onvehiclestartenter.md)

- [onVehicleStartExit](mta://scripting/server/events/onvehiclestartexit.md)

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

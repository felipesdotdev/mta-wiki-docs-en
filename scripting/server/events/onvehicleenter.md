---
doc_id: "mta-wiki:2262"
title: "OnVehicleEnter"
source_title: "OnVehicleEnter"
source_url: "https://wiki.multitheftauto.com/wiki/OnVehicleEnter"
revision_id: 67857
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:26.482481+00:00"
---

# OnVehicleEnter

This event is triggered when a player or ped enters a vehicle.

## Parameters

```
ped thePed, int seat, player jacked
```

- **thePed**: a [player](mta://reference/misc/player.md) or [ped](mta://reference/misc/ped.md) element who is entering the [vehicle](mta://reference/misc/vehicle.md).

- **seat**: an [int](mta://reference/misc/int.md) representing the seat in which the ped is entering. Seat 0 is the driver's seat.

- **jacked**: a [player](mta://reference/misc/player.md) or [ped](mta://reference/misc/ped.md) element representing who has been jacked.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [vehicle](mta://reference/misc/vehicle.md) that was entered.

## Example

**Example 1:** This example forces a player out of a police vehicle if he is not a policeman.

```
policeVehicles = { [598]=true, [596]=true, [597]=true, [599]=true }
policeSkins = { [280]=true, [281]=true, [282]=true, [283]=true, [284]=true, [285]=true, [286]=true }

function enterVehicle ( thePlayer, seat, jacked ) -- when a player enters a vehicle
    if ( policeVehicles[getElementModel ( source )] ) and ( not policeSkins[getElementModel ( thePlayer )] ) then -- if the vehicle is one of 4 police cars, and the skin is not a police skin
        removePedFromVehicle ( thePlayer ) -- force the player out of the vehicle
        outputChatBox ( "Only policeman can enter police cars!", thePlayer ) -- and tell the player why
    end
end
addEventHandler ( "onVehicleEnter", getRootElement(), enterVehicle ) -- add an event handler for onVehicleEnter
```

**Example 2:** This example adds a 'moto' helmet to a player when he gets on a nrg bike, and removes it when he gets off (only works with players using CJ skin).

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

## See Also

### Vehicle events

- [onTrailerAttach](mta://scripting/server/events/ontrailerattach.md)

- [onTrailerDetach](mta://scripting/server/events/ontrailerdetach.md)

- [onVehicleDamage](mta://scripting/server/events/onvehicledamage.md)

- onVehicleEnter

- [onVehicleExit](mta://scripting/server/events/onvehicleexit.md)

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

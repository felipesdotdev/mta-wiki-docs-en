---
doc_id: "mta-wiki:1840"
title: "OnVehicleStartEnter"
source_title: "OnVehicleStartEnter"
source_url: "https://wiki.multitheftauto.com/wiki/OnVehicleStartEnter"
revision_id: 67859
language: "en"
categories: ["Server_Events", "Changes_in_1.0"]
generated_at: "2026-07-26T16:16:26.596035+00:00"
---

# OnVehicleStartEnter

This event is triggered when a player or ped starts to enter a vehicle. This event can be used to cancel entry, if necessary.

## Parameters

```
ped enteringPed, int seat, ped jacked, int door
```

- **enteringPed**: a [player](mta://reference/misc/player.md) or [ped](mta://reference/misc/ped.md) element who is starting to enter a vehicle.

- **seat**: an [int](mta://reference/misc/int.md) representing the seat in which the ped is entering.

- **jacked**: a [player](mta://reference/misc/player.md) or [ped](mta://reference/misc/ped.md) element representing who is going to be jacked.

- **door**: an [int](mta://reference/misc/int.md) of which door is being used (0-3). 0 is driver side door, 1 is front passenger, 2 is back left, 3 is back right.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [vehicle](mta://reference/misc/vehicle.md) in which a ped began to enter.

### Canceling

If this event is [canceled](mta://reference/misc/event-system.md), the ped will not enter the vehicle.

## Example

This example blocks a player out of a police vehicle if he is not a policeman.

```
policeVehicles = { [598]=true,[596]=true,[597]=true,[599]=true }
policeSkins = { [280]=true,[281]=true,[282]=true,[283]=true,[284]=true,[285]=true,[286]=true }

function enterVehicle ( player, seat, jacked ) --when a player enters a vehicle
    if ( policeVehicles[getElementModel(source)] ) and ( not policeSkins[getElementModel(player)] ) then --if the vehicle is one of 4 police cars, and the skin is not a police skin
        cancelEvent()
        outputChatBox ( "Only policeman can enter police cars!", player ) --and tell the player why
    end
end
addEventHandler ( "onVehicleStartEnter", getRootElement(), enterVehicle ) --add an event handler for onVehicleStartEnter
```

## See Also

### Vehicle events

- [onTrailerAttach](mta://scripting/server/events/ontrailerattach.md)

- [onTrailerDetach](mta://scripting/server/events/ontrailerdetach.md)

- [onVehicleDamage](mta://scripting/server/events/onvehicledamage.md)

- [onVehicleEnter](mta://scripting/server/events/onvehicleenter.md)

- [onVehicleExit](mta://scripting/server/events/onvehicleexit.md)

- [onVehicleExplode](mta://scripting/server/events/onvehicleexplode.md)

- [onVehicleRespawn](mta://scripting/server/events/onvehiclerespawn.md)

- onVehicleStartEnter

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

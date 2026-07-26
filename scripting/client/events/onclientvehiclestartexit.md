---
doc_id: "mta-wiki:2568"
title: "OnClientVehicleStartExit"
source_title: "OnClientVehicleStartExit"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientVehicleStartExit"
revision_id: 67847
language: "en"
categories: ["Client_events", "Changes_in_1.1"]
generated_at: "2026-07-26T16:16:20.657073+00:00"
---

# OnClientVehicleStartExit

This event is triggered when a [ped](mta://reference/misc/ped.md) or [player](mta://reference/misc/player.md) starts exiting a vehicle. Once the exiting animation completes, [onClientVehicleExit](mta://scripting/client/events/onclientvehicleexit.md) is triggered.

## Parameters

```
ped thePed, int seat, int door
```

- **thePed:** the ped who started exiting the vehicle.

- **seat:** the number of the seat that the ped was sitting on.

- **door:** the number of the door that the ped is using to leave.

## Source

The source of this event is the vehicle that the ped started to exit.

## Example

This example outputs to the player that he's leaving the drivers seat.

```
function exitingVehicle(player, seat, door)
	if (seat==0) and (door==0) then
		outputChatBox("You are leaving the drivers seat.")
	end
end
addEventHandler("onClientVehicleStartExit", getRootElement(), exitingVehicle)
```

## See Also

### Client vehicle events

- [onClientTrailerAttach](mta://scripting/client/events/onclienttrailerattach.md)

- [onClientTrailerDetach](mta://scripting/client/events/onclienttrailerdetach.md)

- [onClientVehicleCollision](mta://scripting/client/functions/onclientvehiclecollision.md)

- [onClientVehicleDamage](mta://scripting/client/events/onclientvehicledamage.md)

- [onClientVehicleEnter](mta://scripting/client/events/onclientvehicleenter.md)

- [onClientVehicleExit](mta://scripting/client/events/onclientvehicleexit.md)

- [onClientVehicleExplode](mta://scripting/client/events/onclientvehicleexplode.md)

- [onClientVehicleNitroStateChange](mta://scripting/client/events/onclientvehiclenitrostatechange.md)

- [onClientVehicleRespawn](mta://scripting/client/events/onclientvehiclerespawn.md)

- [onClientVehicleStartEnter](mta://scripting/client/events/onclientvehiclestartenter.md)

- onClientVehicleStartExit

- [onClientVehicleWeaponHit](mta://scripting/client/events/onclientvehicleweaponhit.md)

### Client event functions

- [triggerLatentServerEvent](mta://scripting/client/functions/triggerlatentserverevent.md)

- [triggerServerEvent](mta://scripting/client/functions/triggerserverevent.md)
  

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

---
doc_id: "mta-wiki:2567"
title: "OnClientVehicleStartEnter"
source_title: "OnClientVehicleStartEnter"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientVehicleStartEnter"
revision_id: 67845
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:20.638873+00:00"
---

# OnClientVehicleStartEnter

This event is triggered when a [ped](mta://reference/misc/ped.md) or [player](mta://reference/misc/player.md) starts entering a vehicle. Once the entering animation completes, [onClientVehicleEnter](mta://scripting/client/events/onclientvehicleenter.md) is triggered.

## Parameters

```
ped thePed, int seat, int door
```

- **thePed:** the ped that just started entering a vehicle.

- **seat:** the number of the seat he is going to sit on.

- **door:** An integer of which door the ped used (0-3). 0 is driver side door, 1 is front passenger, 2 is back left, 3 is back right.

## Source

The source of this event is the vehicle the ped is entering.

## Cancel effect

This event can be [canceled](mta://reference/misc/event-system.md), but only for the local player or peds synced by the client. If cancelled, they will not begin to the enter the vehicle.

## Example

This example outputs if the local player is about to enter the drivers seat.

```
addEventHandler("onClientVehicleStartEnter", root, function(player,seat,door)
	if (player == localPlayer and seat == 0)then
		outputChatBox("You are going to sit in the drivers seat.")
	end
end)
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

- onClientVehicleStartEnter

- [onClientVehicleStartExit](mta://scripting/client/events/onclientvehiclestartexit.md)

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

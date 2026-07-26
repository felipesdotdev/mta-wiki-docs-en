---
doc_id: "mta-wiki:2570"
title: "OnClientTrailerDetach"
source_title: "OnClientTrailerDetach"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientTrailerDetach"
revision_id: 82154
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:20.441919+00:00"
---

# OnClientTrailerDetach

This event is triggered when a trailer gets detached from its towing vehicle.

## Parameters

```
vehicle towedBy
```

- **towedBy:** the vehicle that was towing the trailer.

## Source

The source of this event is the trailer that is now detached.

## Example

This example outputs to the player that's towing the trailer that "The vehicle is now detached". (TESTED!)

```
addEventHandler("onClientTrailerDetach",root,function(towedBy)
	player = getVehicleOccupant(towedBy,0)
	outputChatBox("The vehicle is now detached.")
end)
```

## See Also

### Client vehicle events

- [onClientTrailerAttach](mta://scripting/client/events/onclienttrailerattach.md)

- onClientTrailerDetach

- [onClientVehicleCollision](mta://scripting/client/functions/onclientvehiclecollision.md)

- [onClientVehicleDamage](mta://scripting/client/events/onclientvehicledamage.md)

- [onClientVehicleEnter](mta://scripting/client/events/onclientvehicleenter.md)

- [onClientVehicleExit](mta://scripting/client/events/onclientvehicleexit.md)

- [onClientVehicleExplode](mta://scripting/client/events/onclientvehicleexplode.md)

- [onClientVehicleNitroStateChange](mta://scripting/client/events/onclientvehiclenitrostatechange.md)

- [onClientVehicleRespawn](mta://scripting/client/events/onclientvehiclerespawn.md)

- [onClientVehicleStartEnter](mta://scripting/client/events/onclientvehiclestartenter.md)

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

---
doc_id: "mta-wiki:2566"
title: "OnClientVehicleExit"
source_title: "OnClientVehicleExit"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientVehicleExit"
revision_id: 77542
language: "en"
categories: ["Client_events"]
---

# OnClientVehicleExit

This event gets fired when a [ped](https://wiki.multitheftauto.com/index.php?search=ped) or [player](https://wiki.multitheftauto.com/index.php?search=player) gets out of a vehicle.

## Parameters

```
ped thePed, int seat
```

- **thePed:** the [player](https://wiki.multitheftauto.com/index.php?search=player) or [ped](https://wiki.multitheftauto.com/index.php?search=ped) element that exited the vehicle

- **seat:** the number of the seat that the player was sitting on. 0 = driver, higher numbers are passenger seats.

## Source

The source of the event is the vehicle that the ped exited.

## Example

This code updates a GUI label with the name of the vehicle the local player is in.

```
lblVehicle = guiCreateLabel(10, 200, 150, 20, "Currently on foot", false)
addEventHandler("onClientVehicleEnter", getRootElement(),
    function(thePlayer, seat)
        if thePlayer == localPlayer then
            guiSetText(lblVehicle, "Currently in a " .. getVehicleName(source))
        end
    end
)

addEventHandler("onClientVehicleExit", getRootElement(),
    function(thePlayer, seat)
        if thePlayer == localPlayer then
            guiSetText(lblVehicle, "Currently on foot")
        end
    end
)
```

## See Also

### Client vehicle events

- [onClientTrailerAttach](mta://scripting/client/events/onclienttrailerattach.md)

- [onClientTrailerDetach](mta://scripting/client/events/onclienttrailerdetach.md)

- [onClientVehicleCollision](mta://scripting/client/functions/onclientvehiclecollision.md)

- [onClientVehicleDamage](mta://scripting/client/events/onclientvehicledamage.md)

- [onClientVehicleEnter](mta://scripting/client/events/onclientvehicleenter.md)

- onClientVehicleExit

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

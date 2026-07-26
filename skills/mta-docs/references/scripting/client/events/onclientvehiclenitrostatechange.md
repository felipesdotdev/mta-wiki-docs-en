---
doc_id: "mta-wiki:7103"
title: "OnClientVehicleNitroStateChange"
source_title: "OnClientVehicleNitroStateChange"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientVehicleNitroStateChange"
revision_id: 44028
language: "en"
categories: ["Client_events"]
---

# OnClientVehicleNitroStateChange

This event gets triggered when nitro state is changing.

| [[{{{image}}}\|link=\|]] | Note: This event is only triggered for vehicles that are streamed in |
| --- | --- |
|  |  |

## Parameters

```
bool state
```

- **state:** current state of nitro

## Source

The source of this event is the player vehicle.

## Example

This example is showing short chat message on nitro state changing.

Click to collapse [-]
Client

```
function nitro_updateState(state)    
    if state then
        outputChatBox("Nitro #00FF00activated!", 255, 200, 0, true)
    elseif not state then
        outputChatBox("Nitro #FF0000deactivated!", 255, 200, 0, true)
    end
end   
addEventHandler("onClientVehicleNitroStateChange", root,  nitro_updateState)
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

- onClientVehicleNitroStateChange

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

---
doc_id: "mta-wiki:1838"
title: "OnVehicleDamage"
source_title: "OnVehicleDamage"
source_url: "https://wiki.multitheftauto.com/wiki/OnVehicleDamage"
revision_id: 59524
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:26.457691+00:00"
---

# OnVehicleDamage

This event is triggered when a vehicle is damaged. If you want to get the attacker you can use [onClientVehicleDamage](mta://scripting/client/events/onclientvehicledamage.md).

## Parameters

```
float loss
```

- **loss**: a [float](mta://reference/misc/float.md) representing the amount of health the [vehicle](mta://reference/misc/vehicle.md) lost.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [vehicle](mta://reference/misc/vehicle.md) that got damaged.

## Example

This example displays a message with the amount of health lost when a vehicle gets damaged.

```
function displayVehicleLoss(loss)
    local thePlayer = getVehicleOccupant(source)
    if(thePlayer) then -- Check there is a player in the vehicle
        outputChatBox("Your vehicle just lost " .. tonumber(loss) .. " health.", thePlayer) -- Display the message
    end
end

addEventHandler("onVehicleDamage", root, displayVehicleLoss)
```

## See Also

### Vehicle events

- [onTrailerAttach](mta://scripting/server/events/ontrailerattach.md)

- [onTrailerDetach](mta://scripting/server/events/ontrailerdetach.md)

- onVehicleDamage

- [onVehicleEnter](mta://scripting/server/events/onvehicleenter.md)

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

---
doc_id: "mta-wiki:1839"
title: "OnVehicleRespawn"
source_title: "OnVehicleRespawn"
source_url: "https://wiki.multitheftauto.com/wiki/OnVehicleRespawn"
revision_id: 59528
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:26.548786+00:00"
---

# OnVehicleRespawn

This event is triggered when a vehicle is respawned due. See [toggleVehicleRespawn](mta://scripting/server/functions/togglevehiclerespawn.md).

## Parameters

```
bool exploded
```

- **exploded**: *true* if this vehicle respawned because it exploded, *false* if it respawned due to being deserted.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [vehicle](mta://reference/misc/vehicle.md) that respawned.

## Example

This example shows a message in the chatbox, if it is respawned.

```
function onVehicleRespawn ( exploded )
  -- Add this variable. It contains the vehicle name of the respawned vehicle
  local vehicleName = getVehicleName ( source )
  
  -- If it is exploded, echo a custom message
  if ( exploded == true ) then 
    outputChatBox("A " .. vehiclename .. " has been respawned, after an explosion")
  
  -- else echo a normal message
  else 
    outputChatBox("A " .. vehiclename .. " has been respawned")
  end
end

-- Add the Event Handler
addEventHandler ( "onVehicleRespawn", getRootElement(), onVehicleRespawn )
```

## See Also

### Vehicle events

- [onTrailerAttach](mta://scripting/server/events/ontrailerattach.md)

- [onTrailerDetach](mta://scripting/server/events/ontrailerdetach.md)

- [onVehicleDamage](mta://scripting/server/events/onvehicledamage.md)

- [onVehicleEnter](mta://scripting/server/events/onvehicleenter.md)

- [onVehicleExit](mta://scripting/server/events/onvehicleexit.md)

- [onVehicleExplode](mta://scripting/server/events/onvehicleexplode.md)

- onVehicleRespawn

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

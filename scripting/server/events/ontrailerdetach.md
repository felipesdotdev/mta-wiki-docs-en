---
doc_id: "mta-wiki:1843"
title: "OnTrailerDetach"
source_title: "OnTrailerDetach"
source_url: "https://wiki.multitheftauto.com/wiki/OnTrailerDetach"
revision_id: 59523
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:26.417576+00:00"
---

# OnTrailerDetach

This event is triggered when a trailer is detached from a truck.

## Parameters

```
vehicle theTruck
```

- **theTruck**: the truck [vehicle](mta://reference/misc/vehicle.md) that this trailer got detached from.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the trailer [vehicle](mta://reference/misc/vehicle.md) that the truck got detached from.

## Example

This example re-attaches a trailer when it detaches.

```
function reattachTrailer(theTruck)
    attachTrailerToVehicle(theTruck, source) -- Reattach the truck and trailer
end

addEventHandler("onTrailerDetach", getRootElement(), reattachTrailer)
```

## See Also

### Vehicle events

- [onTrailerAttach](mta://scripting/server/events/ontrailerattach.md)

- onTrailerDetach

- [onVehicleDamage](mta://scripting/server/events/onvehicledamage.md)

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

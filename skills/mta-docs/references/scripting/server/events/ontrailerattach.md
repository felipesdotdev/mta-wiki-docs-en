---
doc_id: "mta-wiki:1842"
title: "OnTrailerAttach"
source_title: "OnTrailerAttach"
source_url: "https://wiki.multitheftauto.com/wiki/OnTrailerAttach"
revision_id: 82045
language: "en"
categories: ["Server_Events", "Needs_Checking"]
---

# OnTrailerAttach

|  | This article needs checking. |
| --- | --- |
| Reason(s): Cancellation of event has no effect. detachTrailerFromVehicle in the event doesn't work either, 50 ms timer is effective. |  |

This event is triggered when a trailer is attached to a truck or when a tow truck hooks on to a vehicle.

## Parameters

```
vehicle theTruck
```

- **theTruck**: the truck [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle) that got attached to this trailer.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the trailer [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle) that the truck got attached to.

## Cancel effect

| [[\|link=\|]] | Warning: Canceling doesn't appear to work. |
| --- | --- |
|  |  |

If this event is [canceled](mta://reference/misc/event-system.md), the trailer will detach from the truck again.

## Example

This example removes a trailer from the truck it is attached to. Good if you do not want people attaching trailers to vehicles

```
function detachTrailer(theTruck)
    --detachTrailerFromVehicle(theTruck, source) --detach the newly attached trailer
    -- Immediate detatchment of the trailer through cancel event or this method doesn't seem to work so requires a timer:
    setTimer(detachTrailer2, 50, 1, theTruck, source)
end
addEventHandler("onTrailerAttach", getRootElement(), detachTrailer)

function detachTrailer2(theTruck, trailer)
    if (isElement(theTruck) and isElement(trailer)) then
        detachTrailerFromVehicle(theTruck, trailer)
    end
end
```

## See Also

### Vehicle events

- onTrailerAttach

- [onTrailerDetach](mta://scripting/server/events/ontrailerdetach.md)

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
